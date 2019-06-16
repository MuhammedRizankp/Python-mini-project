from sq import viewticket
from sq import editticket
from sq import cancelticket
from sq import bookticket
def user():
    print("1.Book my ticket")
    print("2.View my ticket details")
    print("3.Edit my details")
    print("4.Cancel my ticket")
    print("5.Exit")
    user_choice=int(input("Enter ur choice:"))
    if user_choice==1:
       bookticket()
    elif user_choice==2:
        viewticket()
    elif user_choice==3:
        editticket()
    elif user_choice==4:
        cancelticket()
    elif user_choice==5:
         print("Thankuu!!")
    else:
        print("Sorry u entered invalid choice")
        