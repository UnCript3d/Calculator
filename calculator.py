class calculator:
    def start():
        startup=input("What operation will you like to do user? {+,-,/,*}")
        if startup=="+":
            x=int(input("Input your first number"))
            y=int(input("Input your secound number"))
            z=x+y
            print(z)

        elif startup=='-':
                x=int(input("Input your first number"))
                y=int(input("Input your secound number"))
                z=x-y

        elif startup=='/':
             x=int(input("Input your first number"))
             y=int(input("Input your secound number"))
             z=x/y
        elif startup=='*':
             x=int(input("Input your first number"))
             y=int(input("Input your secound number"))
             z=x*y
        else:
            print("Please give valid input")
                
calculator.start()            
