#2020年12月10日20:24:53
import json
filename='user_name.jason'

def get_user_name():
    username=input("what's your name? ")

    with open(filename,'w') as f:
        json.dump(username,f)
        print("fine,you won't be forgot")

def greet_user():
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        get_user_name()
    else:
        print("hello, %s! here you are, we met again!"%username)

greet_user()