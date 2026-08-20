import os
from dotenv import load_dotenv
from google import genai
from django.conf import settings

load_dotenv()

def analyze_job_description(job_description):
    if not job_description:
        return "Job description is empty. Please provide details to analyze."

    try:
        api_key = os.getenv('GEMINI_API_KEY') or getattr(settings, 'GEMINI_API_KEY', None)
        
        if not api_key:
            return "AI Analysis Failed: GEMINI_API_KEY is missing in .env file."

        client = genai.Client(api_key=api_key)

        prompt = f"""
        You are an AI career advisor. Analyze the following job description.

        CRITICAL FORMATTING RULES:
        1. Every heading MUST be on its own line.
        2. The summary content MUST start on a NEW line below the "### 1. Summary" heading.
        3. Insert TWO blank lines between sections.
        4. Every section (1, 2, 3, 4) MUST be separated into distinct paragraphs.

        Follow this EXACT structure:

        ### 1. Summary
        [Write the summary text here on a new line]


        ### 2. Required Key Skills
        * [Skill 1]
        * [Skill 2]


        ### 3. Important Technologies / Tools
        * [Tool 1]
        * [Tool 2]


        ### 4. Interview Preparation Suggestions
        * [Tip 1]
        * [Tip 2]


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