#module for catalog. In this module the books or the authors name is searched and shown to the user.
import sys
class catalog:
    def searchbyname(self, library, book_name):
        for key,value in library.count_book_dict.items():
           if book_name in library.count_book_dict.keys():
                    print("The book is being searched.")
                    print("\n")
                    print("book_name: {},quantity ,author_name ,rack_number ,publish_date and number_of_page: {}".format(book_name,library.count_book_dict[book_name]))
                    print("\n")
                    print("Choose what you want to proceed")
                    choice = input("yes/no: ")
                    if choice == "yes":
                        break
                    else:
                        print("System exit")
                        sys.exit()
           else:
                print("Enter the book name available in our library")
                break

    
    def searchbyauthor(self, library, author):
        for key,value in library.count_book_dict.items():
            if author in value[1]:
                print("The book is being searched")
                print("\n")
                print("book_name: {},quantity ,author_name ,rack_number ,publish_date and number_of_page: {}".format(key,value))
                print("\n")
                print("If you want to proceed further then enter your choice")
                choice = input("yes/no: ")
                if choice == "yes":
                    break
                else:
                    print("System exit")
                    sys.exit()
        else:
            print("Enter the author name available in our library")

                
