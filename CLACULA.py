import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Empowering Women with AI Financial Tools")
st.subheader("AI Budgeting Tool for Financial Independence")

# Tabs for Features
tabs = st.tabs([
    "User-Friendly Interface",
    "Personalized Budgeting Plans",
    "Expense Tracking",
    "Financial Education Resources",
    "Goal Setting & Progress Tracking",
    "Community Support"
])

# Tab 1: User-Friendly Interface
with tabs[0]:
    st.header("Welcome to Your Budgeting Assistant!")
    st.write("This tool is designed with simplicity in mind to help you manage your finances effectively.")
    language = st.radio("Choose Language:", ("English", "Hindi"))
    if language == "Hindi":
        st.write("नमस्ते! इस बजटिंग टूल का उपयोग शुरू करें।")
    else:
        st.write("Hello! Get started with this budgeting tool.")

# Tab 2: Personalized Budgeting Plans
with tabs[1]:
    st.header("Personalized Budgeting Plans")
    income = st.number_input("Enter Your Monthly Income (₹):", min_value=0, step=1000)
    essential_expenses = st.number_input("Enter Essential Expenses (₹):", min_value=0, step=100)
    savings_goal = st.number_input("Enter Monthly Savings Goal (₹):", min_value=0, step=100)
    discretionary_spending = income - essential_expenses - savings_goal
    st.write(f"Your discretionary spending amount is: ₹{discretionary_spending}")
    if discretionary_spending < 0:
        st.warning("Your expenses exceed your income! Adjust your budget.")
    else:
        st.success("Your budget is balanced.")

# Tab 3: Expense Tracking
with tabs[2]:
    st.header("Expense Tracking")
    categories = ["Food", "Health", "Household", "Education", "Other"]
    expense_data = {category: st.number_input(f"Enter expenses for {category} (₹):", min_value=0, step=100) for category in categories}
    total_expenses = sum(expense_data.values())
    st.write(f"Total Expenses: ₹{total_expenses}")
    if total_expenses > income:
        st.warning("Expenses exceed your income! Reduce spending.")
    else:
        st.success("You're within your budget.")

    # Visualize expenses
    fig, ax = plt.subplots()
    ax.pie(expense_data.values(), labels=expense_data.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

# Tab 4: Financial Education Resources
with tabs[3]:
    st.header("Financial Education Resources")
    st.write("Learn about budgeting, investments, and financial planning:")
    st.markdown("""
    - [Basics of Budgeting](https://www.investopedia.com/budgeting-guide-5189530)
    - [Understanding Mutual Funds](https://www.amfiindia.com/)
    - [Smart Saving Tips](https://www.nerdwallet.com/article/finance/saving-money-tips)
    """)

# Tab 5: Goal Setting & Progress Tracking
with tabs[4]:
    st.header("Goal Setting & Progress Tracking")
    goal = st.text_input("Set Your Financial Goal (e.g., Buy Sewing Machine):", "Buy Sewing Machine")
    goal_amount = st.number_input(f"Enter the cost for {goal} (₹):", min_value=0, step=1000)
    months_to_save = st.slider("Set the timeframe to achieve this goal (in months):", 1, 36, 12)
    monthly_saving_required = goal_amount / months_to_save
    st.write(f"To achieve your goal in {months_to_save} months, you need to save ₹{monthly_saving_required:.2f} per month.")
    progress = st.slider("Track your savings progress (%):", 0, 100)
    st.write(f"You've completed {progress}% of your savings goal.")

# Tab 6: Community Support
with tabs[5]:
    st.header("Community Support")
    st.write("Join our community forums to share your experiences and get advice:")
    st.markdown("""
    - [Financial Literacy Forum](https://forum.financialliteracy.com)
    - [Women's Financial Support Group](https://www.womensfinancialsupport.org)
    """)
    st.button("Join Now")

# Footer
st.write("---")
st.write("This tool is powered by AI to support financial empowerment. 🚀")
