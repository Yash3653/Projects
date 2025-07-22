print("welcome to BYD bank \nPlease Insert your card...")
password=8949
balance=1000000
choice=0
pin=int(input("Enter your password"))
if(pin==password):
    while(choice !=4):
        print("\n __Menu__")
        print("1==balance")
        print("2==deposite")
        print("3==withdraw")
        print("4==cancel\n")
        
        choice=int(input("\n Enter u r option:"))
        
        if(choice==1):
            print("Balance=usd",balance)
        
        elif(choice==2):
            depo=int(input("enter your deposite:usd"))
            balance+=depo
            print("\ndeposite amount:use",depo)
            
            print("Total balance=usd",balance)
        elif(choice==3):
            withdraw=int(input("Enter the amount to withdraw:usd"))
            balance-=withdraw
            print("\n withdraw amount: usd", withdraw)
            print("total balance=usd",balance)
        elif(choice==4):
            print("\n Cancelled")
else:
    print("wrong password !!")