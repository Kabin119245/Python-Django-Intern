# Original string with leading and trailing spaces
text = "   Hello World   "

# Removing spaces from the left (beginning) only
left_trimmed = text.lstrip()
print("After lstrip(): '", left_trimmed, "'", sep='')

# Removing spaces from the right (end) only
right_trimmed = text.rstrip()
print("After rstrip(): '", right_trimmed, "'", sep='')

# Removing spaces from both sides (start and end)
fully_trimmed = text.strip()
print("After strip(): '", fully_trimmed, "'", sep='')
