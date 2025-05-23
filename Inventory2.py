##INVENTORY MANAGEMENT SYSTEM BY ISMAIL
#
#TODO: CREATE A MENU
#TODO: CREATE METHODS TO HANDLE THE MENU
#TODO: VIEW ITEMS IN TABLE STYLE

#Initialise a list data structure to store the available items
stock =[
		{"name":"Muwogo","price":"20000"},
		{"name":"rice","price":"300000"}
	]
sold =[
		# {},
		# {}
	]

choice=""
item={"name":"","price":""}
item_name=""
item_price=""

def sell_item():
	headers=["No","Name","Price"]
	table_view(headers,stock)
	print("Enter Item Number to sell")
	num = int(input	(">>:"))
	
	if num >0 and num<=len(stock)  :
		sold.append(stock.pop(num-1))	#REMOVES FROM STOCK LIST TO SOLD LIST
		print("Item sold")
		menu(False)
	else:
		print("Input value not found")
		menu(False)



def add_item():
	
	print("Enter Item Name")
	item_name=input(">>:")
	print(f"Enter {item_name}'s Price")
	item_price=input(">>:")
	if len(item_name) == 0:
		add_item() #RECURSE UNTILL THE USER ENTERS SOMETHING

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
def  table_view(headers,item_list):
	GAP=2
	#SETTING MAX INITIAL COLUMN SIZES AS HEADING SIZE
	max_len_no=len(headers[0])+GAP
	max_len_name=len(headers[1])+GAP
	max_len_price=len(headers[2])+GAP


	#to get the column size
	for i in item_list:
		if len(i["name"]) > max_len_name:max_len_name=len(i["name"])
	for i in item_list:
		if len(i["price"]) > max_len_price:max_len_price=len(i["price"])
	
	#PRINT HEADERS
	print("".ljust(max_len_no+max_len_name+max_len_price+GAP*3-2,"-"))
	print("|"+
		headers[0].center(max_len_no) + "|" + 
	   	headers[1].center(max_len_name) + "|" +
		headers[2].center(max_len_price) + "|"
	   )
	print("".ljust(max_len_no+max_len_name+max_len_price+GAP*3-2,"-"))
	j=1
	
	#PRINT ITEMS IN STOCK
	for i in item_list:
		print("|"+
		str(j).ljust(max_len_no) + "|" +
		i["name"].ljust(max_len_name) + "|" +
		i["price"].rjust(max_len_price) + "|"
		)
		j+=1
	print("".ljust(max_len_no+max_len_name+max_len_price+GAP*3-2,"-"))

def view_sold_list():
	headers=["No","Name","Sold At"]
	table_view(headers,sold)
	menu(False)

def view_stock_list():
	headers=["No","Name","Price"]
	table_view(headers,stock)

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


def menu(isstart=True):
	if isstart:
		print("==========WELCOME TO HAJ WAHAB TRADERS =======")
		print("Choose Action to perform")
	print("1. Add item to stock")
	print("2. View Stock List")
	print("3. Sell Item")
	print("4. View Sold List")
	
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
		elif choice =="4":
			view_sold_list()
			break
		elif choice.upper() =="Q":
			
			break
		else: 
			print("Invalid Choice")
			


menu()
        
    

