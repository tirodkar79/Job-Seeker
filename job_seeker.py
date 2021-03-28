from flask import Flask, render_template, request, Markup, redirect, url_for, flash, jsonify
import os
from login import Login
from form import Registration
from essay import Essays
import pyrebase
import random
from gingerit.gingerit import GingerIt
from bs4 import BeautifulSoup
import requests
import lxml


app = Flask(__name__)
student_key = ""

firebaseConfig = {'apiKey': "AIzaSyCERHUd4d7N2UO1KoiUjoceblNKuReZTIo",
    'authDomain': "job-seeker-e8f24.firebaseapp.com",
    'databaseURL': "https://job-seeker-e8f24-default-rtdb.firebaseio.com",
    'projectId': "job-seeker-e8f24",
    'storageBucket': "job-seeker-e8f24.appspot.com",
    'messagingSenderId': "896898472873",
    'appId': "1:896898472873:web:078edb56f55f4a846b02b8",
    'measurementId': "G-7V3Z2BJ4V5"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
app.config['SECRET_KEY'] = 'ffc4ffcad104551e6207436770e3b325'
questions = [
    [1, "How many liters of a 90% solution of concentrated acid needs to be mixed with a 75% solution of concentrated acid to get a 30 liter solution of 78% concentrated acid?", 6, 7, 5, 8, 6],
    [2, "A mother her little daughter and her just born infant boy together stood on a weighing machine which shows 74kgs.how much does the daughter weigh if the mother weighs 46kg more than the combined weight of daughter and the infant and the infant weighs 60% less than the daughter?", 11, 12, 10, 14, 10],
    [3, "In paper A, one student got 18 out of 70 and in paper B he got 14 out of 30. In which paper he did fare well?", 'Paper A', 'Paper B', 'None', 'Both', 'Paper B'],
    [4, "The cost of Type 1 rice is Rs. 15 per kg and Type 2 rice is Rs.20 per kg. If both Type 1 and Type 2 are mixed in the ratio of 2 : 3, then the price per kg of the mixed variety of rice is", 17, 18, 16, 19, 18],
    [5, "From a container, 6 liters milk was drawn out and was replaced by water. Again 6 liters of mixture was drawn out and was replaced by the water. Thus the quantity of milk and water in the container after these two operations is 9:16. The quantity of mixture is:", 15, 16, 17, 18, 15],
    [6, "The shopkeeper charged 12 rupees for a bunch of chocolate. but I bargained to the shopkeeper and got two extra ones, and that made them cost one rupee for dozen less then first asking price .how many chocolates I received in 12 rupees ?", 16,14, 13, 12, 16],
    [7, "The marked price of coat was 40%less than the suggested retail price. Eesha purchased the coat for half of the marked price at the 15th anniversary sale. What percent less than the suggested retail price did eesha pay?", 70, 80, 55, 44, 70],
    [8, "The value of a scooter depreciates in such a way that at the end of each year, is ¾ of its value at the beginning of same year. If the initial value of the scooter is rs40,000. What is the value at the end of 3yrs?", 16874, 17867, 16873, 17866, 16873]
]

@app.route("/ReadinessTest")
def readiness_questions():
    
    return render_template("Readiness_Template.html", questions = questions)


def interview_questions(company_name):
    temp_question = []
    if company_name == "TCS":
        HTML_CODE = requests.get('https://www.guru99.com/tcs-interview-questions.html').text
        soup = BeautifulSoup(HTML_CODE, 'lxml')
        questions = soup.find_all('p', class_ = 'faq-question')
        for que in questions:
            q = que.find('strong').text
            temp_question.append(q)

    elif company_name == "Wipro":
        HTML_CODE = requests.get('https://www.wisdomjobs.com/e-university/wipro-technical-interview-questions.html').text
        soup = BeautifulSoup(HTML_CODE, 'lxml')
        questions = soup.find_all('li', class_ = 'quesans mb-20')
        for que in questions:
            q = que.find('a',class_ = "accordion-trigger ques").text
            temp_question.append(q)

    elif company_name == "LTI":
        HTML_CODE = requests.get('https://www.javatpoint.com/ibm-interview-questions').text
        soup = BeautifulSoup(HTML_CODE, 'lxml')
        questions = soup.find('ol', class_ = "points")
        for que in questions:
            if(que == '\n'):
                continue
            q = que.text
            temp_question.append(q) 
    elif company_name == "Capgemini":
        HTML_CODE = requests.get('https://www.faceprep.in/tech-mahindra/tech-mahindra-interview-question/').text
        soup = BeautifulSoup(HTML_CODE, 'lxml')
        questions = soup.find_all('li', class_ = 'ql-indent-1')
        for que in questions:
            q = que.text
            temp_question.append(q)

    else:
        HTML_CODE = requests.get('https://www.faceprep.in/infosys/infosys-interview-questions-experiences/').text
        soup = BeautifulSoup(HTML_CODE, 'lxml')
        questions = soup.find('ul')
        for que in questions:
            q = que.text
            temp_question.append(q)  

    return temp_question

def job_fetch():


@app.route("/Essay", methods=["GET", "POST"])
def essay_corrector():
    
    accuracy = ""
    answer = False
    essays = Essays()
    if request.method == 'POST':
        if essays.validate_on_submit():
            mistakes = 0
            total_length = 0

    
            essay_text = essays.essays.data
            text = list(map(str, essay_text.split()))
            parser = GingerIt()
            for i in text:
                if len(parser.parse(i)['corrections']) > 0:
                    mistakes += 1
                total_length += 1
            accuracy = "Your accuracy is " + str(round((mistakes/total_length)*100)) + "%"
            answer = True
            return render_template("Essay.html", essays = essays, accuracy = accuracy, answer = answer)
    return render_template("Essay.html", essays = essays, accuracy = accuracy, answer = answer)

@app.route("/TCS")
def TCS_fetch():
    interview_question = interview_questions("TCS") 
    return render_template("tcs.html", interview_question = interview_question)

@app.route("/LTI")
def LTI_fetch():
    interview_question = interview_questions("LTI") 
    return render_template("lti.html", interview_question = interview_question)

@app.route("/Capgemini")
def Capgemini_fetch():
    interview_question = interview_questions("Capgemini") 
    return render_template("capgemini.html", interview_question = interview_question)

@app.route("/Infosys")
def Infosys_fetch():
    interview_question = interview_questions("Infosys") 
    return render_template("infosys.html", interview_question = interview_question)

@app.route("/Wipro")
def Wipro_fetch():
    interview_question = interview_questions("Wipro") 
    return render_template("wipro.html", interview_question = interview_question)


@app.route("/Companies")
def company_fetch():
    return render_template("company.html")

@app.route("/Hirings")
def job_hirings():
    pass

@app.route("/Feedback")
def feedback_form():
    return render_template("feedback.html")

@app.route("/Contact")
def contact_form():
    return render_template("contact.html")


@app.route("/Resume")
def resume_builder():

    global student_key
    student_details = dict()
    details = db.child("Students").child(student_key).get()

    student_details['Name'] = details.val()['fname'] + " " + details.val()['lname']
    
    student_details['Email'] = details.val()['email']

    student_details['Phone'] = details.val()['phone_no']

    student_details['Objective'] = details.val()['objective']
    
    skills = details.val()['skills'].replace("\r\n", " ")
    skills = list(map(str, skills.split()))
    final_skills = []
    for i in skills:
        val = random.randrange(65, 98)
        final_skills.append([i, val])
    
    print(final_skills)
    student_details['UG_Name'] = details.val()['college_name']
    student_details['UG_Percent'] = details.val()['college_cgpa']

    student_details['HSC_Name'] = details.val()['hsc_name']
    student_details['HSC_Percent'] = details.val()['hsc_percent']

    student_details['Project_Name'] = details.val()['project_name']
    student_details['Project_Descp'] = details.val()['project_desc']

    return render_template("Resume2.html", student_details = student_details, skills = final_skills)

@app.route("/Profile", methods=["GET", "POST"])
def profile():

    global student_key
    student_details = dict()
    print("Hello")
    print(student_key)
    details = db.child("Students").child(student_key).get()
    print(details.val()['fname'])
    student_details['Name'] = details.val()['fname'] + " " + details.val()['lname']
    
    student_details['Phone'] = details.val()['phone_no']
    
    skills = details.val()['skills'].replace("\r\n", " ")
    skills = list(map(str, skills.split()))
    final_skills = []
    for i in skills:
        val = random.randrange(65, 98)
        final_skills.append([i, val])
    
    print(final_skills)
    student_details['UG_Name'] = details.val()['college_name']
    student_details['UG_Percent'] = details.val()['college_cgpa']

    student_details['HSC_Name'] = details.val()['hsc_name']
    student_details['HSC_Percent'] = details.val()['hsc_percent']

    student_details['Project_Name'] = details.val()['project_name']
    student_details['Project_Descp'] = details.val()['project_desc']

    return render_template("profile.html", template_folder='templates', static_folder='static', student_details = student_details, skills = final_skills)

@app.route("/company", methods=["GET", "POST"])
def company_cards():
    return render_template("company.html", template_folder='templates', static_folder='static')

@app.route("/Student_Reg", methods=["GET", "POST"])
def reg():
    form = Registration()
    if request.method == 'POST':

        if form.validate_on_submit():
            data = {
                "fname" : form.fname.data,
                "lname" : form.lname.data,
                "email" : form.email.data,
                "phone_no" : form.phone_no.data,
                "objective" : form.objective.data,
                "hsc_name" : form.hsc_name.data,
                "hsc_percent" : form.hsc_percent.data,
                "college_name" : form.college_name.data,
                "college_cgpa" : form.college_cgpa.data,
                "year" : form.year.data,
                "project_name" : form.project_name.data,
                "project_desc" : form.project_desc.data,
                "skills" : form.skills.data,
                "password" : form.password.data
            }

            db.child("Students").push(data)

            return redirect(url_for('login'))
    return render_template("registration.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    global student_key
    login = Login()
    if request.method == 'POST':
        if login.validate_on_submit():
            students = db.child("Students").get()
            
            for i in students.each():
                    if(i.val()['email'] == login.username.data):

                        # If grp_id matches checks for password
                        if(i.val()['password'] == login.password.data):
                            student_key = i.key()
                            # If both matches then appends the grp_id in temporary lists
                            return redirect(url_for('profile'))
                # If credentials are wrong
            flash('INVALID CREDENTIALS')

    return render_template('login_page.html', template_folder='templates', static_folder='static', login=login)

@app.route("/")
def homepage():
    return render_template('index.html', template_folder='templates', static_folder='static')

if __name__ == "__main__":

    app.run(debug=True)

