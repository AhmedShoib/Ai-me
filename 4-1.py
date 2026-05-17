def calculator(a, b, operation):
    """
    تقوم بالعمليات الحسابية الأساسية: ("add", "subtract", "multiply", "divide")
    """
    # تحويل النص إلى حروف صغيرة لتجنب الأخطاء إذا كُتبت الحروف كبيرة
    op = operation.lower()
    
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        # التعامل مع حالة القسمة على صفر بأمان
        if b == 0:
            return "خطأ: لا يمكن القسمة على صفر."
        return a / b
    else:
        return "خطأ: عملية غير صالحة. يرجى اختيار 'add', 'subtract', 'multiply', أو 'divide'."
#ادخال المستخدام
m1 = int(input("الرقم الاول")) 
m2 = int(input("الرقم الثاني"))
operation =input("العملية الحسابية (add, subtract, multiply, divide): ")
print(calculator(m1,m2,operation)) #الاخراج

# --- أمثلة على التشغيل ---
print(calculator(10, 5, "add"))       # النتيجة: 15
print(calculator(10, 2, "divide"))    # النتيجة: 5.0
print(calculator(10, 0, "divide"))    # النتيجة: خطأ: لا يمكن القسمة على صفر.
print(calculator(5, 5, "Multiply"))   # النتيجة: 25 (تعمل بنجاح رغم الحرف الكبير)
