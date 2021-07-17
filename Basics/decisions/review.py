import time
print ("\n")
print ("\n")
print ("\n")
print ("            ##################################")
print ("            #######      WELCOME       #######")
print ("            #######         TO         #######")
print ("            #######      STEFAN BANK   #######")
print ("            ##################################""\n")
print ("\n")
print ("             #######  CHOSE OPTIONS     #######""\n")
time.sleep(0)
print ("                     1. FOR BALANCE CHECK""\n")
time.sleep(0)
print ("                     2. FOR CASH WITHDRAW""\n")
time.sleep(0)
print ("                     3. FOR DEPOSITING MONEY""\n")
time.sleep(0)
print ("                     4. FOR EXIT""\n")

#variable with the balance
balance = 5








choice = input()   ## GLOBAL CHOICE 

if (choice == "1"):
  print (" YOUR CURRENT BALANCE IS :",balance, "$")
  print ("\n")
  if (balance <10):
    print (" Look like you have a low balance")
    print ("\n")
    print (" Would you like to deposit some money?")
    print ("\n")
  answer = input(":")
  if (answer == "yes"):
    print (" How much you want to deposit?")
    ammount = float(input(":"))
    new_balance = str((ammount + balance))
    print ("your new balance is ",new_balance)

  elif (answer =="no"):

    print (" PRESS 0 EXIT")
    print ("\n")
    no =input()
    if (no == "0"):
      print (" ####  HAVE A GOOD DAY!  ####")
  else:
    print (" ERROR EXIT AND TRY AGAINE") ###### IF THE USER DOESNT ANSWER WITH "YES" OR "NO" THE PROGRAM WILL CLOSE AND DISPLAY A MESSAGE TO TRY AGAINE

if (choice == "2"):
  withdraw = float(input(" How MUCH YOU WANT TO WITHDRAW? : "))
  print ("\n")
  if ((balance < withdraw) or (withdraw <=0)):                           ####IMPLEMENTED  OR SITUATION !
    print (" You dont have that much money! good bye")
    print ("\n")
  else:
    new_balance = balance - withdraw
    print ("\n")
    print (" Your new balance is",new_balance,"$")




if (choice == "3"):

  deposit = float(input(" How much you want to deposit today? : "))
  print ("\n")

  if (deposit <=0 ):

    print(" You cannot deposit a negative ammount!")

    deposit = float (input(" Please enter againe"))
    print ("\n")

    final_balance =  balance + deposit

    print (" Balance updated your new balance is : ", final_balance,"$")
    print ("\n")
  

if (choice == "4"):
  print (" EXITING ...")
  print ("\n")
  time.sleep(1)
  print (" EXITING ...")
  print ("\n")
  time.sleep(1)
  print (" EXITING ...")
  print ("\n")
  print (" EXITING ...")
  print ("\n")
  time.sleep(1)
