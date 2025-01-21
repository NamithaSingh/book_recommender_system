import streamlit as st
import numpy as np
import pandas as pd

# Page title and description
st.set_page_config(page_title="Book Recommendation App", page_icon="📚", layout="wide")
st.title("📚 Book Recommendation App")
st.markdown(
    """
    Welcome to the **Book Recommendation App**!  
    Enter the title of a book, and we'll provide you with a list of similar books you might enjoy.  
    """
)

# Create a layout with two columns
col1, col2 = st.columns([2, 1])

with col1:
    # Input for the book name
    book_name = st.text_input("🔍 Enter a Book Title", placeholder="Type the title of your favorite book here...")

with col2:
    # Button to generate recommendations
    if st.button("✨ Recommend"):
        if book_name.strip():  # Ensure the input is not empty
            # Mock recommendation logic (replace with actual logic)
            def recommend_books(book_title):
                return [
                    f"📖 {book_title} - Similar Book 1",
                    f"📖 {book_title} - Similar Book 2",
                    f"📖 {book_title} - Similar Book 3"
                ]

            recommendations = recommend_books(book_name)

            # Display recommendations with a header
            st.markdown("### 🛒 Recommendations:")
            for book in recommendations:
                st.markdown(f"- {book}")
        else:
            st.warning("⚠️ Please enter a book title!")
