# Write a Python program that counts the number of vowels in
# a given string.
def count_vowels(string):
    
    vowels = "aeiouAEIOU"
    
    count = 0;
    
    for i in s:
        if (i in vowels):
            count += 1
    return count


s = input("Enter any string: ")
vc = count_vowels(s)
print(f"The number of vowels in string is: {vc}")
                