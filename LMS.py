import loginModule
import dataModule

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#bring back data from previous session
tableTimings = dataModule.ret_tableTimings()
types = dataModule.ret_types()
passwords = loginModule.ret_loadPasswords()  #stores passwords, startup loads passwords from prev session
#documented in module
studentNotes = dataModule.ret_studentNotes()
teacherNotes = dataModule.ret_teacherNotes()
teacherQuickNotes = dataModule.ret_teacherQuickNotes()

studentTime = dataModule.ret_studentTimeTable()
teacherTime = dataModule.ret_teacherTimeTable()

studentTasks = dataModule.ret_studentTasks()
teacherTasks = dataModule.ret_teacherTasks()

requests = dataModule.ret_requests()

studentClasses = dataModule.ret_studentClasses()
teacherClasses = dataModule.ret_teacherClasses()

studentMarks = dataModule.ret_studentMarks()
teacherMarks = dataModule.ret_teacherMarks()

def loginRegistration():
    print("Enter your username or enter 'register' to register a new account\n")
    name = input()
    if name in passwords:
        login(name)
    elif name == "registration\n":
        registration()
    else:
        print(name, "is not a registered account\n")

def login(username):
    print("Enter password for " +  username+ "\n")
    password = input()
    if password == passwords[username]:
        if types[username] == "teacher":
            teacher()
        else:
            student()


def registration():
    print("Enter the username you would like\n")
    username = input()
    if username in passwords.keys():
        print("Username is already taken")
        registration()
    print("Enter the password you would like\n")
    password = input()
    passwords[username] = password
    print("Are you a teacher (enter 't') or a student (enter 's')\n")
    c = 0
    while c < 1:
        sort = input().lower()
        if sort == "t":
            c = 5
            teacherRegistration(username)
        elif sort == "s":
            c = 5
            studentRegistration(username)
        else:
            print("Please enter either 't' or 's'\n")

def teacherRegistration(username):
    if tableTimings == {}:
        print("The school has not set up the time table system used. We will need you to help us set it up.\n")
        tableTimingsSetup()
    types[username] = "t"
    teacherNotes[username] = {}
    teacherQuickNotes[username] = []
    teacherTime[username] = {}
    teacherTasks[username] = {}
    teacherMarks[username] = {}
    print("Enter what subject you teach\n")
    subject = input()

    pass

def studentRegistration(username):
    studentNotes[username] = []
    studentTasks[username] = {}
    studentClasses[username] = []

    pass

def tableTimingsSetup():
    print("How many periods (including breaks) does the school have each day?\n")
    periods = int(input())
    for j in range(periods - 1):
        print("Enter start time for period " + str(j+1) + " (recommended to use (hh:mm) format)\n")
        start = input()
        print("Enter end time for period " + str(j+1) + " (recommended to use (hh:mm) format)\n")
        end = input()
        for i in days:
            tableTimings[i][j] = start + "-" + end
    return None

def student():
    pass

def teacher():
    pass


loginRegistration()







