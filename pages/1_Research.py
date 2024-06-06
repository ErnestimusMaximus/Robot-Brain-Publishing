import streamlit as st
import os

st.title('Robot Brain Publishing - Niche Research Guide')

st.write("Follow the steps below to manually conduct niche research.")

username = st.text_input("Enter your name")
if username != "":
    st.write(f"Hello, {username}!")
else: 
    st.write(f"What's your name?")

# List of niches
niches = [
    "Arts and photography",
    "Business and money",
    "Children's books (not picture books, but how-tos for kids like gardening)",
    "Food and wine (from around the world, not so much cookbooks)",
    "Computers and technology",
    "Crafts or hobbies and home",
    "Education and teaching",
    "Health, fitness and dieting",
    "Humor and entertainment",
    "Parenting and relationships",
    "Self-help",
    "Sports and outdoors",
    "Travel"
]

# Step 1: Select a niche
st.header("Step 1: Select a Niche")
selected_niche = st.selectbox(
    "Select a niche to research",
    niches
)

st.write(f"You have selected the niche: {selected_niche}")

# Step 2: Analyze the top 20 best selling books on Amazon
st.header("Step 2: Analyze the Top 20 Best Selling Books on Amazon")
top_books = st.text_area("List the top 20 best selling books for the selected niche. Separate each book with a new line.")
if top_books:
    books = top_books.split('\n')
    st.write("You have entered the following books:")
    for book in books:
        st.write(f"- {book}")

# Step 3: Identify keywords/topics for each of the top 20 books
st.header("Step 3: Identify Keywords/Topics for Each of the Top 20 Books")
keywords = st.text_area("List keywords/topics for each book. Separate keywords for different books with a new line, and keywords for each book with commas.")
if keywords:
    keywords_list = keywords.split('\n')
    st.write("You have entered the following keywords/topics:")
    for i, book_keywords in enumerate(keywords_list, 1):
        st.write(f"Book {i} keywords: {book_keywords}")

# Step 4: Research each identified keyword/topic
st.header("Step 4: Research Each Identified Keyword/Topic")
keyword_research = st.text_area("For each keyword/topic, research to determine if there are at least 3 books on that topic making over $500 per month with less than 150 reviews. Enter your findings below.")
if keyword_research:
    research_results = keyword_research.split('\n')
    st.write("You have entered the following research results:")
    for result in research_results:
        st.write(f"- {result}")

# Initialize profitable_list
profitable_list = []

# Step 5: Identify the most profitable niche and keyword opportunities
st.header("Step 5: Identify the Most Profitable Niche and Keyword Opportunities")
profitable_keywords = st.text_area("Based on your research, list the most profitable keywords/opportunities that meet the criteria.")
if profitable_keywords:
    profitable_list = profitable_keywords.split('\n')
    st.write("You have identified the following profitable keywords/opportunities:")
    for keyword in profitable_list:
        st.write(f"- {keyword}")

st.write("### Summary of Your Research")
summary_text = f"Selected Niche: {selected_niche}\n"
if top_books:
    summary_text += "Top 20 Best Selling Books:\n"
    for book in books:
        summary_text += f"- {book}\n"
if keywords:
    summary_text += "Identified Keywords/Topics:\n"
    for i, book_keywords in enumerate(keywords_list, 1):
        summary_text += f"Book {i} keywords: {book_keywords}\n"
if keyword_research:
    summary_text += "Keyword Research Results:\n"
    for result in research_results:
        summary_text += f"- {result}\n"
if profitable_keywords:
    summary_text += "Most Profitable Keywords/Opportunities:\n"
    for keyword in profitable_list:
        summary_text += f"- {keyword}\n"

st.text_area("Summary of Your Research", summary_text, height=300)

# Show the "Go to Book" button only if profitable_list is not blank
if profitable_list:
    if st.button("Go to Book"):
        st.session_state['selected_niche'] = selected_niche
        st.session_state['profitable_keywords'] = profitable_list
        st.write("Data saved! Please navigate to Book.py.")

# Button to download summary as a txt file
st.download_button(
    label="Download Summary as TXT",
    data=summary_text,
    file_name=f"{selected_niche}_research_summary.txt",
    mime='text/plain'
)
