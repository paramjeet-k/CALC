import streamlit as st
import math

# Function for SIP Calculator
def sip_calculator():
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


# Function for Budget Planner
def budget_planner():
    st.title("Budget Planner")

    # Inputs for expenses
    food_expense = st.number_input("Enter your food expense (₹):", min_value=0, step=100)
    transport_expense = st.number_input("Enter your transport expense (₹):", min_value=0, step=100)
    entertainment_expense = st.number_input("Enter your entertainment expense (₹):", min_value=0, step=100)

    # Calculate total expenses
    total_expenses = food_expense + transport_expense + entertainment_expense
    st.write(f"Total Expenses: ₹{total_expenses}")

    # Display warnings or success
    if total_expenses > 5000:
        st.warning("Your expenses are high. Consider cutting back on non-essential spending!")
    else:
        st.success("You're within a reasonable spending limit!")


# Function for Expense Tracker (you can add more functionality based on your needs)
def expense_tracker():
    st.title("Expense Tracker")

    income = st.number_input("Enter your monthly income (₹):", min_value=0, step=1000)
    bills = st.number_input("Enter your monthly bills (₹):", min_value=0, step=100)
    savings_goal = st.number_input("Enter your monthly savings goal (₹):", min_value=0, step=100)

    # Calculate available money after bills and savings goal
    available_money = income - bills - savings_goal

    if available_money < 0:
        st.warning("Your expenses exceed your income. Please review your budget!")
    else:
        st.success(f"Your available money for spending this month: ₹{available_money}")


# Function for Goal Tracker
def goal_tracker():
    st.title("Financial Goal Tracker - Wally Model")

    # Inputs for goal tracking
    goal_name = st.text_input("Enter your financial goal (e.g., Emergency Fund):")
    goal_amount = st.number_input(f"Enter the total amount for {goal_name} (₹):", min_value=0, step=1000)
    monthly_contribution = st.number_input("Enter your monthly savings contribution (₹):", min_value=0, step=100)

    if monthly_contribution > 0:
        months_needed = goal_amount / monthly_contribution
        st.write(f"You will achieve your goal in {months_needed:.2f} months.")
    else:
        st.warning("Please enter a valid monthly contribution to reach your goal.")


# Main Streamlit App
def main():
    st.title("AI Budgeting Tool for Financial Empowerment")

    # Tabs for different tools
    tabs = st.tabs([
        "SIP Calculator",
        "Expense Tracker",
        "Goal Tracker",
        "Budget Planner"
    ])

    # Add the logic for each tab
    with tabs[0]:
        sip_calculator()

    with tabs[1]:
        expense_tracker()

    with tabs[2]:
        goal_tracker()

    with tabs[3]:
        budget_planner()

    # Footer
    st.write("---")
    st.write("This tool is powered by AI to support financial empowerment.")


if __name__ == "__main__":
    main()








import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Function for SIP Calculator
def sip_calculator():
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
            (np.power(1 + monthly_rate_of_return, total_months) - 1) / monthly_rate_of_return
        ) * (1 + monthly_rate_of_return)

        # Display Results
        st.write(f"Your maturity amount after {investment_duration} years will be:")
        st.success(f"₹{maturity_value:,.2f}")

    # Show additional details
    st.write("### SIP Summary")
    st.write(f"- Monthly Investment: ₹{monthly_investment:,.2f}")
    st.write(f"- Annual Rate of Return: {annual_rate_of_return}%")
    st.write(f"- Investment Duration: {investment_duration} years")


# Function for AI-Powered Expense Prediction
def ai_expense_prediction():
    st.title("AI-Powered Expense Prediction")

    # Collect historical data
    st.write("Enter your past monthly expenses to train the AI model:")
    months = st.number_input("Number of past months:", min_value=3, max_value=24, step=1)
    expenses = st.text_area("Enter your expenses for each month separated by commas (₹):")

    if st.button("Train Model and Predict"):
        try:
            # Prepare the data
            expenses_list = [float(expense.strip()) for expense in expenses.split(",")]
            if len(expenses_list) != months:
                st.error("The number of expenses must match the number of months.")
                return

            # Create training data
            X = np.arange(1, months + 1).reshape(-1, 1)
            y = np.array(expenses_list).reshape(-1, 1)

            # Train a linear regression model
            model = LinearRegression()
            model.fit(X, y)

            # Predict future expense
            future_month = months + 1
            predicted_expense = model.predict([[future_month]])

            st.write(f"Based on the given data, your predicted expense for Month {future_month} is:")
            st.success(f"₹{predicted_expense[0][0]:,.2f}")

            # Show regression details
            st.write("### Model Details")
            st.write(f"- Intercept: ₹{model.intercept_[0]:,.2f}")
            st.write(f"- Slope (Monthly Increase): ₹{model.coef_[0][0]:,.2f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")


# Function for Goal Tracker
def goal_tracker():
    st.title("Financial Goal Tracker - Wally Model")

    # Inputs for goal tracking
    goal_name = st.text_input("Enter your financial goal (e.g., Emergency Fund):")
    goal_amount = st.number_input(f"Enter the total amount for {goal_name} (₹):", min_value=0, step=1000)
    monthly_contribution = st.number_input("Enter your monthly savings contribution (₹):", min_value=0, step=100)

    if monthly_contribution > 0:
        months_needed = goal_amount / monthly_contribution
        st.write(f"You will achieve your goal in {months_needed:.2f} months.")
    else:
        st.warning("Please enter a valid monthly contribution to reach your goal.")


# Main Streamlit App
def main():
    st.title("AI-Powered Budgeting Tool for Financial Empowerment")

    # Tabs for different tools
    tabs = st.tabs([
        "SIP Calculator",
        "AI Expense Prediction",
        "Goal Tracker",
    ])

    # Add the logic for each tab
    with tabs[0]:
        sip_calculator()

    with tabs[1]:
        ai_expense_prediction()

    with tabs[2]:
        goal_tracker()

    # Footer
    st.write("---")
    st.write("This tool is powered by AI to support financial empowerment.")


if __name__ == "__main__":
    main()
















