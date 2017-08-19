x=input("enter the value")
y=input("enter the value")
def divide(x,y):
    try:
        result=(x/y)
    except ZeroDivisionError:
        print "division by zero"
    else:
        print "result is ", result
    finally:
        print "executing finally clause"
divide(x,y)