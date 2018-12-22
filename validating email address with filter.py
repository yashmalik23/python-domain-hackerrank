import re
def fun(s):
    # return True if s is a valid email, else return False
    a = re.match("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$",s)
    return a
    