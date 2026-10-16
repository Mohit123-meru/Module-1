temp = int(input("What is the temperature today:"))
if temp < 20:
    print ("Wear a jacket")
else:
    print ("wear a T-Shirt")
rain = input("Is it Raining or not:")
if rain == "yes":
    print ("Use an Umbrella")
else:
    print ("You don't need an umbrella") 
wind = int(input("What is the Wind speed:"))
if wind > 40:
    print ("It is very windy today", end = ".")
    print ("Use a wind breaker.")
else:
    print ("It is very calm today", end = ".")
    print ("You don't need a Wind breaker")
