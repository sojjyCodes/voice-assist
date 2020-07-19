import pyttsx3
engine = pyttsx3.init()

operation = input('''
Please choose 1 of the following
1 for About assistant
2 for About Owner 
3 for my GitHub username
4 for what programming language does he use
5 for open Chrome 
6 for open Firefox
7 for exit
8 to fully shutdown system
''')

from selenium import webdriver
driver = webdriver.Chrome()
driver2 = webdriver.Firefox()


def about_assistant():
    pyttsx3.speak("My name, is NZ. And i was created by my lovely master sojjyCodes")
    print("My name, is, NZ. And i, was created by, my master, sojjyCodes.")


def about_master():
    pyttsx3.speak("The name, of my creator, is, sojjyCodes ")
    print("The name of my creator is, sojjyCodes ")


def github_username():
    pyttsx3.speak("My master github is sojjyCodes")
    print("https://github.com/sojjyCodes")


def my_programming_language():
    pyttsx3.speak("My master, uses the python, programming language. ")
    print("Python")


def openChrome():
    driver.get('https://github.com/sojjyCodes')
    pyttsx3.speak('Opening, Chrome')
    print('Opening Chrome')

def openFirefox():
    driver2.get('https://github.com/sojjyCodes')
    pyttsx3.speak('Opening, Firefox')
    print('Opening Firefox')


def exit():
    pyttsx3.speak('Exiting, Program')
    print("Exiting Program")
    exit()


def remotely_shutdown_system():
    pyttsx3.speak("Shutting, down")
    os.system("poweroff")


def process_operation_gotten_from_user(operation_from_user):
    if operation_from_user == '1':
        about_assistant()
    if operation_from_user == '2':
        about_master()
    if operation_from_user == '3':
        github_username()
    if operation_from_user == '4':
        my_programming_language()
    if operation_from_user == '5':
        openChrome()
    if operaton_from_user == '6':
        openFirefox()
    if operation_from_user == '7':
	    quit()
    if operation_from_user == '8':
        remotely_shutdown_system()


process_operation_gotten_from_user(operation)
