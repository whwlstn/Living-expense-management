import numpy as np 
import matplotlib.pyplot as plt 


print("Hello! This is a LIVING EXPENSE MANAGEMENT PROGRAM.")
print("Please enter all your daily expenses of a single week.")
# print("If you entered all the expenses, pleae enter DONE.")
print("")
currency = int(input("Which currency do you use? Enter 1 for US DOLLAR($) or 2 for SOUTH KOREAN WON(￦): "))

print("")

if (currency == 1):
    print("You chose USD($)! Please enter all your expenses in dollar.")
    currencyOutput = "USD($)"
        
if (currency == 2):
    print("You chose KRW(￦)! Please enter all your expenses in won.")
    currencyOutput = "WON(￦)"
print("")

numWeek = 1
expenseList = []
typeList = [0, 0, 0, 0, 0]
num = 0

while(numWeek <= 5):
    print("Week", numWeek)
    
    weekTotal = 0

    while (True):
        
        expense = float(input("ENTER YOUR EXPENSE HERE in " + currencyOutput + " (Please enter 0 if you finish with entering the expenses of a whole week): " ))
        if (expense == 0):
            break
        elif(expense < 0):
            print("ERROR: DO NOT ENTER NEGATIVE VALUE.")
        else:
            print("Your entered ", expense, currencyOutput, ".")
            num += 1
            weekTotal += expense

        print("Please enter the reason of the payment.")
        print("For GROCERY(Amazon fresh, Costco, Target, etc...), enter 1.")
        print("For DELIVERY FOOD(Uber Eats, Door Dash, etc...), enter 2.")
        print("For APARTMENT FEE, enter 3.")
        print("For FEE FOR STUDYING(textbooks, applications, etc...), enter 4.")
        print("OTHERS, enter 5.")
        
        type = int(input("ENTER HERE: "))
        print("")

        if (type == 1):
            typeList[0] += expense
        elif (type == 2):
            typeList[1] += expense
        elif (type == 3):
            typeList[2] += expense
        elif (type == 4):
            typeList[3] += expense
        else:
            typeList[4] += expense

    expenseList.append(weekTotal)
    numWeek += 1
    print("")

print("________________________________________")
print("             EXPENSE RESULT             ")
print("________________________________________")
print("")

# compute average
total = 0
for weeklyExpense in expenseList:
    total += weeklyExpense

dailyAvg = total / num
weeklyAvg = total / 5
weekMax = max(expenseList)
mostSpentWeek = expenseList.index(weekMax)
typeMax = max(typeList)
indexOfMostSpentCategory = typeList.index(typeMax)

if indexOfMostSpentCategory == 0:
    mostSpentCategory = "GROCERY"
elif indexOfMostSpentCategory == 1:
    mostSpentCategory = "DELIVERY FOOD"
elif indexOfMostSpentCategory == 2:
    mostSpentCategory = "APARTMENT FEE"
elif indexOfMostSpentCategory == 3:
    mostSpentCategory = "FEE FOR STUDYING"
elif indexOfMostSpentCategory == 4:
    mostSpentCategory = "OTHERS"


print(" The average of daily expenses:  " + str(dailyAvg) + " " + currencyOutput)
print(" The average of weekly expenses: " + str(weeklyAvg) + " " + currencyOutput)
print(" The most spent week:            " + "Week " + str(mostSpentWeek + 1) + " (" + str(weekMax) + " " + currencyOutput + ")")
print(" The most spent category:        " + mostSpentCategory + " (" + str(typeMax) + " " + currencyOutput + ")")
print("")
print("________________________________________")
print("")
graph = input("Do you want to see the graph of your expense? (Y/N) ")

if graph != 'N' and graph != 'n': 

    # Graph of Weekly Payment Fluctuation 
    plt.bar(["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"], expenseList)
    plt.title('Weekly Payment Fluctuation')
    plt.xlabel('Weeks of Month')
    if (currency == 1):
        plt.ylabel('USD($)')
    if (currency == 2):
        plt.ylabel('WON(￦)')
    plt.show()

    # Graph of Expended Categories
    plt.bar(["GROCERY", "FOOD", "APARTMENT", "STUDYING", "OTHERS"], typeList, color = 'm')
    plt.title('Expended Categories')
    plt.xlabel('Categories')
    if (currency == 1):
        plt.ylabel('USD($)')
    if (currency == 2):
        plt.ylabel('WON(￦)')
    plt.show()

else:
    print("FINISHED!!!")