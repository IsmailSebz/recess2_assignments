##INVENTORY MANAGEMENT SYSTEM BY ISMAIL
#

#Initialise a list data structure to store the available items
stock =[]
choice=""
item_name=""
item_price=""

def add_item():
	print("Enter Item Name")
	item_name=input(">>:")
	print(f"Enter {item_name}'s Price")
	item_price=input(">>:")
	if len(item_name) == 0:
		add_item() 

	#INCASE THE LENGTH IS MORE, CODE WILL CONTINUE HERE
	stock.append(item_name)
	print("1. Enter Another")
	print("2. Main Menu")
	choice=""
	choice=input(">>:")
	if choice==1:
		add_item() 
	elif choice == 2:	
		menu()
        
        




def menu():
    print("==========WELCOME TO HAJ WAHAB TRADERS =======")
    print("Choose Action to perform")
    print("1. Add item to stock")
    print("2. View Stock List")
    print("3. Sell Item")
    print("h. Help")

menu()
while True:
    choice=input(">>")    
    if choice=="1":
        add_item()
        break
    elif choice=="2":
        view_stock()
        break
    elif choice =="3":
        sell_item()
        break
    else: 
         print("Invalid Choice")
          
        
    

