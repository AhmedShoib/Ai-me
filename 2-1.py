temp = float(input("Enter the current temperature in Celsius: "))#أدخال المستخدام
if temp >= 30:
    print("It's a hot day. Stay hydrated!")#أكبر من 30
elif 20 <= temp <= 29:
    print("It's a warm day. Enjoy the weather!")#من 20الي 29
elif 10 <= temp <= 19:
    print("It's a cool day. Wear a jacket!")#من10الي19
else:
    print("It's a cold day. Stay warm!")#اقل من 10
