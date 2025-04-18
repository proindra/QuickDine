# 🍽️ Restaurant Booking System

A web-based restaurant table reservation system built with **Python**, **Streamlit**, and **CSV** data files — allowing users to search restaurants, check table availability, make bookings, and manage reservations.

---

## 🌐 Live Demo

> Coming soon on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📁 Project Structure
---
title: "Restaurant Booking System"
description: "A Streamlit-based restaurant reservation system using Python and CSV"
author: "Prajwal"
tags: [python, streamlit, csv, project, restaurant booking]
---

# 🍽️ Restaurant Booking System

A responsive, user-friendly restaurant reservation system built with **Python** and **Streamlit**. Users can view restaurants, check availability, make table reservations, and manage bookings. All data is stored using simple **CSV files** — no database required!

---

## 📦 Features

- 🔐 **User Login** (via CSV)
- 🏪 **Search & Filter Restaurants**
- 📅 **Date, Time, and Party Size Booking**
- ✅ **Check Availability & Confirm Reservation**
- 📖 **View & Cancel Bookings**
- 💾 **Persistent Storage with CSV**

---

## 📁 Project Structure

---

## 🛠️ Tech Stack

| Tool       | Use Case                    |
|------------|-----------------------------|
| Python     | Core programming language   |
| Streamlit  | Web interface & UI engine   |
| CSV        | Data persistence (lightweight database alternative) |

---

📑 CSV File Formats

🧍 users.csv

user_id,name,email,phone_number,current_bookings
U1,John Doe,john@example.com,1234567890,"[]"

🍴 restaurants.csv

restaurant_id,name,cuisine_type,rating,location,total_tables,table_configuration,opening_hours,closing_hours
R1,The Gourmet Spot,Italian,4.6,New York,10,"{'2-Seat': 4, '4-Seat': 4}",10:00,22:00

📅 bookings.csv

booking_id,user_id,restaurant_id,table_id,date,time,party_size
B-1683560189.12,U1,R1,4-Seat-1,2025-04-20,19:30,4


---

📄 License

This project is licensed under the MIT License.
You are free to use, modify, distribute, and build upon it for personal or commercial use.


---

### Key Changes:
1. **Fixed the Installation Section:** 
   - Added code blocks around the install and run commands for better readability.
2. **Improved CSV File Format Descriptions:** 
   - The CSV examples now appear in proper code blocks for better structure.
3. **Corrected the Heading Format:** 
   - In the "Installation & Run" section, I ensured the headings were more consistent.
4. **Minor Consistency Improvements:** 
   - Tidied up some formatting and made sure sections like "Tech Stack" and "License" were clearly separated.

Feel free to modify further based on your project's specific needs.


## 💻 Installation & Run

### 📌 Requirements

- Python 3.8+
- pip

### 🚀 Run the App

Make sure you've installed the dependencies:

pip install streamlit

Then run the app using:

streamlit run app.py


---
### 📦 Install dependencies

```bash
pip install streamlit
