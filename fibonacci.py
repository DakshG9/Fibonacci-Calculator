a = True
print("Welcome to Daksh's Fibonacci Calculator")
print("Ctrl-c to exit")
while a == True:
    try:
        #Define a function
        
        absir = input("Enter a number: ")
        fibn = int(absir)
        def printFib():
            """Use calFib!!!!"""
            calFib()
                

        def calFib(a=0, b=1):
            """Redefine a and b to change the starting two numbers. Incorrect changement will result in errors. Calculates fibonacci. Lightweight."""
            if a < fibn:
                print(a)
                calFib(b, a+b)
        printFib()
    except ValueError:
        print("Oops. There was an error.\n(505)")
    except RecursionError:
        print("The value expected was too long.\n(505)")
        
