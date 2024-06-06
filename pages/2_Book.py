# Book.py
import streamlit as st

st.title('Book Details')

st.write("Enter the details for your book:")

# Retrieve data from session state
selected_niche = st.session_state.get('selected_niche', 'Not selected')
profitable_keywords = st.session_state.get('profitable_keywords', [])

st.write(f"Most Profitable Niche: {selected_niche}")
st.write("Keyword Opportunities:")
if profitable_keywords:
    for keyword in profitable_keywords:
        st.write(f"- {keyword}")
else:
    st.write("No profitable keywords found.")

# Author characteristics
st.header("Author Characteristics")
author_gender = st.selectbox("Select the author's gender", ["Male", "Female", "Non-binary", "Prefer not to say"])
author_experience = st.selectbox("Select the author's experience level", ["Beginner", "Intermediate", "Expert"])
author_age_group = st.selectbox("Select the author's age group", ["18-25", "26-35", "36-45", "46-55", "56+"])

# Audience characteristics
st.header("Audience Characteristics")
audience_age_group = st.selectbox("Select the audience's age group", ["Children", "Teens", "Young Adults", "Adults", "Seniors"])
audience_interests = st.selectbox("Select the primary interest of the audience", ["Fiction", "Non-fiction", "Self-help", "Educational", "Fantasy", "Science Fiction", "Romance", "Mystery", "Biography"])
audience_gender = st.selectbox("Select the audience's gender", ["Male", "Female", "Non-binary", "All"])
audience_income = st.selectbox("Select the audience's income level", ["Low", "Medium", "High"])
audience_location = st.selectbox("Select the audience's location", ["Urban", "Suburban", "Rural", "Any"])
audience_education = st.selectbox("Select the audience's education level", ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "Doctorate"])

# Book details
st.header("Book Details")
genre = st.selectbox("Select the genre of the book", ["Fiction", "Non-fiction", "Fantasy", "Science Fiction", "Romance", "Mystery", "Biography", "Self-help", "Educational"])
book_format = st.selectbox("Select the format of the book", ["Hardcover", "Paperback", "E-book", "Audiobook"])
language = st.selectbox("Select the language of the book", ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Other"])
book_style = st.selectbox("Select the style of the book", ["Formal", "Informal", "Technical", "Conversational", "Narrative"])
book_tone = st.selectbox("Select the tone of the book", ["Serious", "Humorous", "Inspirational", "Neutral", "Cautionary"])
reading_level = st.selectbox("Select the reading level of the book", ["Beginner", "Intermediate", "Advanced"])

# Number of chapters
st.header("Structure")
num_chapters = st.slider("Select the number of chapters", 1, 50, 10)

# Additional features
st.header("Additional Features")
glossary = st.checkbox("Include a glossary")
index = st.checkbox("Include an index")
illustrations = st.checkbox("Include illustrations")
foreword = st.checkbox("Include a foreword")
appendix = st.checkbox("Include an appendix")

# Summary of selections
st.write("### Summary of Your Book Details")
summary_text = f"**Author's Gender:** {author_gender}\n"
summary_text += f"**Author's Experience Level:** {author_experience}\n"
summary_text += f"**Author's Age Group:** {author_age_group}\n"
summary_text += f"**Audience's Age Group:** {audience_age_group}\n"
summary_text += f"**Audience's Primary Interest:** {audience_interests}\n"
summary_text += f"**Audience's Gender:** {audience_gender}\n"
summary_text += f"**Audience's Income Level:** {audience_income}\n"
summary_text += f"**Audience's Location:** {audience_location}\n"
summary_text += f"**Audience's Education Level:** {audience_education}\n"
summary_text += f"**Genre:** {genre}\n"
summary_text += f"**Format:** {book_format}\n"
summary_text += f"**Language:** {language}\n"
summary_text += f"**Style:** {book_style}\n"
summary_text += f"**Tone:** {book_tone}\n"
summary_text += f"**Reading Level:** {reading_level}\n"
summary_text += f"**Number of Chapters:** {num_chapters}\n"

if glossary:
    summary_text += "**Includes:** Glossary\n"
if index:
    summary_text += "**Includes:** Index\n"
if illustrations:
    summary_text += "**Includes:** Illustrations\n"
if foreword:
    summary_text += "**Includes:** Foreword\n"
if appendix:
    summary_text += "**Includes:** Appendix\n"

summary_text += f"**Most Profitable Niche:** {selected_niche}\n"
summary_text += "Keyword Opportunities:\n"
if profitable_keywords:
    for keyword in profitable_keywords:
        summary_text += f"- {keyword}\n"
else:
    summary_text += "No profitable keywords found.\n"

# Additional comments or notes
st.header("Additional Comments or Notes")
additional_notes = st.text_area("Enter any additional comments or notes about the book")
if additional_notes:
    summary_text += f"**Additional Comments/Notes:**\n{additional_notes}\n"
    st.write("**Additional Comments/Notes:**")
    st.write(additional_notes)

st.write(summary_text)

# Button to download summary as a txt file
st.download_button(
    label="Download Book Details as TXT",
    data=summary_text,
    file_name=f"{selected_niche}_book_details.txt",
    mime='text/plain'
)
