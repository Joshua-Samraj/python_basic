


def validate(a,b):
    if(s_username == a and s_password == b ):
        return " Welcome " + a
    else:
        return " Wrong Username or Password "

s_username = "Joshua"
s_password = "123"
uname = input("Enter Username : ")
u_password = input("enter a password : ")

c =  validate(uname,u_password)    
print(c)   