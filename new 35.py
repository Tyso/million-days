import random
print("Type integer for required: ")
print("0.snake")
print("1.water")
print("2.gun")
b=int(input("enter number between 0,1,2 : "))
match b:
    case 0:
        print("user input : snake")
    case 1:
        print("user input : water")   
    case 2:
        print("user input : gun")     
a=random.randint(0,2)
if a==0:
    print("computer : snake")
elif a==1:
    print("computer : water")
else:
    print("computer : gun")        

