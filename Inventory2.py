##INVENTORY MANAGEMENT SYSTEM BY ISMAIL
#
#TODO: CREATE A MENU
#TODO: CREATE METHODS TO HANDLE THE MENU
#TODO: VIEW ITEMS IN TABLE STYLE

#Initialise a list data structure to store the available items
stock =[
		{"name":"Muwogo","price":"20000","quantity":"2"},
		{"name":"rice","price":"300000","quantity":"1"},
		{"name":"matooke","price":"300000","quantity":"10"},
	]
sold =[
		# {},
		{"name":"Muwogo","price":"200000000","quantity":"2",},
		# {}
	]

choice=""
item={"name":"","price":"","quantity":0}
item_name=""
item_price=""

def sell_item():
	headers=["No","Name","Price","Qty"]
	table_view(headers,stock)
	print("Enter Item Number to sell")
	num = int(input	(">>:"))
	selected = stock[int(num-1)]
	print(f"Available Quantity {selected["quantity"]}")
	qty=input(">>:")
	if num >0 and num<=len(stock)  :
		sold.append(stock.pop(num-1))	#REMOVES FROM STOCK LIST TO SOLD LIST
		print("=====Item sold=======")
		menu(False)
	else:
		print("Input value not found")
		menu(False)

def search():
	print("Search item name")
	term = input(">>:")
	searched = []
	for itm in stock:
		if itm["name"].find(term)!=-1:
			searched.append(itm)
	
	if len(searched)==0:
		print("No item found")
	else:
		headers=["No","Name","Price","Qty"]
		table_view(headers,searched)
	print("Press Enter to to to main menue")
	term = input(">>:")
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
	col_sizes=[]	#STORE INDIVIDUAL COL SIZES
	col_size = 0	#STORE TOTAL COL SIZE
	for i in headers:
		col_sizes.append(len(i)+GAP)	#add all sizes to the list
	
	
	for i in item_list:
		j=1
		for k,v in i.items():
			if col_sizes[j]<len(str(v))+GAP:
				col_sizes[j]=len(str(v))+GAP
			j+=1
	#now fill the max col size
	for i in col_sizes: col_size += i


	#PRINT HEADERS
	print("-" * (col_size+len(col_sizes)+1))
	head_txt="|"
	J=0
	for i in headers:
		head_txt += i.center(col_sizes[headers.index(i)]) + "|"
	print(head_txt)
	print("-"*(col_size+len(col_sizes)+1))

	
	
	#PRINT ITEMS IN STOCK
	j=1
	for item in item_list:
		list_txt="|"
		v_txt=""
		i=1
		list_txt += str(j).ljust(col_sizes[0]) +"|"
		for k,v in item.items():
			isint=False
			try:
				isint=int(v)
			except: ValueError
			
			if isint:
				v_txt += str(v).rjust(col_sizes[i]) + "|"
			else:
				v_txt += str(v).ljust(col_sizes[i]) + "|"
			i+=1
		print(list_txt+v_txt)
		
		j+=1
	

	print("-" * (col_size+len(col_sizes)+1))

def view_sold_list():
	headers=["No","Name","Sold At","Qty"]
	table_view(headers,sold)
	menu(False)

def view_stock_list():
	headers=["No","Name","Price","Qty"]
	table_view(headers,stock)

	print("1. Sell Item")
	print("2. Main Menu")
	print("3. Search item")

	choice=""
	choice=input(">>:")
	if choice=="1":
		sell_item()
	elif choice == "2":	
		menu()
	elif choice == "3":	
		search()
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
	print("5. Search Stock List")
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
		elif choice =="5":
			search()
			break
		elif choice.upper() =="Q":
			
			break
		else: 
			print("Invalid Choice")
			


menu()
        
    

