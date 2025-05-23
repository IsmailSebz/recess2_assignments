people =[]
print("Enter number of people to add to the list")
num = input(">>")
try:
    num = int(num)
except ValueError:
    print("Value error")
for i in range(num):
    people.append(input(f"#{i+1}>>"))
print(people)

##ASSINMENT 2: CHANGING THE NAME OF THE FIRST ELEMENT
print("=============================================")
print(f"Enter the name to replace {people[0]}")
people[0]=input(">>:")

print(people)