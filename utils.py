import google.generativeai as genai

genai.configure(api_key="AIzaSyCa63WCw9jnkCiDl59f-nVT0XKkLmEMqtc")

def generate_technical_questions(tech_stack):
    """
    Generates technical questions using the Gemini API based on the provided tech stack.
    """
    tech_stack = tech_stack.strip().lower()

    prompt = f"Generate 3-5 technical interview questions for a candidate proficient in {tech_stack}. " \
             "Ensure the questions are relevant and test different levels of proficiency (basic to advanced)."

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)

        if hasattr(response, 'text'):
            questions = response.text.strip().split("\n")
            return [q.strip() for q in questions if q.strip()]
        else:
            return ["Error: Unexpected response format from Gemini API."]

    except Exception as e:
        return [f"Error generating technical questions: {e}"]
