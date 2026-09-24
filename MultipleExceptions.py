try:
    num1,num2 = eval(input("enter two numbers, separared by a comma:"))
    result = num1 / num2
    print("the result is", result)

except ZeroDivisionError:
    print ("division by zero is error !!")
except SyntaxError:
    print("comma is missing. Print numbers separated by comma like this 1,2")

except:
    print("wrong input")

else:
    print("no exeptions") 

finally:
    print("this will execute no matter what")