import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd

# Load users from secrets
users = st.secrets["users"]

# Create the credentials dictionary
credentials = {"usernames": {}}
for user in users["usernames"]:
    credentials["usernames"][user["username"]] = {
        "name": user["name"],
        "password": user["password"],
    }

# Function to hash passwords
hashed_passwords = stauth.Hasher(
    [credentials["usernames"][user]["password"] for user in credentials["usernames"]]
).generate()

# Update the credentials dictionary with hashed passwords
for i, user in enumerate(credentials["usernames"]):
    credentials["usernames"][user]["password"] = hashed_passwords[i]

# Initialize authenticator
authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)

# Add login form
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.write(f"Welcome *{name}*")
    st.title('Operating Expenses Tracker')

    # Hardcoded expenses with type of payment
    expenses = [
        {"Type": "API", "Amount": 20.00, "Date": "2024-06-01", "Payment Type": "Recurring"},
        {"Type": "Domains", "Amount": 24.00, "Date": "2024-06-01", "Payment Type": "One-Time"},
    ]

    # Convert expenses to a DataFrame
    df_expenses = pd.DataFrame(expenses)

    # Separate recurring and one-time expenses
    df_recurring_expenses = df_expenses[df_expenses['Payment Type'] == "Recurring"]
    df_one_time_expenses = df_expenses[df_expenses['Payment Type'] == "One-Time"]

    # Display the list of recurring expenses
    st.header("Recurring Expenses Summary")
    st.dataframe(df_recurring_expenses)

    # Display total recurring expenses
    total_recurring = df_recurring_expenses['Amount'].sum()
    st.write(f"**Total Recurring Expenses:** ${total_recurring:,.2f}")

    # Display the list of one-time expenses
    st.header("One-Time Expenses Summary")
    st.dataframe(df_one_time_expenses)

    # Display total one-time expenses
    total_one_time = df_one_time_expenses['Amount'].sum()
    st.write(f"**Total One-Time Expenses:** ${total_one_time:,.2f}")

    # Button to download recurring expenses as a CSV file
    csv_recurring_expenses = df_recurring_expenses.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Recurring Expenses as CSV",
        data=csv_recurring_expenses,
        file_name='recurring_expenses.csv',
        mime='text/csv'
    )

    # Button to download one-time expenses as a CSV file
    csv_one_time_expenses = df_one_time_expenses.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download One-Time Expenses as CSV",
        data=csv_one_time_expenses,
        file_name='one_time_expenses.csv',
        mime='text/csv'
    )

    # Hardcoded wishlist
    wishlist = [
        {"Item": "Vellum", "Estimated Cost": 250.00, "Payment Type": "One-Time"},
        {"Item": "Otter.ai", "Estimated Cost": 90.00, "Payment Type": "Recurring"},
        {"Item": "ChatGPT Workspace", "Estimated Cost": 90.00, "Payment Type": "Recurring"},
        {"Item": "Google Workspace", "Estimated Cost": 20.00, "Payment Type": "Recurring"},
        {"Item": "KDSpy", "Estimated Cost": 69.00, "Payment Type": "One-Time"},
    ]

    # Convert wishlist to a DataFrame
    df_wishlist = pd.DataFrame(wishlist)

    # Display the wishlist
    st.header("Wishlist")
    st.dataframe(df_wishlist)

    # Display total estimated cost
    total_wishlist_cost = df_wishlist['Estimated Cost'].sum()
    total_wishlist_recurring = df_wishlist[df_wishlist['Payment Type'] == "Recurring"]['Estimated Cost'].sum()
    total_wishlist_one_time = df_wishlist[df_wishlist['Payment Type'] == "One-Time"]['Estimated Cost'].sum()

    st.write(f"**Total Estimated Cost:** ${total_wishlist_cost:,.2f}")
    st.write(f"**Total Recurring Estimated Cost:** ${total_wishlist_recurring:,.2f}")
    st.write(f"**Total One-Time Estimated Cost:** ${total_wishlist_one_time:,.2f}")

    # Button to download wishlist as a CSV file
    csv_wishlist = df_wishlist.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Wishlist as CSV",
        data=csv_wishlist,
        file_name='wishlist.csv',
        mime='text/csv'
    )
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

authenticator.logout('Logout', 'main')
