# AI Job Application Tracker 🚀 & Complete Documentation

An AI-powered Django web application designed to help job seekers track their job applications and automatically analyze job descriptions using Google's Gemini AI.

---

## 🌟 Key Features

* **Job Application Management:** Add, edit, view, and track job applications and status.
* **AI Job Analysis:** Get automated summaries, key required skills, tools, and custom interview preparation advice from job descriptions using Gemini AI.
* **Secure Setup:** Keeps private API credentials safe using environment variable files (`.env`).

---

## 📽️ Project Demo & Video Walkthrough

* **Drive Video Link:** [Click here to watch the demo video](https://drive.google.com/your-drive-video-link-here)

---

## 🛠️ Requirements & Prerequisites

* **Python:** Version 3.10 or higher
* **Git:** Installed on local machine
* **Gemini API Key:** Free key obtained from [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 🚀 Complete Setup & Installation Guide

### Local Server URL
Once running, open your browser and visit:  
**`http://127.0.0.1:8000/`**

### Terminal Commands:

```bash
# 1. Clone the Repository
git clone [https://github.com/FahmidaMitu/job_tracker_project.git](https://github.com/FahmidaMitu/job_tracker_project.git)
cd job_tracker_project

# 2. Create Virtual Environment
python -m venv venv

# 3. Activate Virtual Environment
# Windows:
venv\Scripts\activate
# Mac / Linux:
# source venv/bin/activate

# 4. Install Project Dependencies
pip install -r requirements.txt

# 5. Apply Database Migrations
python manage.py migrate

# 6. Run the Development Server
python manage.py runserver