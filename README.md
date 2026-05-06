
# AI-Carrer-Copilot (Flask + Ollama)

An AI-powered Resume Analyzer web application that analyzes resumes and provides structured feedback based on a target job role.
This project is built using Flask for backend and integrates AI using Ollama (LLaMA model) to generate smart suggestions.

⸻

✨ Features

* 🔐 User Authentication (Signup / Login)
* 📄 Upload Resume (PDF / DOCX)
* 🤖 AI-based Resume Analysis
* 🎯 Role-based feedback (user input job role)
* 📊 Structured Output:
    * Missing Skills
    * Skills to Remove
    * Recommended Projects
    * Learning Roadmap
* 🕘 Resume History Tracking
* 💻 Clean Dashboard UI

⸻

🧠 AI Integration

* Uses Ollama to run LLM locally
* LLaMA model for generating resume feedback
* Custom prompt to generate structured HTML output

⸻

🛠️ Tech Stack

* Frontend: HTML, CSS
* Backend: Python (Flask)
* Database: SQLAlchemy
* Resume Parsing:
    * PyPDF2 (PDF)
    * python-docx (DOCX)
* AI: Ollama (LLaMA)

⸻

📂 Project Structure

Resume-Analyzer/
│
├── app.py
├── db.py
├── models.py
├── ai.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── history.html
│
├── static/
│   └── style.css
│
└── venv/   (do not upload to GitHub)

⸻

⚙️ How It Works

1. User signs up / logs in
2. Uploads resume (PDF or DOCX)
3. Resume text is extracted
4. User enters target job role
5. AI analyzes resume using Ollama
6. Structured feedback is generated
7. Results displayed on dashboard

⸻

🚀 Installation & Setup

### Create virtual environment
python -m venv venv
### Activate environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
### Install dependencies
pip install flask sqlalchemy PyPDF2 python-docx ollama
### Run application
python app.py

⸻

⚠️ Important

Make sure Ollama is installed and running locally.

Run LLaMA model before starting app:

ollama run llama3

⸻

📸 Demo

* Login Page
<img width="1470" height="956" alt="Screenshot 2026-05-04 at 10 17 50 PM" src="https://github.com/user-attachments/assets/b43e0760-f2f5-4ce1-bc97-0c41f206549e" />

* Dashboard
<img width="1470" height="956" alt="Screenshot 2026-05-04 at 10 18 09 PM" src="https://github.com/user-attachments/assets/e74f873e-3ab7-4471-b520-c55dd9bf8440" />

* AI Result Output
<img width="1470" height="956" alt="Screenshot 2026-05-04 at 10 19 01 PM" src="https://github.com/user-attachments/assets/690b80fa-bd41-4b32-8ca0-f8842b8d0652" />

⸻

🎯 Learning Outcomes

* Built full-stack web application using Flask
* Integrated AI (LLM) into real-world project
* Implemented authentication system
* Learned resume parsing (PDF & DOCX)
* Used prompt engineering for structured results

⸻

🚧 Future Improvements

* Resume scoring system
* Cloud deployment
* Downloadable report
* Better AI accuracy

⸻

⭐ Support

If you like this project, give it a star ⭐
