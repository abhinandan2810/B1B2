my_list = []
n = int(input("How many elements do you want to add to the list? "))

for _ in range(n):
    element = input("Enter an element to append: ")
    my_list.append(element)

print("The final list is:", my_list)
