import mysql.connector
import time
from datetime import datetime
from getpass import getpass
from bullet import Password
#dictionary
restuarant = {"bawarchi" : {"biryani":110,"rice":75,"curd":10,"roti":5}, "paradise": {"cicken curry":35,"biryani":115,"mutton curry":45,"icecream":15}
               , "udipi": {"idly":20,"dosa":25,"puri":30,"wada":30}}

database1 = mysql.connector.connect(host="localhost", user="root",password="12345678",database="project1")
cur = database1.cursor()

#function start
def time_Function():
    now = datetime.now()
    currentTime = now.strftime("%H")
    end_time = 18
    if currentTime == str(end_time):
            print("sorry we are closed")
    elif currentTime == str(17):
            print("we are closing soon....",now.strftime("%H:%M:%S"))
    else:
            print("we are open now...🍔")

#function start
def owner_key():

    print("You can use your account...😎")
    time_Function()
    print("Currently available restuartants : ", list(restuarant.keys()))
    funcuserchoice()
#function start
def funcuserchoice():
    userchoice = str(input("Enter your restuarant to know food items : ")).lower()

    print(list((restuarant[userchoice])))
    if userchoice == "bawarchi":
        print("Location - sr nagar")
    elif userchoice == "paradise":
        print("Location - secunderabad")
    elif userchoice == "udipi":
        print("Location - kukatpally")
    #Temporary testing code

    food_items = str(input("select your : "))


    if food_items in restuarant[userchoice]:
        print(restuarant[userchoice][food_items])
        print(food_items,"cost -> ",(restuarant[userchoice][food_items]),"rps")

    #below line allows user to select mutliple words.
    x = list(map(str, input("Enter a multiple value: \n ").split("|")))
    print("List of students: ", x)
    print(x)

    a = []
    for i in x:
        if i in restuarant[userchoice]:
            a.append(restuarant[userchoice][i])
    print(sum(a))
#function-end

#function-start

def addDetails():


    id = int(input("Enter id:"))
    firstname = str(input("Firstname : "))
    lastname = str(input("Lastname : "))
    dob = int(input("DOB : "))
    email = str(input("Emailid : "))
    phonenumber = int(input("Phone Number : "))
    username = str(input("Username : "))
    password = getpass("Password : ")

    newAccount = {"id":id,"firstname": firstname, "lastname": lastname, "dob" : dob, "emailid" : email, "phonenumber" : phonenumber, "username" : username, "password" : password}
    s="INSERT INTO details values(%s,%s,%s,%s,%s,%s,%s,%s)"
    t=(id,firstname,lastname,dob,email,phonenumber,username,password)
    cur.execute(s,t)
    database1.commit()

    owner_key()


#function-end


def funccalls():

    selectoption = str(input("Create account Login "))
    if selectoption == "create account":
        addDetails()
     # owner_key(username="foodlist", password="5star")

    user_id = str(input("Enter your unique id : "))
    user_name = str(input("Enter your name : "))
    # pass_word = str(input("Enter your password : "))
    pass_word = Password(prompt="password: ", hidden="*")
    result1 = str(pass_word.launch())
    cur.execute("select id from details")
    result = cur.fetchall()
    p = [', '.join(map(str, x)) for x in result]
    if user_id in p:
        owner_key()

funccalls()




#save all usernames in a list and then use a method to find weather the userinput login is in that list. if it exits then call the function.
