# AI Job Application Tracker 🚀 & Complete Documentation

An AI-powered Django web application designed to help job seekers track their job applications and automatically analyze job descriptions using AI.

---

## 🌟 Key Features

* **User Authentication:** Allow users to securely register, log in, and log out.
* **Job Application Management:** Add, edit, view, and track job applications and status.
* **AI Job Analysis:** Get automated summaries, key required skills, tools, and custom interview preparation advice from job descriptions using AI.
* **Search and Filtering:** Effortlessly search and filter job applications by title, company, or status.
* **Interview Management:** Schedule, organize, and keep track of upcoming interview dates, notes, and preparation steps for each job application.
* **Interactive Dashboard:** View real-time visual insights, summary metrics, total applications, and interview statuses at a glance.

---

## 📽️ Project Demo Video 

* **Drive Video Link:** [Click here to watch the demo video](https://drive.google.com/file/d/1K2ibXDCpgrvka7QL_coinWogUfD6p6Hv/view?usp=sharing)

---

## 📸 Screenshots & Visual Overview

* **Drive Screenshots Link:** [Click here to see the screenshots](https://drive.google.com/drive/folders/1590X-zBjZsdetxpjfJehIntIRgcRyyI4?usp=sharing)


---

## 🛠️ Requirements & Prerequisites

* **Python:** Version 3.10 or higher
* **Git:** Installed on local machine
* **API Key:** Free key obtained from [Google AI Studio](https://aistudio.google.com/app/apikey)

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