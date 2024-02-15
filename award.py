swim = input("How long was you swimming section?")
swim = int(swim)
cycle = input("How long was you cycling section?")
cycle = int(cycle)
run = input("How long was you running section?")
run = int(run)
total_time = swim + cycle + run
print("Your total time was " + str(total_time)) # Converted to a string so able to print sentence together.
# Conditions working from largest to smallest time as only 1 statement can be true at a time.
if total_time > 110:
    print("Unfortunately you did not qualify for an award. Try again next year!")
elif total_time > 105:
    print("Congratulations on a 'Provincial Scroll' award. Sign up for next year to improve your time by 5 to 10 minutes to qualify..")
elif total_time > 100:
    print("Congratulations on a 'Provincial Half Colours' award. Sign up for next year to improve your time by 5 minutes or less to qualify.")
elif total_time < 101:
    print("Congratulations qualifying! You have achieved the 'Provincial Colours' award. You are an inspiration to others!")
else:
    print("Error. check that you have etered your time in minutes as a whole number.")