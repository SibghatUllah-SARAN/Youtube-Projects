# creating a simple calculator in python
num_1=int(input("\n\t\t Enter first number : \t"))
num_2=int(input("\n\t\t Enter Second number : \t"))

opp=input("\n\t\t Choose oiprater from    '+', '-', '/', '*' ")

if opp=='+':
    result=num_1+num_2
    print(f"n\t\t\t The Result is :  \t {result}\n\n")

elif opp=='-':
    result=num_1-num_2
    print(f"n\t\t\t The Result is :  \t {result}\n\n")

elif opp=='*':
    result=num_1*num_2
    print(f"n\t\t\t The Result is :  \t {result}\n\n")

elif opp=='/':
    result=num_1/num_2
    print(f"n\t\t\t The Result is :  \t {result}\n\n")
    
else:
    print("\t\t\t Invalid Choice  Sorry \3\3")

    #  NOW LETS RUN THIS CODE