# Remove square brackets from a List in Python

# ✅ remove square brackets from a list of Strings
list_of_strings = ['bobby', 'hadz', 'com']

result = ', '.join(list_of_strings)
print(result)  # 👉️ bobby, hadz, com

# ---------------------------------------------

# ✅ remove square brackets from a list of Integers
list_of_numbers = [44, 22, 66]

result = ', '.join(str(item) for item in list_of_numbers)
print(result)  # 👉️ 44, 22, 66