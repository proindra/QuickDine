# 🍽️ Restaurant Booking System

A web-based restaurant reservation app built with **Python**, **Streamlit**, and **CSV** files. Users can **log in**, browse restaurants, check **table availability**, make **bookings**, and manage reservations — all via a sleek, responsive interface.

---

## 🌟 Features

- 🔐 **User Login & Session Management**
- 🍴 **Search Restaurants by Name**
- 📅 **Book Tables Based on Date, Time & Party Size**
- ✅ **Real-Time Availability Check**
- 🔁 **View & Cancel Existing Bookings**
- 💾 **CSV-based Persistent Storage** (No external database needed!)

---

## 🖼️ Preview

Coming soon to [Streamlit Cloud](https://streamlit.io/cloud) 🚀

---

## 🗂️ Project Structure

```bash
restaurant-booking/
├── app.py              # Streamlit app UI and logic
├── core.py             # Restaurant & User class logic
├── users.csv           # Registered user data
├── restaurants.csv     # Restaurant & table configuration data
├── bookings.csv        # All bookings data
```

---

## 📚 CSV Formats

**👤 users.csv**

```csv
user_id,name,email,phone_number,current_bookings
U1,John Doe,john@example.com,1234567890,"[]"
```

**🍽 restaurants.csv**

```csv
restaurant_id,name,cuisine_type,rating,location,total_tables,table_configuration,opening_hours,closing_hours
R1,The Gourmet Spot,Italian,4.6,New York,10,"{'2-Seat': 4, '4-Seat': 4}",10:00,22:00
```

**📅 bookings.csv**

```csv
booking_id,user_id,restaurant_id,table_id,date,time,party_size
B-1683560189.12,U1,R1,4-Seat-1,2025-04-20,19:30,4
```

---

## 🛠️ Tech Stack

| Tool         | Role                           |
| ------------ | ------------------------------ |
| Python 🐍    | Backend logic                  |
| Streamlit 🌐 | Web UI & interactivity         |
| CSV 📄       | Lightweight persistent storage |

---

## 🚀 Quick Start

### ✅ Requirements

- Python 3.8+
- pip

### 🔧 Installation

```bash
pip install streamlit
```

### ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔍 Sample Code Snippets

### 📌 Checking Available Tables

```python
available_tables = selected_restaurant.get_available_tables(
    str(date), time.strftime("%H:%M"), party_size)
```

### 🧾 Confirming a Booking

```python
booking_id = user.make_reservation(
    restaurant_id, date, time, table_id, party_size)
```

---

## 🧰 Boilerplate Starter Code

### 📁 `app.py`

```python
import streamlit as st
from core import Restaurant, User
import pandas as pd

# Load CSV data
restaurants_df = pd.read_csv("restaurants.csv")
users_df = pd.read_csv("users.csv")
bookings_df = pd.read_csv("bookings.csv")

st.title("🍽️ Restaurant Booking System")

# --- Login Section ---
st.sidebar.header("🔐 Login")
user_email = st.sidebar.text_input("Email")
if st.sidebar.button("Login"):
    user_row = users_df[users_df['email'] == user_email]
    if not user_row.empty:
        st.session_state['user'] = user_row.iloc[0]
        st.success(f"Welcome, {user_row.iloc[0]['name']}!")
    else:
        st.error("User not found.")

# --- Restaurant Browser ---
st.header("📍 Available Restaurants")
search = st.text_input("Search by restaurant name")

filtered = restaurants_df[restaurants_df["name"].str.contains(search, case=False)] if search else restaurants_df
st.dataframe(filtered[["name", "cuisine_type", "rating", "location"]])

# --- Booking Interface ---
if "user" in st.session_state:
    st.subheader("📅 Book a Table")
    restaurant = st.selectbox("Choose Restaurant", filtered["name"])
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    party_size = st.number_input("Party Size", min_value=1, max_value=10)

    if st.button("Check Availability"):
        st.info("Check logic goes here…")
        # You'd fetch the selected restaurant object and call get_available_tables()

    if st.button("Confirm Booking"):
        st.success("Booking confirmed! ✅")
        # Here you'd call User.make_reservation and update CSVs
else:
    st.warning("Please log in to book a table.")
```

---

## 📄 License

Licensed under the MIT License. Feel free to use, modify, and distribute for personal or commercial projects.

---

## 🙌 Acknowledgments

Thanks to the open-source community and [Streamlit](https://streamlit.io) for enabling rapid app development!

---

Made with ❤️ by PRAJWALINDRA

