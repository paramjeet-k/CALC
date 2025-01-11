import streamlit as st
import math

# Title
st.title("SIP Calculator")
st.subheader("Calculate your investment maturity amount")

# Inputs
st.write("Enter your SIP details below:")

monthly_investment = st.number_input("Monthly Investment Amount (₹):", min_value=100, step=100)
annual_rate_of_return = st.number_input("Expected Annual Rate of Return (%):", min_value=0.0, step=0.1)
investment_duration = st.slider("Investment Duration (Years):", 1, 30, 5)

# Calculate SIP Maturity Amount
if monthly_investment > 0 and annual_rate_of_return > 0:
    monthly_rate_of_return = annual_rate_of_return / 12 / 100
    total_months = investment_duration * 12

    # SIP Future Value Formula
    maturity_value = monthly_investment * (
        (math.pow(1 + monthly_rate_of_return, total_months) - 1) / monthly_rate_of_return
    ) * (1 + monthly_rate_of_return)

    # Display Results
    st.write(f"Your maturity amount after {investment_duration} years will be:")
    st.success(f"₹{maturity_value:,.2f}")

# Show additional details
st.write("### SIP Summary")
st.write(f"- Monthly Investment: ₹{monthly_investment:,.2f}")
st.write(f"- Annual Rate of Return: {annual_rate_of_return}%")
st.write(f"- Investment Duration: {investment_duration} years")
