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
    st.title("Financial Goal Tracker")

    # Inputs for goal tracking
    goal_name = st.text_input("Enter your financial goal (e.g., Emergency Fund):")
    goal_amount = st.number_input(f"Enter the total amount for {goal_name} (₹):", min_value=0, step=1000)
    monthly_contribution = st.number_input("Enter your monthly savings contribution (₹):", min_value=0, step=100)

    if monthly_contribution > 0:
        months_needed = goal_amount / monthly_contribution
        st.write(f"You will achieve your goal in {months_needed:.2f} months.")
    else:
        st.warning("Please enter a valid monthly contribution to reach your goal.")








# Function for Expense Tracker
def expense_tracker():
    st.title("AI-Powered Expense Tracker")

    # Inputs for current month
    income = st.number_input("Enter your monthly income (₹):", min_value=0, step=1000)
    bills = st.number_input("Enter your monthly bills (₹):", min_value=0, step=100)
    savings_goal = st.number_input("Enter your monthly savings goal (₹):", min_value=0, step=100)

    # Historical data input
    st.write("### Provide your historical data (for AI predictions)")
    num_months = st.number_input("Number of past months to include:", min_value=3, max_value=24, step=1)
    historical_bills = st.text_area("Enter your monthly bills for each of the past months (₹), separated by commas:")

    # Calculate available money for the current month
    available_money = income - bills - savings_goal
    if available_money < 0:
        st.warning("Your expenses exceed your income. Please review your budget!")
    else:
        st.success(f"Your available money for spending this month: ₹{available_money:,.2f}")

    # AI Prediction Section
    if st.button("Predict Future Bills"):
        try:
            # Process historical data
            bills_list = [float(bill.strip()) for bill in historical_bills.split(",")]
            if len(bills_list) != num_months:
                st.error("The number of bills entered must match the number of months specified.")
                return

            # Prepare the training data
            X = np.arange(1, num_months + 1).reshape(-1, 1)  # Months (1, 2, ..., n)
            y = np.array(bills_list).reshape(-1, 1)  # Corresponding bills

            # Train a linear regression model
            model = LinearRegression()
            model.fit(X, y)

            # Predict future bills
            next_month = num_months + 1
            predicted_bill = model.predict([[next_month]])

            st.write(f"Based on your historical data, your predicted bill for Month {next_month} is:")
            st.success(f"₹{predicted_bill[0][0]:,.2f}")

            # Display model insights
            st.write("### Model Insights")
            st.write(f"- Monthly Bill Increase (Slope): ₹{model.coef_[0][0]:,.2f}")
            st.write(f"- Initial Bill Estimate (Intercept): ₹{model.intercept_[0]:,.2f}")

        except Exception as e:
            st.error(f"An error occurred: {e}")


# Main Streamlit App
def main():
    st.title("AI Budgeting Tool for Financial Empowerment")

    # Tabs for different tools
    tabs = st.tabs([
        "SIP Calculator",
        "Expense Tracker",
        "Goal Tracker",
        "Budget Planner",
        "AI Expense Tracker"
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

    with tab[4]:
        expense_tracker()
       
      
        

    # Footer
    st.write("---")
    st.write("This tool is powered by AI to support financial empowerment.")


if __name__ == "__main__":
    main()











# # Function for Expense Tracker
# def expense_tracker():
#     st.title("AI-Powered Expense Tracker")

#     # Inputs for current month
#     income = st.number_input("Enter your monthly income (₹):", min_value=0, step=1000)
#     bills = st.number_input("Enter your monthly bills (₹):", min_value=0, step=100)
#     savings_goal = st.number_input("Enter your monthly savings goal (₹):", min_value=0, step=100)

#     # Historical data input
#     st.write("### Provide your historical data (for AI predictions)")
#     num_months = st.number_input("Number of past months to include:", min_value=3, max_value=24, step=1)
#     historical_bills = st.text_area("Enter your monthly bills for each of the past months (₹), separated by commas:")

#     # Calculate available money for the current month
#     available_money = income - bills - savings_goal
#     if available_money < 0:
#         st.warning("Your expenses exceed your income. Please review your budget!")
#     else:
#         st.success(f"Your available money for spending this month: ₹{available_money:,.2f}")

#     # AI Prediction Section
#     if st.button("Predict Future Bills"):
#         try:
#             # Process historical data
#             bills_list = [float(bill.strip()) for bill in historical_bills.split(",")]
#             if len(bills_list) != num_months:
#                 st.error("The number of bills entered must match the number of months specified.")
#                 return

#             # Prepare the training data
#             X = np.arange(1, num_months + 1).reshape(-1, 1)  # Months (1, 2, ..., n)
#             y = np.array(bills_list).reshape(-1, 1)  # Corresponding bills

#             # Train a linear regression model
#             model = LinearRegression()
#             model.fit(X, y)

#             # Predict future bills
#             next_month = num_months + 1
#             predicted_bill = model.predict([[next_month]])

#             st.write(f"Based on your historical data, your predicted bill for Month {next_month} is:")
#             st.success(f"₹{predicted_bill[0][0]:,.2f}")

#             # Display model insights
#             st.write("### Model Insights")
#             st.write(f"- Monthly Bill Increase (Slope): ₹{model.coef_[0][0]:,.2f}")
#             st.write(f"- Initial Bill Estimate (Intercept): ₹{model.intercept_[0]:,.2f}")

#         except Exception as e:
#             st.error(f"An error occurred: {e}")


# # Main Streamlit App
# def main():
#     st.title("AI-Integrated Budgeting and Expense Tracking Tool")
    
#     # Tabs for functionalities
#     tabs = st.tabs([
#         "Expense Tracker",
#     ])

#     # Expense Tracker Tab
#     with tabs[0]:
#         expense_tracker()

#     # Footer
#     st.write("---")
#     st.write("This tool is powered by AI to support financial empowerment.")


# if __name__ == "__main__":
#     main()















