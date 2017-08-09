n = input("Enter any number")
r = 0
while(n>0):
    r = r*10+n%10
    n = n/10
    print "reverse number is", r