import random
import math


print("             CHECK THE AVAILABLE BUSES AND CONTINUE YOUR JOURNEY")
travelagency={"Chennai-Madurai":854,"Madurai-Chennai":887,"Coimbatore-Chennai":530,"Bangalore-Chennai":710,"Salem-Madurai":325,"Chennai-Coimbatore":887,"Madurai-Coimbatore":470}

class Travel:

    def __init__(self):
        self.book=input("Enter the bus route:")

    def reserve(self):
        if(self.book.isnumeric()):
            tra_val=travelagency.values()
            if(int(self.book) in tra_val):
                paymentconfirmation()
            else:
                print("Error")
        
                

def paymentconfirmation():
    amount=int(input("Enter the Amount Rs.500:"))
    if(amount==500):
        key=otpgen()
        print("\n")
        value=int(input("Enter The Received OTP:"))
        print("\n")
        if(key==value):
            print("                       booking successful")
            print("\n")
        else:
            print("                       incorrect otp")
        cont=input("Do You Want To Continue yes/no?")
        print("\n")
        if(cont=='yes'):
            menu()
        else:
            print("""                 Thank You For Using travelling app                             """)
            exit()
    else:
        print("                       booking Failed")
        print("\n")
        j=input("Do You Want To Continue yes/no?")
        print("\n")
        if (j=='yes'):
            menu()
        else:
            print("""                 Thank You For Using travelling app                             """)
            exit()

def otpgen():
    otp=""
    digits="0123456789"

    for i in range(4):
        otp=otp+digits[math.floor(random.random()*10)]

    print("The OTP is:",otp)

    return (int(otp))



def viewavailable():
    for i,j in travelagency.items():
        print("         ",i," : ",j)

    print("\n")
    menu()


def menu():
    print("""
    1.Book
    2.Available
    3.Exit App
    """)
    pref=int(input("Enter The Number Of Your Preference:"))
    print("\n")
    if(pref==1):
        ps=Travel()
        ps.reserve()
    elif(pref==2):
        viewavailable()
    elif(pref==3):
        print("""                 Thank You For Using Travelling app                             """)
        exit()


menu()
