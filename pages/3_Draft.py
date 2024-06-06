import streamlit as st
import api

st.title('Book Draft')

# List of Genres
genres = [
    "Arts and Photography",
    "Business and Money",
    "Children's Books",
    "Food and Wine",
    "Computers and Technology",
    "Crafts or Hobbies and Home",
    "Education and Teaching",
    "Health, Fitness and Dieting",
    "Humor and Entertainment",
    "Parenting and Relationships",
    "Self-Help",
    "Sports and Outdoors",
    "Travel"
]

# Add a dropdown list for genres
selected_genre = st.selectbox("Select the Genre you want to write:", genres)

st.write(f"You selected: {selected_genre}")

# Add a text input for Book Title
book_title = st.text_input("Enter the Book Title:")

# Display the Book Title and selected genre
if book_title:
    st.write(f"Book Title: {book_title}")

# Conditional dropdown for available authors if "Self-Help" is selected
if selected_genre == "Self-Help":
    authors = {
        "Anxiety Self-Help Author": "asst_aB4g5eT5BVuGSXZKCPZ87SNx",
    }
    selected_author = st.selectbox("Available Authors:", list(authors.keys()))
    st.write(f"You selected: {selected_author}")

# Get list of Assistants from OpenAI API
assistants = api.list_assistants(st.secrets["openai_api_key"])
st.write(assistants)
