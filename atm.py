
#features:
#create account
#put in your pin
#withdraw
#check balance
#transfer
#change pin
#lock


#assignment:
#create a dictionary of account, let the parameters be name, account number and pin
#remove name, account no, and pin from ibk_atm dictonary
#add a new object into the ibk_atm dictionary



#version1
account_ibk = {"name":"", "account":"0987654334", "pin":"1234"}
ibk_atm = {"account": account_ibk, "balance": 420, "account_no": "0987654334", "status": True}
ibk_atm2 = {"account": account_ibk, "balance": 920, "account_no": "0987654334", "status": True}

abr_atm = {"name": "abr", "pin": "0000", "balance": 0,  "account_no": "0737483837", "status": True}
#name, pin, balance, accouht no, status


#version2
#pin = "3456"
#f ibk_atm["pin"] == pin:
 #   print("Welcome")
#else:
#    print("Wrong pin")
    
#print("087654")


#version3
#pin = "1234"

#checker = True
#while checker == True:
#    if ibk_atm["status"] == True:
#       if ibk_atm["pin"] == pin:
#          print("Welcome")
#            balance = ibk_atm["balance"]
#            print("$", balance)
#    
#        else:
#            print("Wrong pin")
#        
#    else:
#        print ("account blocked")

#print(ibk_atm)
#print(ibk_atm2)
#print(abr_atm)

#version 4
#hile True:
#    input_pin = str(int(input("Please enter pin:")))
#    if input_pin == ibk_atm["account"]["pin"]:
#        print("Welcome")
#        break
#    else:
#        print("Wrong!!!1")

#print("Goodbye and see you again")

#version5
#input_pin = str(int(input("Please enter pin:")))
#while True:
    #if input_pin == ibk_atm["account"] ["pin"]:
        #print("########Welcom#########")
        #input_var = int(input("Choose an option: \n1: fund  \n2: "
      #                        "withdraw \n3: send \n4: balance" "\n5: end \nOption: "))
        
        
        #if input_var == 5:
         #   break
        #elif input_var ==4:
          #  balance = ibk_atm["balance"]
         #   print(balance)
        #elif input_var == 1:
       #     amount =int(input("Enter amount: "))
     #       ibk_atm["balance"] += amount
      #      print("Fund transaction successful")
    #    else:
   #         pass
        
  #  else:
 #       print("Wrong!!!")

#print("Goodbye, see you again")

#version6
if ibk_atm["status"] == True:
    while True:
        #print(ibk_atm)
        try:
            input_pin = str(int(input("Enter your pin")))
        except:
            print("Sorry, try an integer")
            input_pin = str(int("Try again: "))
            
        
        if input_pin == ibk_atm["account"] ["pin"]:
            print("#########Welcome###########")
            input_var = int(input("Choose an option: \n1: fund  \n2: "
                                "withdraw \n3: send \n4: balance"
                                "\n5: end \n \n6:lock \nOption: "))
            if input_var ==5:
                break 
            elif input_var == 4:
                balance = ibk_atm["balance"]
                print(balance)
            elif input_var == 1:
                amount =int(input("Enter amount: "))
                ibk_atm["balance"] += amount
                print("Fund transaction successful")
            elif input_var == 2:
                amount = int(input("Enter amount"))
                ibk_atm["balance"]-= amount
                print("withdrawal successful")
            elif input_var == 3:
                account_no = (int(input("Enter account number:")))
                amount = (int(input("how much:")))
                ibk_atm["balance"] -= amount
                ibk_atm2["balance"] += amount
                print("send successful")
            elif input_var == 6:
                ibk_atm["status"] = False
                print("sorry, network issue")
                break
            else:
                pass
            
        else:
            print("Wrong pin!")
            
else:
    print("wrong pin!")
    
    

print("Goodbye, see you again")






    
