from user import user
from admin import admin
print('Heyy!!Welcome to the Movie Ticket Booking System!Happy weekend!!')
print("1.User")
print("2.Admin")
login_choice=int(input("Please Enter ur Login Option:"))
if login_choice==1:
   user()
elif login_choice==2:
    admin()
else:
    print(" Oops Inavalid Option!!")
    