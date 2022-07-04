# test = 5 Это переменные 

# int
#number = 5
#age = 21

# float 
#fnumber = 5.5

# str
#name = "Tamerlan"

# bool
#status = True

# Перевод строки - \n

#конкатенация
# print("hello "  + name)
# print ("Мне "+ str(age) + " года" + "!")

#input
#name = input ("Введите свой ник: ")
#pas = input ("Укажи гилдию: ")
#print("Добро пожаловать! " + name + " в гилдию "+ pas +"ов" "!")

# +, -, /, *, **, %, унарный минус, округление, ПИ. 

#унарный минус
#a = 10
#a = -a 
#print (a)

# округление 
#a = 10.67
#print(round(a))
#import math 
#print(math.floor(в меньшу)// math.ceil(В большу))

#ПИ
#import math
#print(math.pi)

#Калькулятор №1
from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

print( Fore.BLACK)
print(Back.GREEN)	

a = float(input(" "))

print(Back.CYAN)

what = input (" ")

print(Back.GREEN)

b = float(input(" "))

print(Back.RED	)

if what == "+":
	c = a + b
	print(" " + str(c))
elif what == "-":
	c = a - b
	print(" " + str(c))
elif what == "*" :
	c = a * b
	print(" " + str(c))
elif what == "/" :
	c = a / b
	print(" " + str(c))
elif what == "**" :
	c = a ** b
	print(" " + str(c))
elif what == "%" :
	c = a % b
	print(" " + str(c))
else:
	print("Error!")

input()

