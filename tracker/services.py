import os
import google.generativeai as genai


def analyze_job_description(job_description):
    if not job_description or not job_description.strip():
        return "Please provide a valid job description for analysis."

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable is not set."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
        Analyze the following job description and provide:
        1. Key Requirements & Qualifications
        2. Top 5 Essential Technical & Soft Skills
        3. Match Advice / Resume Tailoring Tips

        Job Description:
        {job_description}
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI Analysis Failed: {str(e)}"