import pyttsx3 as p

def Operation(opt, n1, n2):
    switcher = {
        "a": n1*n1,
        "b": n1/n2,
        "c": n1+n2,
        "d": n1-n2
        }
    return switcher.get(opt, "nothing")
p.speak("                  ")
p.speak("Hi, Whats Your Name?? Please Enter")
name = input("Your Name:")
p.speak("Nice to Meek You"+ name)
p.speak("I Am Under Development!! For now I can only do basic Calculations!")
j=1#To Implement Loop For spectific conditions! 
zeroError = int(0)#To Handle zero Error!
i=1 #To Implement Loop only first Time!
while True:
    if zeroError==1:
        p.speak("Please enter options again!")
    if i==1 and zeroError == 0 and j==1:
        i=0
        p.speak("So, How Can I Help You!"+ name)
        p.speak("These are the things I can help You with:")
        print("A. Multiply \nB. Division \nC. Summation \nD. Substraction")
        print("Please Enter From The Following Options!")
        p.speak("Please Enter Your Choice")
        opt = input("Your Choice:").lower()
    if j==0 and zeroError == 0:
        j=1
        p.speak("Please Enter From The Following Options, If You Again want to calculate!")
        print("A. Multiply \nB. Division \nC. Summation \nD. Substraction")
        opt = input("Your Choice:").lower()

    if opt == "a" and zeroError == 0 :
        p.speak("You Selected Multiplication:")
        p.speak("Please Enter two Numbers to multiply")
        optName = "Multiplication"
    elif opt == "b" and zeroError == 0:
        p.speak("You Selected Division:")
        p.speak("Please Enter two Numbers to divide")
        optName = "Division"
    elif opt == "c" and zeroError == 0:
        p.speak("You Selected Summation:")
        p.speak("Please Enter two Numbers to sum")
        optName = "Summation"
    elif opt == "d" and zeroError == 0:
        p.speak("You Selected Substraction:")
        p.speak("Please Enter two Numbers to substract")
        optName = "Substraction"
    elif zeroError == 0:
        j=0
        p.speak("You Entered a wrong Choice")
    zeroError =0
    if j==1 :
        n1 = float(input("First Number:"))
        if type(n1)== int or type(n1)==float:
            n2 = float(input("Secound Number:"))
        else:
            j=0
            p.speak("You Entered a Invalid Input, Try Again:(")
        if type(n2)!=int and type(n2)!=float :
            j=0
            p.speak("You Entered a Invalid Input, Try Again!")
        
        if(opt == "b" and n2 == 0):
            p.speak("You cannot divide by zero, deviding by zero is Not Defined")
            zeroError=int(1)
            continue
        result = float(Operation(opt, n1, n2))
        if result < 0:
            p.speak("So the Result of "+optName+" of "+ str(n1) + "and" + str(n2)+ "is" + "minus {:0.2f}".format(result))
        else:
            p.speak("So the Result of "+optName+" of "+ str(n1) + "and" + str(n2)+ "is" + "{:0.2f}".format(result))

        print("Your result is: "+ str(result))

        p.speak("so Wanna try Again!")
        exitOpt = input("If Yes Enter 'Y', else enter any key:")
        if(exitOpt.lower()=="y"):
            j=0
            continue
        else:
            p.speak("Thankyou For Using Me, Have a great Day"+ name+", Bye")
            break
