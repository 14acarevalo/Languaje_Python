#Title - Notebook Practise Python - Your Spends
#Description - This notebook is a simple program that asks the user about their monthly income and expenses
#Author - Alberto Campanero Arévalo
#Date - 2025-07-02

print ("Welcome to Notebook Practise Python, today we are doing a notebook about your spends")

print("User, please, insert your name: ")
name = input()
print("Hello " +str(name) + ", let's start with the first question")
print("Are you working? (yes/no)")
answer = input()

if answer == "yes":
    print("Great! How much do you earn per month?")
    salary = float(input())
    print ("Now, I need to know how mucho you spend per month")
    print("Do you have to pay a house? (yes/no)")
    answer1 = input()
    
    if answer1 == "yes":
        print("How much do you pay for your house per month?")
        house = float(input())   
    else:
        house= 0.0
        
    print("Do you have to pay a car or other vehicle? (yes/no)")
    answer2 = input()
    
    if answer2 == "yes":
        print("How much do you pay for your car or other vehicle per month?")
        vehicle = float(input())   
    else:
        vehicle = 0.0
    
    print("Do you have to pay for food? (yes/no)")
    answer3 = input()
    
    if answer3 == "yes":
        print("How much do you spend on food per month?")
        food = float(input())
    else:
        food = 0.0
        
    print("Do you have to pay for ocio? (yes/no)")
    answer4 = input()
    
    if answer4 == "yes":
        print("How much do you spend on ocio per month?")
        ocio = float(input())
    else:
        ocio = 0.0
        
    print("Have you earn any money from other sources? (yes/no)")
    answer5 = input()
    
    if answer5 == "yes":
        print("How much do you earn from other sources per month?")
        other_income = float(input())
    else:
        other_income = 0.0
        
    print("Have you got other expenses? (yes/no)")
    answer6 = input()

    if answer6 == "yes":
        print("How mucho do you spend on other expenses per month?")
        other = float(input())
    else:
        other = 0.0
        
    print("How much money do you save per month?")
    save_money = float(input())
        
    print("Okey, now I will calculate your money balance")
    money_balance = salary+other_income -(house+vehicle+food+ocio+other)
    
    if money_balance >= save_money:
        print("Congratulations " +str(name) + ", you can save money this month! Your balance is: " + str(money_balance))
    else:
        print("Sorry " +str(name) + ", you cannot save money this month. Your balance is: " + str(money_balance))
        
        
else:
    print("No problem, but I neet to know how much your earn per mont?")
    money = float(input())
    print ("Maybe, you cannot save money, but you can try to reduce your expenses")
    
