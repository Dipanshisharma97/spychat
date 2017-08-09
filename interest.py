p = input("Enter any principle amount")
t = input("Enter any time")
if (t>10):
    si = (p*t*10)/100
else:
    si = (p*t*15)/100
    print "Simple Interest = ",si