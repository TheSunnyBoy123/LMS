import pickle

def ret_loadPasswords(): #returns dictionary {username:password} to reload previous sessions
    f = open("passwords.dat", "ab")
    f.close()
    try:
        f = open("passwords.dat", "rb")
        d = eval(f.read())
        return d
    except SyntaxError:
        return {}



