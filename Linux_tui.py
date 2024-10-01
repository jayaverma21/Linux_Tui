import os

import getpass

os.system("tput setaf 1")

print("\t\t Jaya's TUI Program of Linux ")

os.system("tput setaf 7")

print("\t\t\t----------------------------")



passwd = getpass.getpass("Enter you passwod: ")

mypass = "redhat"

if passwd != mypass :

    print("auth incoorect")

    exit()



print("Enter your location where you want to run your command (remote/local) : " , end="")

location = input()



if location == "remote":

    remoteIp = input("enter remote sytem ip : ")



while True:

        print("""Press 1: to see date 

        Press 2: to see cal

        Press 3: to see ls

        Press 4: to create user

        Press 5: to config webserver

        press 6: to networking 

        press 7 : to create file

        press 0 : to exit 

        """)



        print("Enter Your choise: ", end="")

        choose = input()



        if location == "local":

            if int(choose) == 1:

                os.system("date")

            elif int(choose) == 2:

                os.system("cal")

            elif int(choose) == 3:

                os.system("ls")

            elif int(choose) == 4:

                print("Enter username : " , end ="")

                createUser = input()

                os.system("useradd {} ".format(createUser))

            elif int(choose) == 0:

                exit()

            else:

                print("no cmd here")

            input("Enter for continue......")        

            os.system("clear")

        

        elif location == "remote":

            if int(choose) == 1:

                os.system("ssh {0} date".format(remoteIp))

            elif int(choose) == 2:

                os.system("ssh {0} cal".format(remoteIp))

            elif int(choose) == 3:

                os.system("ssh {0} ls".format(remoteIp))

            elif int(choose) == 4:

                print("Enter username : " , end ="")

                createUser = input()

                os.system("ssh {0} useradd {1} ".format(remoteIp , createUser))

            elif int (choose) == 0:

                exit()

            else:

                print("no cmd here")
        else:

            print("location does'nt support currently")
