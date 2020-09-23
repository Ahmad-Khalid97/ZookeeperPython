# Save the input in this variable
ticket = input()


# Add up the digits for each half
half1 = sum(int(i) for i in ticket[:3])
half2 = sum(int(j) for j in ticket[3:])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")