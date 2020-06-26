import pyttsx3
engine = pyttsx3.init()

operation = input('''
Please choose 1 of the following
1 for About assistant
2 for About Owner 
3 for my GitHub username
4 for what programming language does he use
5 for exit
''')


def about_assistant():
    pyttsx3.speak("My name, is NZ. And i was created by my lovely master sojjyCodes")
    print("My name, is, NZ. And i, was created by, my master, sojjyCodes.")


def about_master():
    pyttsx3.speak("The name, of my creator, is, sojjyCodes ")
    print("The name of my creator is, sojjyCodes ")


def github_username():
    pyttsx3.speak("The username, is, sojjyCodes")
    print("https://github.com/sojjyCodes")


def my_programming_language():
    pyttsx3.speak("My master, uses the python, programming language. ")
    print("Python")


def process_operation_gotten_from_user(operation_from_user):
    if operation_from_user == '1':
        about_assistant()
    if operation_from_user == '2':
        about_master()
    if operation_from_user == '3':
        github_username()
    if operation_from_user == '4':
        my_programming_language()
    else:
        exit(1)


process_operation_gotten_from_user(operation)
