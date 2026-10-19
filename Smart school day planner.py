day = input("which day is it today (Monday - Sunday):")
weather = input ("How is the weaher today? (Sunny/Cloudy/Rainy):")
homework = input ("Have you finished your homework? (yes/no):")
if day == "Monday":
    print ("Day type: Toady is the first day of the week.")
elif day in ("tuesday", "thursday", "wednesday"):
    print ("Day type: Today is a normal school day.")
elif day in ("Saturday", "Sunday"):
    print ("Day type: Today is a weekend.")
elif day == "Friday":
    print ("Day type: Today is the last school day.")
else :  
    print ("Day type: not recognised")

if homework == "yes" and weather == "Sunny":
    print ("You can go out to play.")
if weather in ("Cloudy","Rainy") or homework == "no":
    print ("You can't go out and play today.")
if not homework == "yes":
    print ("Stay indoors and complete your homework.")
if not homework == "yes" and weather in ("Cloudy", "Rainy"):
    print ("Best plan : You should stay indoors and complete your homework.")
elif not homework == "no" and weather == "Sunny":
    print ("Best plan : You are all set for a good school day.")

    