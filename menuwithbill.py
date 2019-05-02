#Default program for creating a menu or ordering from a menu at a restaurant
#Update take multiple orders and Print Bill
name=print("Welcome to Bad Food.com")
default_menu=["1.Steak:$10","2.Fish & chips:$7.99"
              ,"3.Pizza:$6.94","4.Burgers:$5.99"]
prices=[10,7.99,6.94,5.99]
user=int(input("Press for: "+"\n 1.Customer"+"\n 2.Manager "))
import random
x=random.randint(1,101) #just to give a professional look we will print a cutomer number randomly generated
if(user==2):
    password=int(input("\n Enter password: "))
    if(password==1234):
        new_item="5."+input("\n Enter new item: ")
        default_menu.append(new_item)
        print(default_menu)
    else:
        print("\n Wrong Password")
elif(user==1):
    print(default_menu)
    total_order=[]
    fin_order="Yes"
    quant=0
    bill=0
    while(fin_order!="NO"):
        sumindivual=0
        new_list=[]
        order=int(input("\n Enter choice: "))
        quant=int(input("\n Enter Quantity: "))
        sumindivual=prices[order-1]*quant
        bill=bill+sumindivual
        z=[default_menu[order-1],quant,sumindivual]
        total_order.append(z)
        fin_order=input("Would like anything else?"+"\n Yes/No: ").upper()
    print("Order Id: "+str(x)+"\n\t Item "+"\t\t  Quantity"+"\t Total Amount")
    for i in range(0,len(total_order)):
        print(*total_order[i],sep="         ",end="  ")
        print(" ")   
else:
    print("Wrong input")
print("\n Thank You, for the order")
        
