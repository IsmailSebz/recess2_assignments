stock =[
		{"name":"Muwogo","price":"20000"},
		{"name":"rice","price":"300000"}
	]
x={"name":"Muwogo","price":"1"}
y=None
try: 
    y=int(x["price"])
except: ValueError

print(isinstance(y, int))

# for item in stock:
#     for k,v in item.items():
#         print(k)