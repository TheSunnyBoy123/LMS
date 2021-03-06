import pickle
def dump_types(t):
    with open("accountTypes.txt", "w") as f:
        f.write(t)
    return

def ret_types():
    f = open("accountTypes.txt", "a")
    f.close()
    try:
        f = open("accountTypes.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}
def dump_studentSubs(t):
    with open("studentSubs.txt", "w") as f:
        f.write(t)
    return

def ret_studentSubs():
    f = open("studentSubs.txt", "a")
    f.close()
    try:
        f = open("studentSubs.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}
def dump_teacherSubjects(t):
    with open("teacherSubjects.txt", "w") as f:
        f.write(t)
    return
def ret_teacherSubjects():
    f = open("teacherSubjects.txt", "a")
    f.close()
    try:
        f = open("teacherSubjects.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

##############
#tableTimings: stored as {Monday:{1:"start - end", 2: "start -end", ...}, Tuesday: {1:"start - end", ....}, ...}
##############

def ret_tableTimings():
    f = open("tableTimings.txt", "a")
    f.close()
    try:
        f = open("tableTimings.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_tableTimings(tableTimings):
    f = open("tableTimings.txt", "w")
    f.write(tableTimings)
    f.close()
    return None


##############
#NOTES: stored as {studentName: notes}} or {teacher:{class:{students:individual notes}}}
##############
def ret_studentNotes():
    f = open("studentNotes.dat", "ab")
    f.close()
    try:
        f = open("studentNotes.dat", "rb")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}
def dump_studentNotes(t):
    with open("studentNotes.dat", "wb") as f:
        f.write(t)
    return

def ret_teacherNotes():
    f = open("teacherNotes.dat", "ab")
    f.close()
    try:
        f = open("teacherNotes.dat", "rb")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_teacherNotes(t):
    with open("teacherNotes.dat", "wb") as f:
        f.write(t)
    return

def ret_teacherQuickNotes():
    f = open("teacherQuickNotes.dat", "ab")
    f.close()
    try:
        f = open("teacherQuickNotes.dat", "rb")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_teacherQuickNotes(t):
    with open("teacherQuickNotes.dat", "wb") as f:
        f.write(t)
    return
##############
#Time Table: stored as {studentName: {day: [classes], day: []}, studentName: {day:[]} or {teacher: {day: [classes], day: []}, teacher: {day:[]}
##############
def ret_studentTimeTable():
    f = open("studentTimeTable.dat", "ab")
    f.close()
    try:
        f = open("studentTimeTable.dat", "rb")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}
def dump_studentTimeTable(t):
    with open("studentTimeTable.dat", "wb") as f:
        f.write(t)
    return

def ret_teacherTimeTable():
    f = open("teacherTimeTable.dat", "ab")
    f.close()
    try:
        f = open("teacherTimeTable.dat", "rb")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}
def dump_teacherTimeTable(t):
    with open("teacherTimeTable.dat", "wb") as f:
        f.write(t)
    return

##############
#Tasks/Deadlines: stored as {Name:{task: (subject, deadline), task: (subject, deadline)}} for student and as {name:{task:(class, deadline)}} for teacher
##############
def ret_studentTasks():
    f = open("studentTasks.txt", "a")
    f.close()
    try:
        f = open("studentTasks.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_studentTasks(t):
    with open("studentTasks.txt", "w") as f:
        f.write(t)
    return

def ret_teacherTasks():
    f = open("teacherTasks.txt", "a")
    f.close()
    try:
        f = open("teacherTasks.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_teacherTasks(t):
    with open("teacherTasks.txt", "w") as f:
        f.write(t)
    return

##############
#Requests to be added to teacher's class: stored as {name:{teachername:className},...}
##############
def ret_requests():
    f = open("requests.dat", "ab")
    f.close()
    try:
        f = open("requests.dat", "rb")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_requests(t):
    with open("requests.dat", "wb") as f:
        f.write(t)
    return

##############
#Classes: stored as {name:{class:subject(from student)}} for student and {name:{class:[students]}} for teacher
##############
def ret_studentClasses():
    f = open("studentClasses.txt", "a")
    f.close()
    try:
        f = open("studentClasses.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_studentClasses(t):
    with open("studentClasses.txt", "w") as f:
        f.write(t)
    return

def ret_teacherClasses():
    f = open("teacherClasses.txt", "a")
    f.close()
    try:
        f = open("teacherClasses.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_teacherClasses(t):
    with open("teacherClasses.txt", "w") as f:
        f.write(t)
    return
##############
#Marks: stored as {Name:{Subject:[(mark, outMarks),(Mark, outMarks)]}} for student and {teacherName: {class:{student:[(grade, out), (grade, out)]}}} for teacher
##############

def ret_studentMarks():
    f = open("studentMarks.txt", "a")
    f.close()
    try:
        f = open("studentMarks.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}

def dump_studentMarks(t):
    with open("studentMarks.txt", "w") as f:
        f.write(t)
    return

def ret_teacherMarks():
    f = open("teacherMarks.txt", "a")
    f.close()
    try:
        f = open("teacherMarks.txt", "r")
        d = eval(f.read())
        f.close()
        return d
    except SyntaxError:
        f.close()
        return {}


def dump_teacherMarks(d):
    f = open("teacherMarks.txt", "w")
    f.write(str(d))
    f.close()
    return None


