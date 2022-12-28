import random 

charc= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_+={}[].?/,<>"


while 1:
    password_leng=int(input("Enter The Length Of The Password: "))
    password_count=int(input("How Many Passwords Would You Like: "))
    if password_leng>=12:
        for x in range(0,password_count):
            passwd=""

            for x in range(0,password_leng):
                passwd_charc=random.choice(charc)

                passwd=passwd + passwd_charc
            print("Here Is Your Password: ",passwd)
    else:
        print("Length of Password should Be At Least 12. Enter New Length.")



    
