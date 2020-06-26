operation = input('''
Please choose 1 of the following
1 for About Me
2 for About Owner 
3 for owners github
4 for what programming language does he use
5 for exit
''')
import pyttsx3

def oper(About):
    if operation == '1':
        pyttsx3.speak("My, name is NZ, i was, created by my, lovely master, sojjyCodes")
        print("My, name is NZ, i was, created by my, lovely master, sojjyCodes")
oper("about")

def oper(Owner):
    if operation == '2':
        pyttsx3.speak("The name, of my creator is Ebenezer, he is 13 years old.")
        print("The name, of my creator is Ebenezer, he is 13 years old.")
oper("Owner")

def oper(hub):
    if operation == '3':
        pyttsx3.speak("sojjy's github is sojjyCodes")
        print("https://www.github.com/sojjyCodes/")
oper("hub")

def oper(lang):
    if operation == '4':
        pyttsx3.speak("His main programming language is python ")
    print("His main programming language is python ")
oper("lang")

if operation == '5':
    pyttsx3.speak("Thanks for visiting ")
    print("Thanks for visiting ")
    exit()
oper("Thanks")



