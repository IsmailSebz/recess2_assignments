##INVENTORY MANAGEMENT SYSTEM BY ISMAIL
#

#Initialise a list data structure to store the available items
stock =[
		{"name":"Muwogo","price":"20000"},
		{"name":"rice","price":"300000"}
	]

choice=""
item_name=""
item_price=""

def sell_item():
	stock_table()
	num = int(input	(">>:"))
	
	if num >0 and num<=len(stock)  :
		stock.pop(num-1)
		print("Item sold")
		menu()
	else:
		print("Input value not found")
		menu()



def add_item():
	item={"name":"","price":""}
	print("Enter Item Name")
	item_name=input(">>:")
	print(f"Enter {item_name}'s Price")
	item_price=input(">>:")
	if len(item_name) == 0:
		add_item() 

	#INCASE THE LENGTH IS MORE, CODE WILL CONTINUE HERE
	item["name"]=item_name
	item["price"]=item_price
	stock.append(item)
	print("1. Enter Another")
	print("2. View Stock Items")
	print("3. Main Menu")
	choice=""
	choice=input(">>:")
	if choice=="1":
		add_item() 
	elif choice == "2":	
		view_stock_list()
	elif choice == "3":	
		menu()
	else:
		print("Invalid Entry")
		choice=input(">>:")

##THE IDEA IS TO CREATE A TABLE LIKE VIEW
def  stock_table():
	GAP=2
	headers=["No","Name","Price"]
	max_len_no=len(headers[0])
	max_len_name=len(headers[1])
	max_len_price=len(headers[2])


	#to get the column size
	for i in stock:
		if len(i["name"]) > max_len_name:max_len_name=len(i["name"])
	for i in stock:
		if len(i["price"]) > max_len_price:max_len_price=len(i["price"])
	
	#PRINT HEADERS
	print("".ljust(max_len_no+max_len_name+max_len_price+GAP*6-2,"-"))
	print("|"+
		headers[0].center(max_len_no+GAP) + "|" + 
	   	headers[1].center(max_len_name+GAP) + "|" +
		headers[2].center(max_len_price+GAP) + "|"
	   )
	print("".ljust(max_len_no+max_len_name+max_len_price+GAP*6-2,"-"))
	j=1
	
	#PRINT ITEMS IN STOCK
	for i in stock:
		print("|"+
		str(j).ljust(max_len_no+GAP) + "|" +
		i["name"].ljust(max_len_name+GAP) + "|" +
		i["price"].rjust(max_len_price+GAP) + "|"
		)
		j+=1


def view_stock_list():
	stock_table()
	print("1. Sell Item")
	print("2. Main Menu")
	choice=""
	choice=input(">>:")
	if choice=="1":
		sell_item()
	elif choice == "2":	
		menu()
	else:
		print("Invalid Entry")
		choice=input(">>:")


def menu():
	print("==========WELCOME TO HAJ WAHAB TRADERS =======")
	print("Choose Action to perform")
	print("1. Add item to stock")
	print("2. View Stock List")
	print("3. Sell Item")
	print("h. Help")
	print("q. Quit")

	while True:
		choice=input(">>")    
		if choice=="1":
			add_item()
			break
		elif choice=="2":
			view_stock_list()
			break
		elif choice =="3":
			sell_item()
			break
		elif choice =="h":
			inv_help()
			break
		else: 
			print("Invalid Choice")
			


menu()
        
    

