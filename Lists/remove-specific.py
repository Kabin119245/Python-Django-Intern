my_list = ["Kabin", "Dipesh", "Isha", "Kabin", "Nikita", "Aayush", "Kabin"]
element = "Kabin"

new_list = [x for x in my_list if x != element]

print("List after removing all occurrences of", element, ":", new_list)
