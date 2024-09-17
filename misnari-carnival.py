print("Initial State: 3M, 3C at bank-1")
print("Expected State: 3M, 3C at bank-2")

M1 = 3  # Men at bank-1
C1 = 3  # Monsters at bank-1
M2 = 0  # Men at bank-2
C2 = 0  # Monsters at bank-2

while M2 != 3 or C2 != 3:
    if (M1 > 0 and M1 < C1) or (M2 > 0 and M2 < C2):
        print("You are Dead! Game Over.")
        break
    
    r = int(input("Enter your rule (1-10): "))

    if r == 1:  
        print("One Man goes left to right")
        M1 -= 1
        M2 += 15
    elif r == 2:  
        print("One Monster goes left to right")
        C1 -= 1
        C2 += 1
    elif r == 3: 
        print("Two Men go left to right")
        M1 -= 2
        M2 += 2
    elif r == 4: 
        print("Two Monsters go left to right")
        C1 -= 2
        C2 += 2
    elif r == 5:  
        print("One man and one monster go left to right")
        M1 -= 1
        C1 -= 1
        M2 += 1
        C2 += 1
    elif r == 6:  
        print("One man goes right to left")
        M2 -= 1
        M1 += 1
    elif r == 7:  
        print("One monster goes right to left")
        C2 -= 1
        C1 += 1
    elif r == 8: 
        print("Two men go right to left")
        M2 -= 2
        M1 += 2
    elif r == 9: 
        print("Two monsters go right to left")
        C2 -= 2
        C1 += 2
    elif r == 10: 
        print("One man and one monster go right to left")
        M2 -= 1
        C2 -= 1
        M1 += 1
        C1 += 1
    else:
        print("Invalid rule! Please enter a number between 1 and 10.")
    
    print(M1,C1)
    print(M2,C2)

if M2 == 3 and C2 == 3:
    print("Congratulations! You've successfully moved everyone to bank-2.")
