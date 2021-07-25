import pickle
def writes():
    f = open("test.dat", "w")
    s = str({1:{10:100, 20:200}})
    f.write(s)
    f.close()

def reads():
    f = open("test.dat", "r")
    r = eval(f.read())
    print(type(r))
    print(r)
    f.close()

writes()
reads()
