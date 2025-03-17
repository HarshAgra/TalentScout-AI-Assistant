import streamlit as st
from utils import generate_technical_questions
import google.generativeai as genai

# Set Google Gemini API Key (replace with your actual API key)
genai.configure(api_key="AIzaSyCa63WCw9jnkCiDl59f-nVT0XKkLmEMqtc")

def main():
    # Set the title and description for the app
    st.title("TalentScout AI Hiring Assistant")
    st.write("""
    Welcome to the TalentScout Hiring Assistant! I will assist you in submitting your details and generating technical questions 
    based on your tech stack.
    """)

    # Information gathering
    with st.form(key='candidate_info'):
        st.subheader("Please provide your information:")

        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        years_of_experience = st.number_input("Years of Experience", min_value=0)
        desired_position = st.text_input("Desired Position(s)")
        current_location = st.text_input("Current Location")

        # Tech stack selection
        tech_stack = st.text_area("Tech Stack (Programming Languages, Frameworks, Tools etc.)", 
                                 placeholder="e.g., Python, Django, React, MySQL")

        submit_button = st.form_submit_button("Submit")

    # Proceed if user submits the form
    if submit_button:
        # Display candidate details (This could also be stored in a database)
        st.write(f"Thank you for providing your details, {full_name}!")
        st.write(f"Email: {email}")
        st.write(f"Phone: {phone}")
        st.write(f"Years of Experience: {years_of_experience}")
        st.write(f"Desired Position: {desired_position}")
        st.write(f"Location: {current_location}")
        st.write(f"Tech Stack: {tech_stack}")

        # Generate technical questions based on the tech stack
        if tech_stack:
            st.subheader("Technical Questions:")
            questions = generate_technical_questions(tech_stack)
            if questions:
                for idx, question in enumerate(questions, start=1):
                    st.write(f"{idx}. {question}")
            else:
                st.write("Sorry, I couldn't generate questions. Please try again later.")

        # End Conversation (Gracefully conclude the conversation)
        st.write("\nThank you for using TalentScout AI Assistant. We will be in touch soon!")
        st.stop()

if __name__ == "__main__":
    main()
