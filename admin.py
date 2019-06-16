from sq import managemovie
from sq import customerdetail
def admin():
    admin_psswrd=int(input("enter the admin password:\n"))
    print("***********")
    if admin_psswrd==9539479356:
        print("1.Manage the Movie details")
        print("2.View details of our customers")
        print("3.Exit")
        admin_input=int(input("Enter ur choice:"))
        if admin_input==1:
            managemovie()
        elif admin_input==2:
            customerdetail()
        elif admin_input==3:
            print("Thankuu!!")
        else:
            print("Invalid choice!!")
    else:
        print("U entered the wrong password.try again!!")