guests = ['Albert Einstein', 'Marie Curie', 'Leonardo da Vinci']

for guest in guests:
    message = f"Dear {guest}, you are cordially invited to dinner. It would be an honor to have you join us."
    print(message)

print(f"\nUnfortunately, {guests[1]} cannot make it to dinner.\n")

guests[1] = 'Nikola Tesla'

for guest in guests:
    message = f"Dear {guest}, you are cordially invited to dinner. It would be an honor to have you join us."
    print(message)