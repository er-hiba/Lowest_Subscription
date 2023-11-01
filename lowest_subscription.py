# Function to calculate the cost of different subscription offers based on monthly call duration
def cost(X):
    List = []

    # Calculate cost for the 0DH offer (2DH per minute, no free minutes)
    B0 = X * 2
    List.append(B0)

    # Calculate cost for the 20DH offer with 30 minutes of free calls and additional charges (1.5DH per minute)
    if X > 30:
        B20 = 20 + (X-30) * 1.5
    else:
        B20 = 20
    List.append(B20)

    # Calculate cost for the 50DH offer with 60 minutes of free calls and additional charges (1DH per minute)
    if X > 60:
        B50 = 50 + (X-60) * 1
    else:
        B50 = 50
    List.append(B50)

    # Calculate cost for the 100DH offer with 120 minutes of free calls and additional charges (0.5DH per minute)
    if X > 120:
        B100 = 100 + (X-120) * 0.5
    else :
        B100 = 100
    List.append(B100)

    return List

# Main program

X = float(input("Enter the total call duration for the month in minutes: "))
List = cost(X)

# Display the total cost for different subscription offers
print("The total cost to pay at the end of the month for subscription offers 0DH, 20DH, 50DH, 100DH:")
print(List)

Min = List[0]
for i in range(0, 4):
    if Min > List[i]:
        Min = List[i]

# Check if the lowest cost offer is one of the monthly subscriptions (0DH, 20DH, 50DH, 100DH) or the 200DH offer
if Min > 200:
    print("The lowest cost offer is the 200DH monthly subscription.")
else :
    offer = List.index(Min)
    print("The lowest cost offer is offer number", offer+1)
