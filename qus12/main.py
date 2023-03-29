t=("usernasme",)
l=t+("password",)
print(l)
try:
    username = "user"
    password = 1234
    login_info = (username, password)
    login_info = login_info[0] + "," + str(login_info[1])
    # do something with the login_info tuple
except TypeError:
    print("error: cannot concatenate string and number")
print(login_info("user"+1234))