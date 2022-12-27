import sys
from library import library
from User import member
from catalog import catalog          
library = library({"Anna Karenina":[6, "Leo Tolsty", "12H", 1878, 510], "To Kill a Mockingbird":[3, "Harper Lee", "12H", 1960, 475], "The Great Gatsby":[5, "F.Scott Fitzgerald", "12H", 1920, 337], "Don Quixote":[2, "Miguel de Cervantes", "12H", 1615, 337], "Beloved":[3, "Toni Morrison", "12H", 1987, 437],"Jane Eyre":[1, "Charlotte Bronte", "12H", 1847, 427]},"Library Management System of")
m1 = member("@bibas123","bibas123","bibas","bibasrai68@gmail.com","9982030680","NA","100")
catalog = catalog()
while(True):
    print("Welocome to {} library. Enter your choice".format(library.name))
    print("1","Display books")
    print("2","Borrow book")
    print("3","Return book")
    print("4","Pay fine")
    print("5","Find book by book name.")
    print("6","find book by author name.")
    print("\n")

    user_choice = input()
    if user_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Enter what you want from above \n")
        continue
    else:
        user_choice = int(user_choice)
        if user_choice == 1:
            print("The available books are available in {} library".format(library.name))
            library.display_books()
            print("\n")
        elif user_choice == 2:
            book = input("Enter name of the book you want to borrow: ")
            user = input("Enter your name: ")
            m1.lend_book(library, book, user)
            print("\n")

        elif user_choice == 3:
            book = input("Enter name of the book you want to return: ")
            user = input("Enter your name:")
            m1.return_book(library, book, user)
            print("\n")
        elif user_choice == 4:
            book = input("Enter name of the book for fine: ")
            user = input("Enter your name: ")
            m1.check_fine(library, book, user)
            print("\n")
            
        elif user_choice == 5:
            book_name = input("Enter name of the book: ")
            catalog.searchbyname(library, book_name)
            print("\n")
            
        elif user_choice == 6:
            author = input("Enter name of the author: ")
            catalog.searchbyauthor(library, author)
            print("\n")
            
             
        print("press q to quit or c to conitinue")
        choice = ""
        while(choice!= "c" and choice != "q"):
            choice = input()
            if choice == "c":
                continue
            elif choice == "q":
                sys.exit()

