income=0
expenses=0
while True:
    print("\n======مدیریت دخل و خرج======")
    print("1.ثبت درآمد")
    print("2.ثبت هزینه")
    print("3.نمایش موجودی")
    print("4.گزارش مالی ")
    print("5.خروج")
    choice=input("انتخواب شما:")
    if choice == "1":
        amount= int(input("مبلغ درآمد را وارد کنید :"))
        income +=amount
        print("درآمد با موفقیت ثبت شد.")
    elif choice == "2":
        amount=int(input("مبلغ هزینه را وارد کنید:"))
        if amount <=income - expenses:
            expenses +=amount 
            print("هزینه با موفقیت ثبت شد.")
        else :
            print("موجودی کافی نیست!")
    elif choice =="3":
        balance= income - expenses
        print("موجودی شما:",balance)
    elif choice =="4":
        print("مجموع درآمد:",income)
        print("مجموع هزینه:",expenses)
        print("موجودی:",income-expenses)
    elif choice == "5":
        break
    else:
        print("گزینه انتخواب شده نا معتبر است")
        
    
    
    
    
    
    
    
    