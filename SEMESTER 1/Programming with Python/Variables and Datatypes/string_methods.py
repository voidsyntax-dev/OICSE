s = "Hello, World!"

# Add tab whitespace using \t
s = "\t" + s + "\t"
print(repr(s))

# 1. strip() - Remove leading and trailing whitespace
print(s.strip())

# 2. upper() - Convert to uppercase
print(s.upper())

# 3. lower() - Convert to lowercase
print(s.lower())

# 4. title() - Convert to title case
print(s.title())

# 5. capitalize() - Capitalize first letter
print(s.capitalize())

# 6. replace() - Replace a substring
print(s.replace("World", "Python"))

# 7. split() - Split into a list
print(s.split(","))

# 8. join() - Join list elements
words = ["Hello", "World"]
print(",".join(words))

# 9. find() / index() - Find substring position
print(s.find("World"))

# 10. count() - Count occurrences
print("o".count("o"))

# 11. concat() / + - String concatenation
concatenated = s + " " + "This is Python!"
print(concatenated)