#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QGroupBox, QButtonGroup
)
from random import shuffle

app = QApplication([])
RadioGroupBox = QGroupBox("Answer Options")
question = QLabel("Question")
rbtn_1 = QRadioButton("Option 1")
rbtn_2 = QRadioButton("Option 2")
rbtn_3 = QRadioButton("Option 3")
rbtn_4 = QRadioButton("Option 4")
rgroup = QButtonGroup()
rgroup.addButton(rbtn_1)
rgroup.addButton(rbtn_2)
rgroup.addButton(rbtn_3)
rgroup.addButton(rbtn_4)

ans_btn = QPushButton("Answer")
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
ansGroupBox = QGroupBox("Test Result")
result = QLabel("True/False")
correct = QLabel("Correct answer")

layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment = (Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(correct, alignment = Qt.AlignHCenter, stretch = 2)

ansGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()#Question
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment = Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(ansGroupBox)
layout_line3.addWidget(ans_btn, stretch = 2)

ansGroupBox.hide()

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.setSpacing(5)

def show_results():
    RadioGroupBox.hide()
    ansGroupBox.show()
    ans_btn.setText("Next Question")

def show_question():
    print("a")
    RadioGroupBox.show()
    ansGroupBox.hide()
    ans_btn.setText("Answer")
    rgroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    rgroup.setExclusive(True)

def start_test():
    if ans_btn.text() == "Answer":
        show_results()
    else:
        next_question()
    #    show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(Question, Correct, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(Correct)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    question.setText(Question)
    correct.setText(Correct)
    show_question()

def check_answer():
    if ans_btn.text() == "Answer":
        if answers[0].isChecked():
            show_correct("Correct")
        else:
            if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                show_correct("Incorrect")
    else:
        next_question()

def show_correct(res):
    result.setText(res)
    show_results()

questions = { 
        "q1" : ["The national language of Brazil", "Portugese", "Mandarin", "Italian", "Brazillian"],
        "q2" : ["When did World War 2 end?", "1945", "1806", "1920", "1860"],
        "q3" : ["What is the fourth planet in the solar system?", "Mars", "Earth", "Jupiter", "Mercury"],
        "q4" : ["Who is the president of the United States now?", "Joe Biden", "Barack Obama", "Donald Trump", "George W. Bush"],
        "q5" : ["What element does Au stand for?", "Gold", "Silver", "Copper", "Iron"]
    }


def next_question():
    global index
    if index >= 5:
        index = 0
    index += 1
    key = "q"+str(index)
    ask(questions[key][0], questions[key][1], questions[key][2], questions[key][3], questions[key][4])
    
index = 1
my_win = QWidget()

my_win.setLayout(layout_card)
my_win.setWindowTitle("Memory Card")
ask(questions["q1"][0], questions["q1"][1], questions["q1"][2], questions["q1"][3], questions["q1"][4])
ans_btn.clicked.connect(check_answer)



my_win.show()
app.exec()