guests = ['Albert Einstein', 'Marie Curie', 'Leonardo da Vinci']

for guest in guests:
    message = f"Dear {guest}, you are cordially invited to dinner. It would be an honor to have you join us."
    print(message)

print(f"\nUnfortunately, {guests[1]} cannot make it to dinner.\n")

guests[1] = 'Nikola Tesla'

for guest in guests:
    message = f"Dear {guest}, you are cordially invited to dinner. It would be an honor to have you join us."
    print(message)

print("\nGreat news! We found a bigger dinner table.\n")

guests.insert(0, 'Isaac Newton')
guests.insert(2, 'Galileo Galilei')
guests.append('Stephen Hawking')

for guest in guests:
    message = f"Dear {guest}, you are cordially invited to dinner. It would be an honor to have you join us."
    print(message)