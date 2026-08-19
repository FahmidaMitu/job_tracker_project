import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_job_description(job_description):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Analyze the following job description and return ONLY a valid JSON object with these keys:
        "summary", "required_skills", "required_experience", "important_technologies", "interview_suggestions".
        
        Job Description:
        {job_description}
        """
        
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        return json.loads(response.text)
    except Exception as e:
        return {
            "error": "Failed to analyze job description using AI.",
            "details": str(e)
        }