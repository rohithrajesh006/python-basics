while True:
      num1=int(input("Enter first number :"))
      num2=int(input("Enter second number :"))
      print("1.Addition \n2.Substraction \n3.Multiplication \n4.Division")
      choice=int(input("Enter your choice :"))
      if choice==1:
        print(num1+num2)
      elif choice==2:
        print(num1-num2)
      elif choice==3:
        print(num1*num2)
      elif choice==4:
        print(num1/num2)
      else:
       print("Enter an ivalid choice!!")

      choice2=str(input("Do you want to continue (yes/no) :"))

      if choice2.lower()!="yes":
         break