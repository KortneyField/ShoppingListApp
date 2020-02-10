
shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    print("Added: {} to thte list".format(len(shopping_list)))

def show_help():
    print("What should we pick up from the store? ")
    print("Enter 'DONE' to stop adding items")
    print("Enter 'HELP' to display help")
    print("Enter 'SHOW' to display your shopping list")

def show_list():
    print("Here is youre list:")
    for item in shopping_list:
        print (item)

show_help()
while True:
    new_item = input(":::  ")
    if new_item == "DONE":
        break;
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)
