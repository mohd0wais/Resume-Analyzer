from flask import Flask, render_template, request, redirect, session
from db import engine, Base, SessionLocal
import models
import PyPDF2
import docx
# import json
from ai import analyze_resume

app = Flask(__name__)
app.secret_key = "secret123"

Base.metadata.create_all(bind=engine)


#----HOME
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")



#----SIGNUP
@app.route("/signup", methods= ["GET", "POST"])
def signup():
    db = SessionLocal()

    print("METHOD:", request.method)

    if request.method == "POST":
        print("FORM DATA:", request.form)
        username = request.form.get("username")   
        email = request.form.get("email")
        password =request.form.get("password")

        existing_user = db.query(models.user).filter_by(email=email).first()
        if existing_user:
            return "User already exists"

        user = models.user(
            username=username,  
            email=email,
            password=password
        )

        db.add(user)
        db.commit()


        print("USER SAVED ✅")
        return redirect("/login")
    return render_template("signup.html")





#----LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        print("EMAIL:", email)
        print("PASSWORD:", password)

        user = db.query(models.user).filter_by(email=email).first()
        print("USER:", user)

        if user and user.password == password:
            session["user_id"] = user.id   
            session["username"] = user.username
            session["email"] = user.email
            return redirect("/dashboard")

        return "Invalid credentials"

    return render_template("login.html")


#----DASHBAORD
@app.route("/dashboard", methods =["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    
    result = None

    if request.method == "POST":
        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")

        file = request.files.get("file")

        #file handling
        if file and file.filename != "":
            if file.filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                    resume_text = text
                except Exception as e:
                    result = f"PDF error: {str(e)}"
                    return render_template("dashboard.html", result=result, user=session.get("user"))
            
            elif file.filename.endswith(".docx"):
                try:
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text + "\n"
                    resume_text = text
                except Exception as e:
                    result = f"Docx error: {str(e)}"
                    return render_template("dashboard.html", result=result, user=session.get("user"))

        # Analyze resume using AI
        if resume_text and user_goal:
            result = analyze_resume(resume_text, user_goal)
        else:
            result = "Please provide both resume text/file and your target role."

    return render_template("dashboard.html", result=result, user=session.get("user"))


#----LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/test-db")
def test_db():
    conn = engine.connect()
    conn.close()
    return "DB Connected Successfully!"