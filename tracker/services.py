from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def analyze_job_description(job_description):
    if not job_description:
        return "Job description is empty. Please provide details to analyze."

    try:
        prompt = f"""
        Analyze the following job description and provide structured insights:
        1. Summary
        2. Required Key Skills
        3. Important Technologies/Tools
        4. Interview Preparation Suggestions

        Job Description:
        {job_description}
        """

        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
        )
        return response.text

    except Exception as e:
        return f"AI Analysis Failed: {str(e)}"