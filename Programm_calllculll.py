from PySide2 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyCalc import Ui_Form
import sys
import math


app = QtWidgets.QApplication(sys.argv)


Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

symbol = ''
view_numbers = ''
num_1 = ''
num_2 = ''

"""Функционал цифр от 0 до 9"""

def button_0():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '0'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '0'
ui.pushButton_0.clicked.connect(button_0)

def button_1():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '1'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '1'
ui.pushButton_1.clicked.connect(button_1)

def button_2():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '2'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '2'
ui.pushButton_2.clicked.connect(button_2)

def button_3():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '3'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '3'
ui.pushButton_3.clicked.connect(button_3)

def button_4():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '4'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '4'
ui.pushButton_4.clicked.connect(button_4)

def button_5():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '5'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '5'
ui.pushButton_5.clicked.connect(button_5)

def button_6():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '6'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '6'
ui.pushButton_6.clicked.connect(button_6)

def button_7():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '7'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '7'
ui.pushButton_7.clicked.connect(button_7)

def button_8():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '8'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '8'
ui.pushButton_8.clicked.connect(button_8)

def button_9():
	global view_numbers
	global num_1
	view_numbers = view_numbers + '9'
	ui.lineEdit.setText(view_numbers) #выводим текст
	num_1 = num_1 + '9'
ui.pushButton_9.clicked.connect(button_9)

"""Функционал удаления цифры, del, процента и факториала"""

def backSpace():
	global view_numbers
	global num_1
	view_numbers = view_numbers[0 : -1]
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1[0 : -1]
ui.pushButton_clean.clicked.connect(backSpace)

def delete():
	global view_numbers
	global num_1
	global num_2
	global symbol
	view_numbers = ''
	num_1 = ''
	num_2 = ''
	symbol = ''
	ui.lineEdit.setText(view_numbers)
ui.pushButton_del.clicked.connect(delete)

def procent():
	global view_numbers
	global num_1
	global num_2
	if '+' in view_numbers or '-' in view_numbers or 'x' in view_numbers or '/' in view_numbers or '%' in view_numbers:
		pass
	else:
		num_1 = float(num_1)
		num_1 = num_1 * 0.01
		num_1 = str(num_1)
		view_numbers = num_1
		ui.lineEdit.setText(view_numbers)
ui.pushButton_procent.clicked.connect(procent)

def factorial():
	global view_numbers
	global num_1
	global num_2
	if float(view_numbers) <= 0:
		ui.lineEdit.setText('Number <= 0')
	else:
		if '+' in view_numbers or '-' in view_numbers or 'x' in view_numbers or '/' in view_numbers or '%' in view_numbers:
			pass
		else:
			try:
				num_1 = int(num_1)
				fact = 1
				for i in range(1, num_1 + 1):
					fact = fact * i
				num_1 = str(fact)
				view_numbers = num_1
				ui.lineEdit.setText(view_numbers)
			except:
				num_1 = num_1[: -2]
				num_1 = int(num_1)
				fact = 1
				for i in range(1, num_1 + 1):
					fact = fact * i
				num_1 = str(fact)
				view_numbers = num_1
				ui.lineEdit.setText(view_numbers)
ui.pushButton_factorial.clicked.connect(factorial)

def point():
	global view_numbers
	global num_1
	if '.' in num_1:
		pass
	else:
		num_1 = num_1 + '.'
		view_numbers = view_numbers + '.'
		ui.lineEdit.setText(view_numbers)
ui.pushButton_tochka.clicked.connect(point)

"""Функционал логических истин и равенства"""
def split():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if '+' in view_numbers or '-' in view_numbers or 'x' in view_numbers or '/' in view_numbers or '%' in view_numbers:
		pass
	else:
		view_numbers = view_numbers + '/'
		ui.lineEdit.setText(view_numbers)
		symbol = 'diveder'
		num_2 = num_1
		num_1 = ''
ui.pushButton_split.clicked.connect(split)

def plus():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if '+' in view_numbers or '-' in view_numbers or 'x' in view_numbers or '/' in view_numbers or '%' in view_numbers:
		pass
	else:
		view_numbers = view_numbers + '+'
		ui.lineEdit.setText(view_numbers)
		symbol = 'plus'
		num_2 = num_1
		num_1 = ''
ui.pushButton_plus.clicked.connect(plus)

def mult():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if '+' in view_numbers or '-' in view_numbers or 'x' in view_numbers or '/' in view_numbers or '%' in view_numbers:
		pass
	else:
		view_numbers = view_numbers + 'x'
		ui.lineEdit.setText(view_numbers)
		symbol = 'mult'
		num_2 = num_1
		num_1 = ''
ui.pushButton_multiplication.clicked.connect(mult)

def min():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if '+' in view_numbers or '-' in view_numbers or 'x' in view_numbers or '/' in view_numbers or '%' in view_numbers:
		pass
	else:
		view_numbers = view_numbers + '-'
		ui.lineEdit.setText(view_numbers)
		symbol = 'minus'
		num_2 = num_1
		num_1 = ''
ui.pushButton_min.clicked.connect(min)

def equally():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if symbol == 'plus':
		num_1 = float(num_1)
		num_2 = float(num_2)
		answer = num_2 + num_1
		num_1 = answer
		answer = str(answer)
		ui.lineEdit.setText(answer)
		num_1 = str(num_1)
		num_2 = str(num_2)
		view_numbers = num_1
		answer = ''
	elif symbol == 'minus':
		num_1 = float(num_1)
		num_2 = float(num_2)
		answer = num_2 - num_1
		answer = str(answer)
		ui.lineEdit.setText(answer)
		num_1 = num_2 - num_1
		num_1 = str(num_1)
		num_2 = str(num_2)
		view_numbers = num_1
	elif symbol == 'diveder':
		num_1 = float(num_1)
		num_2 = float(num_2)
		answer = num_2 / num_1
		answer = str(answer)
		ui.lineEdit.setText(answer)
		num_1 = str(num_1)
		num_2 = str(num_2)
		view_numbers = num_1
	elif symbol == 'mult':
		num_1 = float(num_1)
		num_2 = float(num_2)
		answer = num_2 * num_1
		answer = str(answer)
		ui.lineEdit.setText(answer)
		num_1 = str(num_1)
		num_2 = str(num_2)
		view_numbers = num_1
	else:
		ui.lineEdit.setText('EROR')
ui.pushButton_end_data.clicked.connect(equally)


sys.exit(app.exec_())