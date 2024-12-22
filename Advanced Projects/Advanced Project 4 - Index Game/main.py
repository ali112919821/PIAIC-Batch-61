list = ["apple", "banana", "orange", "grape", "pineapple"]

print("--------------------------------")
print("Welcome to the Index Game!")
print("--------------------------------")

def accessing_elements(list):
    accessing_index = int(input("Enter the Accessing Index: "))
    if(accessing_index >= len(list) ):
        print("Index out of Range!")
    elif(list[accessing_index] in list):
        print(f"The value at given Index is: {list[accessing_index]}")


def modifying_elements(list):
    modifying_index = int(input("Enter the Modifying Index: "))
    new_value = input("Enter the New Value: ")
    if(modifying_index >= len(list)):
        print("Index out of Range!")
    else:
        list[modifying_index] = new_value
    print("\nUpdated List: ")
    print(list)


def slcing_elements(list):
    start_index = int(input("Enter Start Index: "))
    end_index = int(input("Enter End Index: "))
    if(((start_index < 0) or (start_index > len(list))) or ((end_index < 0) or (end_index > len(list)))):
        print("Indice out of Range!")
    else:
        print(list[start_index+1:end_index-1])



while(True):
    choice = input("\nSelect an operation (Access, Modify, Slice, Exit): ")
    print()
    match(choice.lower()):
        case "access":
            accessing_elements(list)
        case "modify":
            modifying_elements(list)
        case "slice":
            slcing_elements(list)
        case "exit":
            print("Exiting the Program....")
            break
        case _:
            print("Invalid Input!")

print(f"\nHere is the Final List: \n{list}\n")
