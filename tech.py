from bs4 import BeautifulSoup
import requests

QNA_dic = {}

temp_question = []
HTML_CODE = requests.get('https://www.guru99.com/tcs-interview-questions.html').text
soup = BeautifulSoup(HTML_CODE, 'lxml')
questions = soup.find_all('p', class_ = 'faq-question')
for que in questions:
    q = que.find('strong').text
    temp_question.append(q)
QNA_dic["TCS"] = temp_question

temp_question = []
HTML_CODE = requests.get('https://www.wisdomjobs.com/e-university/wipro-technical-interview-questions.html').text
soup = BeautifulSoup(HTML_CODE, 'lxml')
questions = soup.find_all('li', class_ = 'quesans mb-20')
for que in questions:
    q = que.find('a',class_ = "accordion-trigger ques").text
    temp_question.append(q)
QNA_dic["WIPRO"] = temp_question

temp_question = []
HTML_CODE = requests.get('https://www.faceprep.in/tech-mahindra/tech-mahindra-interview-question/').text
soup = BeautifulSoup(HTML_CODE, 'lxml')
questions = soup.find_all('li', class_ = 'ql-indent-1')
for que in questions:
    q = que.text
    temp_question.append(q)
QNA_dic["TECH MAHINDRA"] = temp_question

temp_question = []
HTML_CODE = requests.get('https://www.faceprep.in/infosys/infosys-interview-questions-experiences/').text
soup = BeautifulSoup(HTML_CODE, 'lxml')
questions = soup.find('ul')
for que in questions:
    q = que.text
    temp_question.append(q)  
QNA_dic["INFOSYS"] = temp_question

temp_question = []
HTML_CODE = requests.get('https://www.javatpoint.com/ibm-interview-questions').text
soup = BeautifulSoup(HTML_CODE, 'lxml')
questions = soup.find('ol', class_ = "points")
for que in questions:
    if(que == '\n'):
        continue
    q = que.text
    temp_question.append(q)  
QNA_dic["IBM"] = temp_question

print(QNA_dic)