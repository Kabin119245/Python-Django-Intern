str = '"How can I find out who yelled, Fire! in the theater?" and then didnot wait to hear Missy give the answer---"John Tracy."'
print("--------------Before removing punctutation---------")
print(str)
print("--------------After removing punctutation---------")
clean_str = ''.join(char for char in str if char.isalnum() or char.isspace())
print(clean_str)