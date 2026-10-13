corn = 342
wheat = 400
barley = 300
kg = corn + wheat + barley
price = 35
earnings = kg*price
avg = kg/3
packet = 5
total_packs = kg//packet
leftover = kg % packet
print ("Farm Harvest Calculator \n")
print (kg)
print ("price ",end="= ")
print (price, "per kg")
print ("total number of packets =", total_packs)
print ("leftover =" , leftover)
kg +=15
print (kg)

