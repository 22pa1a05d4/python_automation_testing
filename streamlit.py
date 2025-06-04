

import streamlit as st
import requests

# --- Step 1: Simple Login Setup ---
st.title("🔐 Login")

# Hardcoded username and password (for demo)
correct_username = "admin"
correct_password = "1234"

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login success flag
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Check credentials
if st.button("Login"):
    if not username or not password:
        st.warning("⚠️ Please enter both username and password.")
    elif username == correct_username and password == correct_password:
        
        st.session_state.logged_in = True

#         Session State: 
# {
#   "logged_in": True,
#   "username": "admin",
#   "password": "1234"
# }

        st.success("✅ Logged in successfully!")
    else:
        st.error("❌ Invalid username or password")

# --- Step 2: Show Converter if Logged In ---
if st.session_state.logged_in:
    st.title("💱 Real-Time Currency Converter")

    amount = st.number_input("Enter amount", min_value=0.0, format="%.2f")
    from_currency = st.selectbox("From Currency", ["USD", "EUR", "INR", "JPY", "GBP"])
    to_currency = st.selectbox("To Currency", ["USD", "EUR", "INR", "JPY", "GBP"])

    if st.button("Convert"):
        if from_currency == to_currency:
            st.warning("Please select two different currencies.")
        else:
            url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
            try:
                response = requests.get(url)
                data = response.json()

                if "rates" in data and to_currency in data["rates"]:
                    result = data["rates"][to_currency]
                    st.success(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
                else:
                    st.error("Conversion failed. Check currencies.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
