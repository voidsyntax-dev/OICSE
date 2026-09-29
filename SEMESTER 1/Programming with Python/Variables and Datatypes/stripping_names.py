name = "  \tNew\nUser\t  "

# Display the name with whitespace
print("Name with whitespace displayed:")
print(repr(name))

# Strip from the left
print("\nUsing lstrip():")
print(repr(name.lstrip()))

# Strip from the right
print("\nUsing rstrip():")
print(repr(name.rstrip()))

# Strip from both ends
print("\nUsing strip():")
print(repr(name.strip()))