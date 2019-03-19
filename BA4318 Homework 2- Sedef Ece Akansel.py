#getting from the user number of points
number = int(input("Please enter number of coordinates there will be:" ))
#getting coordinates from user:
liste =[]
for point in range(0, number):
    point = input("Please enter coordinates with comma in between:").split(",")
    x = float(point[0])
    y = float(point[1])
    point = (x,y)
    liste.append(point)
print("The coordinates you have selected are:", liste)
#calculating center of mass:
n = len(liste)
sumx = 0
sumy = 0
for point in liste:
    sumx += point[0]
    sumy += point[1]
centerofmass = (sumx/n, sumy/n)
print("Center of mass is:", centerofmass)
x = sumx/n
y = sumy/n
#distance calculation
c = 0
liste2 = []
for distance in range(0, number):
    distance = ((liste[c][0]-x )**2+ (liste[c][1] - y)**2)**0.5
    liste2.append(distance)
    c +=1
print("Distances for each point from center of mass is", liste2)
#closest point
liste2.sort()
print("Closest distance from center of mass is", liste2[0], "Furthest distance from center of mass is", liste2[-1])