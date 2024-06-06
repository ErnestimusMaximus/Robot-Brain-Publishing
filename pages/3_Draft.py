import streamlit as st
import api

st.title('Book Draft')

# List of Assistants
genres = [
    "Arts and Photography Author",
    "Business and Money Author",
    "Children's Books Author",
    "Food and Wine Author",
    "Computers and Technology Author",
    "Crafts or Hobbies and Home Author",
    "Education and Teaching Author",
    "Health, Fitness and Dieting Author",
    "Humor and Entertainment Author",
    "Parenting and Relationships Author",
    "Self-Help Author",
    "Sports and Outdoors Author",
    "Travel Author"
]

# Add a dropdown list
selected_assistant = st.selectbox("Select the Assistant you want to use:", genres)

st.write(f"You selected: {selected_assistant}")

# Add a text input for Book Title
book_title = st.text_input("Enter the Book Title:")

# Display the Book Title and selected genre
if book_title:
    st.write(f"Book Title: {book_title}")

# Get list of Assistants from OpenAI API
assistants = api.list_assistants(st.secrets["openai_api_key"])
st.write(assistants)
