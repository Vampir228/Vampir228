from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QHBoxLayout,
                 QVBoxLayout,
         QGroupBox,QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle
app = QApplication([])
window = QWidget()

lb_Question = QLabel('В каком году основали Москву')
btn_OK = QPushButton('Ответить')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
AnsGroupBox = QGroupBox('Результат теста')
right_answer = QLabel("прав ты или нет?")
lb_Corrent = QLabel("Ответ будет тут")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Corrent, alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def next_question():
        cur_question = randint(0,len(question_list) - 1) 
        window.cur_question += 1
        if window.cur_question >= len(question_list):
                window.cur_question = 0
        q = question_list[window.cur_question]
        ask(q)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 

layout_line1.addWidget(lb_Question)
layout_line3.addWidget(btn_OK)

layout_line2.addWidget(RadioGroupBox)
layout_main = QVBoxLayout()
layout_main.addLayout(layout_line1)
layout_main.addLayout(layout_line2)
layout_main.addLayout(layout_line3)
window.setLayout(layout_main)


def show_result():
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Следуший вопрос')
btn_OK.clicked.connect(show_result)
def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Ответить')
        RadioGroupBox.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroupBox.setExclusive(True)
class Question():
        def __init__(self,question,right,wrong1,wrong2,wrong3):
                self.question = question 
                self.right = right
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3
q = Question('На какой планете мы живём',"Земля","Марс","Юпитер","Уран")
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q):
        shuffle(answers)
        answers[0].setText(q.right)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_Question.setText(q.question)
        show_question()
def show_correct(res):
                show_correct.setText(res)
                show_result()
def check_answer():
                if answer[0].isChecked():
                        show_correct('Правильно')
                else:
                        if answer[1] or answer[2].isChecked() or answer[3].isChecked():
                                show_correct('Неправильно')

def click_OK():
        print('- Статистика')
        print('')
question_list = []
question_list.append(q)
ask(question_list[0])
btn_OK.clicked.connect(check_answer)




window.show()
app.exec_()
