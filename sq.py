import sqlite3
dbase=sqlite3.connect("booking.db")
cursor=dbase.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS user_details(
              ID      INT     PRIMARY KEY      NOT NULL,
              NAME    TEXT                     NOT NULL,
              PHONENO INT                      NOT NULL,
              FILM    TEXT                     NOT NULL,
              THEATRE TEXT                     NOT NULL) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS movie_details(
              SLNO         INT    PRIMARY KEY     NOT NULL,
              THETRE_NAME  TEXT                   NOT NULL, 
              MOVIE1       TEXT                   NOT NULL,
              MOVIE2       TEXT                   NOT NULL,
              MOVIE3       TEXT                   NOT NULL)''')

def bookticket():
    print("We have services on the following theatres")
    thetres=cursor.execute('''SELECT THETRE_NAME from movie_details''')
    a=["1","2","3","4","5"]
    i=1
    for record in thetres:
        print(str(i)+".",record[0])
        i+=1
        
    
    thetre_choice=input("enter ur choice:")
    if thetre_choice not in a:
        print("S orry u entered the invalid choice")
    else:
        movies=cursor.execute('''SELECT MOVIE1,MOVIE2,MOVIE3 from movie_details WHERE SLNO=?''',thetre_choice)
        print("Here are ur movies")
        list2=[1,2,3]
        for record in movies:
            print ("1."+record[0])
            print ("2."+record[1])
            print ("3."+record[2])
            movie_choice=int(input("Enter ur choice:"))
            if movie_choice not in list2:
                print("Sorry!!U enterd the invalid choice!!")
            else:
                movie=movie_choice-1
                user_name=input("enter ur name:")
                user_no=input("Enter ur no.:")
                string=str(user_no)
                identity=string[9]
                movie_index=dbase.execute('''SELECT  * from movie_details WHERE SLNO=?''',(thetre_choice))
                movie_name=record[movie]
                thetre_index=cursor.execute('''SELECT THETRE_NAME from movie_details WHERE SLNO=?''',(thetre_choice))
                for record in thetre_index:
                    thetre_name=record[0]
                cursor.execute('''INSERT INTO user_details(ID,NAME,PHONENO,FILM,THEATRE) VALUES(?,?,?,?,?)''',(identity,user_name,user_no,movie_name,thetre_name))
                dbase.commit()
                print("***************\n")
                print("Ur ticket is booked\n")
                print("Enjoy ur dayy!!\n")
                print("Ur ticket id is",identity)
                print("Please keep ur ticket id safe ")
                print("Thank uu!!")
    
    
def viewticket():
     print("Heyy!!Welcome again to the Movie ticket booking system\n")
     print("We need ur ticket id to view ur booked ticket details.Hope its with u!!!\n")
     ticket_id=input("Please enter ur ticket ID:")
     ticket_detail=dbase.execute("""SELECT * FROM user_details WHERE ID=?""",ticket_id)
     for record in ticket_detail:
         print("***********")
         print("Ticket ID:",record[0])
         print("Name:",record[1])
         print("Phone no:",record[2])
         print("Theatre:",record[4])
         print("Movie:",record[3])
         print("***********")
         print("Thankuu!!")
         
        
def editticket():
    ticket_id=input("Enter ur id:")
    print("Here is ur ticket details")
    ticket_detail=dbase.execute("""SELECT * FROM user_details WHERE ID=?""",ticket_id)
    for record in ticket_detail:
         print("***********")
         print("Ticket ID:",record[0])
         print("Name:",record[1])
         print("Phone no:",record[2])
         print("Theatre:",record[4])
         print("Movie:",record[3])
    print("**************")
    print("What u want to edit??")
    print("1.Name")
    print("2.Theatre")
    print("3.Phone no.")
    edit_choice=int(input("Enter ur choice:"))
    if edit_choice==1:
        new_name=input("Enter the name:")
        cursor.execute('''UPDATE user_details set NAME=? WHERE ID =?''',(new_name,ticket_id))
        dbase.commit()
        print("Name is changed successfully ")
        print("Thank uu!!")
        
        
    elif edit_choice==2:
        
       thetres=cursor.execute('''SELECT THETRE_NAME from movie_details''')
       a=[1,2,3,4,5]
       i=1
       for record in thetres:
           print(str(i)+".",record[0])
           i+=1
       newtheatre_choice=input("Enter ur choice:")
       theatres=cursor.execute('''SELECT THETRE_NAME FROM movie_details WHERE SLNO=?''',newtheatre_choice)
       for record in theatres:
           newtheatre_name=record[0]
       movies=cursor.execute('''SELECT MOVIE1,MOVIE2,MOVIE3 from movie_details WHERE SLNO=?''',newtheatre_choice)
       print("Here are ur movies")
       list2=[1,2,3,4,5]
       for record in movies:
           print ("1."+record[0])
           print ("2."+record[1])
           print ("3."+record[2])
       movie_choice=int(input("Enter ur choice:"))
       movie=movie_choice-1
       movie_index=dbase.execute('''SELECT  * from movie_details WHERE SLNO=?''',(newtheatre_choice))
       newmovie_name=record[movie]
       cursor.execute('''UPDATE user_details set THEATRE=? WHERE ID =?''',(newtheatre_name,ticket_id))
       dbase.commit()
       cursor.execute('''UPDATE user_details set FILM=? WHERE ID=?''',(newmovie_name,ticket_id))
       dbase.commit()
       print("Theatre is changed successfully ")
       print("Thank uu!!")
    
    elif edit_choice==3:
        new_phoneno=input("Enter the Number:")
        cursor.execute('''UPDATE user_details set PHONENO=? WHERE ID =?''',(new_phoneno,ticket_id))
        dbase.commit()
        print("Phone number is changed successfully ")
        print("Thank uu!!")
    else:
        print("U entered the invalid choice")
        
        
def cancelticket():
    userid=input("Enter ur ticket ID:")
    user_confirm=input("Are u sure u want to cancel ticket?Y/N:")
    if user_confirm=="Y" or "y":
        cursor.execute('''DELETE  from user_details WHERE ID=?''',userid)
        dbase.commit()
        print("Ur ticket is cancelled!!")
        print("Thank uu!!")
    
def managemovie():
     theatre_id=input("Enter the theatre ID:")
     print("Here are ur selected movies")
     theatre_details=cursor.execute('''SELECT MOVIE1,MOVIE2,MOVIE3 FROM movie_details WHERE SLNO=?''',theatre_id)
     for record in theatre_details:
         print("1.",record[0])
         print("2.",record[1])
         print("3.",record[2])
     admin_confirm=input("Do u want to update ur movie list? Y/N:")
     if admin_confirm=="Y"or"y":
         new_movie=input("Enter the new movie:")
         
         cursor.execute('''UPDATE movie_details set MOVIE1= ? WHERE SLNO=?''',(new_movie,theatre_id))
         dbase.commit()
         print('Ur movie list is updated')
         print('Thank u for ur service.')  
     else:
        print("Thank u for ur service")
        
        
def customerdetail():
    theatre_id=input("Enter ur theatre ID:")
    theatre_names=cursor.execute('''SELECT THETRE_NAME FROM movie_details WHERE SLNO=?''',theatre_id)
    for record in theatre_names:
        theatre_name=record[0]
        
    user_detail=cursor.execute('''SELECT * FROM  user_details WHERE THEATRE=?''',(theatre_name,))
    for record in user_detail:
        print("***********")
        print("ID:",record[0])
        print("Name:",record[1])
        print("Number:",record[2])
        print("Movie:",record[3])
        print("************")
        
        
        
    
    
    
         
         
    
     
    