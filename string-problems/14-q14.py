string1 = input("Enter the first string: ").strip().lower()
string2 = input("Enter the second string: ").strip().lower()

if sorted(string1) == sorted(string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")

