name = input("Enter your name: ")
print(f"---WELCOME TO THE MANWHA LIST MAKER, {name}---")

manwha_list = []
while True:#hellue
    manwha = input("Enter the title of the Manwha you want to add [type 'exit' to stop]: ")
    if manwha.lower() == 'exit':
        break
    manwha_list.append(manwha)
    print(f"'{manwha}' has been added to the list. Continue.")

else:
    print("Error!")#JBS

print(f"\nManwha List of {name.upper()}:")
for i in range(1, len(manwha_list)+ 1):
    print(f" {i} - {manwha_list[i - 1]}")
print("Thank You for using the Manwha List Maker!, Come back again next time!!")#JBS