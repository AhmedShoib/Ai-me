#مكان حفظ اسعار سلع 
item1 = 10
item2 = 50
item3 = 200

#مكان حفظ الميزانيه
budget = 200

#حساب التكلفه
total = item1 + item2 + item3

#حساب الفرق
difference = budget - total

#طباعه الناتج
print("Total cost" + str(difference))

#مقارنه
if budget>= total:
    print("Your budget is sufficient! You'll have some left over"+" "+str(difference)+" "+ "pounds")
else:
    -difference == -1 * difference
    print("The budget is insufficient. You need"+" "+str(-difference)+" "+"pounds")