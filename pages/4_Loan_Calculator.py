import streamlit as st

st.title("SBA Loan Cash Flow Calculator")

st.write("""
This calculator helps you determine the required monthly cash flow for SBA loans.

A conservative rule of thumb for SBA loans is 1,200 monthly for every 100,000. 
Lenders want to see 2x loan coverage, so the monthly cash flow needs to be 2,400 per month per 100,000 in price.
""")

list_price = st.number_input("Enter the list price for the business ($):", min_value=0.0, step=100000.0)
reported_cashflows = st.number_input("Enter your reported monthly cash flows ($):", min_value=0.0, step=100.0)

if list_price > 0:
    down_payment = list_price * 0.1
    loan_amount = list_price - down_payment
    estimated_loan_payment = (loan_amount / 100000) * 1200
    required_cashflow = (loan_amount / 100000) * 2400
    cashflow_after_loan_payment = reported_cashflows - estimated_loan_payment
    
    st.write(f"#### List Price: ${list_price:,.2f}")
    st.write(f"#### Down Payment (10%): ${down_payment:,.2f}")
    st.write(f"#### Loan Amount: ${loan_amount:,.2f}")
    st.write(f"#### Reported Monthly Cash Flows: ${reported_cashflows:,.2f}")
    st.write(f"#### Required Monthly Cash Flow: ${required_cashflow:,.2f}")
    st.write(f"#### Estimated Monthly Loan Payment: ${estimated_loan_payment:,.2f}")
    st.write(f"#### Cash Flow After Loan Payment: ${cashflow_after_loan_payment:,.2f}")
    
    # Visual validation
    if required_cashflow > reported_cashflows:
        st.error("The reported cash flow is less than the required cash flow. You might need to increase your monthly cash flow.")
    else:
        st.success("The reported cash flow is sufficient to cover the required cash flow.")
else:
    st.write("Please enter the list price for the business to calculate the required monthly cash flow.")
