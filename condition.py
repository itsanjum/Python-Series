 # if condition

# age= int(input("Enter your age : "))
# if (age>=18):
#     print("you are eligible to vote")

# balance =float(input("Enter your bank balance "))
# if balance <= 20000:
#     print("You are not eligible to take a loan")


# if -else Condition

# age=int(input("Enter your age: "))
# if age>=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")    


# number = int(input("Enter a number : "))
# if number % 2 == 0 :
#     print("The number is even")
# else :
#     print("The number is odd")    

#IF-ELIf statement

# marks=int(input("Enter your marks "))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else :
#     print("Grade D")    


num1 =int(input("Enter your first number "))
num2 =int(input("Enter your Second number "))
operator= input("Enter the operator (+,-,*,/) : ")
match operator :
    case "+" :
        print("Result : " ,num1 + num2)
    case "-" : 
        print("Result : " ,num1 - num2)
    case "*" : 
        print("Result : " ,num1 * num2)
    case "/" : 
        print("Result : " ,num1 / num2)
    case "_" : 
        print("Invalid Operator")