import csv
import json
from datetime import datetime

class Restaurant:
    def __init__(self, restaurant_id, name, cuisine_type, rating, location,
                 total_tables, table_configuration, opening_hours, closing_hours):
        self.restaurant_id = restaurant_id
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.location = location
        self.total_tables = total_tables
        self.table_configuration = table_configuration
        self.opening_hours = opening_hours
        self.closing_hours = closing_hours

    def get_available_tables(self, date, time, party_size):
        try:
            with open('bookings.csv', 'r') as file:
                reader = csv.DictReader(file)
                booked_tables = [row['table_id'] for row in reader
                                 if row['restaurant_id'] == self.restaurant_id and
                                    row['date'] == date and
                                    row['time'] == time]
        except FileNotFoundError:
            booked_tables = []

        available_tables = []
        for table_type, count in self.table_configuration.items():
            if int(table_type.split('-')[0]) >= party_size:
                for i in range(count):
                    table_id = f"{table_type}-{i+1}"
                    if table_id not in booked_tables:
                        available_tables.append(table_id)
        return available_tables

    def check_valid_booking_time(self, time):
        opening = datetime.strptime(self.opening_hours, "%H:%M").time()
        closing = datetime.strptime(self.closing_hours, "%H:%M").time()
        booking_time = datetime.strptime(time, "%H:%M").time()
        return opening <= booking_time <= closing

class User:
    def __init__(self, user_id, name, email, phone_number, current_bookings):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.current_bookings = json.loads(current_bookings) if isinstance(current_bookings, str) else current_bookings

    def make_reservation(self, restaurant_id, date, time, table_id, party_size):
        booking_id = f"B-{datetime.now().timestamp()}"
        with open('bookings.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                booking_id,
                self.user_id,
                restaurant_id,
                table_id,
                date,
                time,
                party_size
            ])

        booking_data = {
            "booking_id": booking_id,
            "restaurant_id": restaurant_id,
            "date": date,
            "time": time,
            "table_id": table_id,
            "party_size": party_size
        }
        self.current_bookings.append(booking_data)
        return booking_id

    def cancel_reservation(self, booking_id):
        rows = []
        booking_found = False

        try:
            with open('bookings.csv', 'r') as file:
                reader = csv.reader(file)
                headers = next(reader)
                for row in reader:
                    if row[0] != booking_id:
                        rows.append(row)
                    else:
                        booking_found = True

            if booking_found:
                with open('bookings.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
                    writer.writerows(rows)

                self.current_bookings = [b for b in self.current_bookings if b.get("booking_id") != booking_id]
                return True
            return False

        except FileNotFoundError:
            return False

    def get_booking_history(self):
        return self.current_bookings
