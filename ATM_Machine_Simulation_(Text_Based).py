'''PROJECT : ATM_Machine_Simulation_(Text_Based)'''

'''it can check your security pin system, withdrawal, deposit and check balance'''
# variables

pin = 1234
balance = 10000

# intro

print(" ")
print("==================================================") 
print("             Welcom To Awaisey Bank 🏛️ ")
print("==================================================") 

# agar pin incorrect ho :
for i in range(3):
    
    print(" ")
    pin1 = int(input("Enter Your 4 digit Pin 🔢: "))

    if pin1 == pin:
       print("\nLogin Successful ✅\n")
       break
    else:   
       print("You Enter Incorrect Pin ❌ TRY AGAIN ")
       print(" ")
else:
    print("You Tried 3 Times ❌ !! \n  and now Your Account is BANNED ☠️") 
    exit()


# main body :
while True:
      print("==================================================") 
      print("                      Menu ")
      print("==================================================") 

      
      print(" ")
      print("Select What do You Want To Do? ")
      print("------------------------------")
      print(" ")
       
      print("1. Withdrawal Money")        
      print("2. Deposit Money")        
      print("3. Check Your Balance")
      print("4. Exit The ATM !")
      print(" ")
      
#   choice taken by user
      choice = int(input("Enter Your Choice Here: "))
      print(" ")
    
#   Withdrawal money
      if (choice == 1):
        w_a = int(input("Enter Your Withdrawal Amount 💰: "))
        if w_a > balance:
           print("Insufficent Balance In Your Account ❌")
           print(" ")
           print("==================================================") 

        else:
           print(" ")
           print("Money Withdrawal Succesfully ✅")
           balance -= w_a
           print(" ")
           print(f"Account Balance After Withdrawal is : --> {balance} ")
           print(" ")          
           print("==================================================") 
    
#    deposit money
      elif (choice == 2):
        d_a =  int(input("Enter Deposit Amount ✨  :  "))
        balance += d_a
        print(" ")
        print(f"Your New Balance After Deposit is : --> {balance}")
        print(" ")
        print("==================================================") 
      
#   check balance
      elif (choice == 3):
         print(f"Your Current Balance is --> ' {balance} ' 💸✨")
         print(" ")
         print("==================================================") 

#    exit
      elif(choice == 4):
         break

#    if choice is invalid
      else:
         print("❌ Invalid Choice is entered ")
   
print("==================================================") 