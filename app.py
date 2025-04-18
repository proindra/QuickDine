import streamlit as st
import csv
import json
from datetime import datetime
from core import Restaurant, User

# ---------------------- Load Restaurants ----------------------
def load_restaurants():
    restaurants = []
    try:
        with open("restaurants.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                config = json.loads(row["table_configuration"].replace("'", '"'))
                restaurants.append(Restaurant(
                    restaurant_id=row["restaurant_id"],
                    name=row["name"],
                    cuisine_type=row["cuisine_type"],
                    rating=float(row["rating"]),
                    location=row["location"],
                    total_tables=int(row["total_tables"]),
                    table_configuration=config,
                    opening_hours=row["opening_hours"],
                    closing_hours=row["closing_hours"]
                ))
        return restaurants
    except Exception as e:
        st.error(f"Error loading restaurants: {e}")
        return []

# ---------------------- Load User ----------------------
def load_user(user_id):
    try:
        with open("users.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["user_id"] == user_id:
                    return User(
                        user_id=row["user_id"],
                        name=row["name"],
                        email=row["email"],
                        phone_number=row["phone_number"],
                        current_bookings=row["current_bookings"]
                    )
    except Exception as e:
        st.error(f"Error loading user: {e}")
    return None

# ---------------------- Streamlit UI ----------------------
st.set_page_config(page_title="Restaurant Booking System", layout="centered")
st.title("🍽️ Restaurant Booking System")

# Session state for user
if "user" not in st.session_state:
    st.session_state.user = None

with st.sidebar:
    st.header("🔐 User Login")
    user_id = st.text_input("Enter your User ID")
    if st.button("Login"):
        user = load_user(user_id)
        if user:
            st.session_state.user = user
            st.success(f"Welcome, {user.name}!")
        else:
            st.error("User not found.")

if st.session_state.user:
    restaurants = load_restaurants()
    restaurant_names = [r.name for r in restaurants]

    st.subheader("🔍 Search & Book a Table")
    selected_restaurant_name = st.selectbox("Choose Restaurant", restaurant_names)
    date = st.date_input("Choose Date")
    time = st.time_input("Choose Time")
    party_size = st.number_input("Party Size", min_value=1, value=2)

    selected_restaurant = next(r for r in restaurants if r.name == selected_restaurant_name)

    # Session state for availability
    if "available_tables" not in st.session_state:
        st.session_state.available_tables = []

    if st.button("Check Availability"):
        if selected_restaurant.check_valid_booking_time(time.strftime("%H:%M")):
            available_tables = selected_restaurant.get_available_tables(
                str(date), time.strftime("%H:%M"), party_size)
            if available_tables:
                st.session_state.available_tables = available_tables
                st.success("Available tables found!")
            else:
                st.session_state.available_tables = []
                st.warning("No tables available for this selection.")
        else:
            st.session_state.available_tables = []
            st.error("Selected time is outside restaurant operating hours.")

    if st.session_state.available_tables:
        table_choice = st.selectbox("Select Table", st.session_state.available_tables)
        if st.button("Confirm Booking"):
            booking_id = st.session_state.user.make_reservation(
                selected_restaurant.restaurant_id,
                str(date), time.strftime("%H:%M"),
                table_choice, party_size
            )
            st.success(f"✅ Booking Confirmed! Your booking ID is {booking_id}")
            st.session_state.available_tables = []  # Clear availability after booking

    st.divider()
    st.subheader("📖 Your Bookings")
    for booking in st.session_state.user.get_booking_history():
        st.markdown(f"**Booking ID:** {booking['booking_id']}")
        st.text(f"Restaurant: {booking['restaurant_id']}\nDate: {booking['date']}  Time: {booking['time']}\nTable: {booking['table_id']}  Size: {booking['party_size']}")
        if st.button(f"Cancel {booking['booking_id']}"):
            if st.session_state.user.cancel_reservation(booking['booking_id']):
                st.success("Booking cancelled!")
            else:
                st.error("Failed to cancel booking.")
