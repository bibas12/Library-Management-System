from datetime import date,timedelta
class User:
    def __init__(self, username, password, user, email, mobile, address):
        self.username = username
        self.password = password
        self.user = user
        self.email = email
        self.mobile = mobile
        self.address = address
        
class member(User):
    def __init__(self, username, password, user, email, mobile, address, mber_id):
        super().__init__(username, password, user, email, mobile, address)
        self.mber_id = mber_id
        self.max_book_count = {}
        self.bookdict = {}
        
    def count_book(self, user, book):
        if user not in self.max_book_count:
            self.max_book_count[user] = [book]
            return len(self.max_book_count[user])
        else:
            if len(self.max_book_count[user]) <= 4:
                self.max_book_count[user].append(book)
                return len(self.max_book_count[user])
            else:
                return len(self.max_book_count[user])
            
    def lend_book(self, library, book, user):
    # giving the member the book they want
    # maintain the record inot the system   
            if book in library.count_book_dict.keys():
                if library.count_book_dict[book][0] >= 1:
                    if (book, user) not in self.bookdict.keys():
                        if not self.check_previous_fine(book, user):
                            if self.count_book(user, book) <= 5:
                                lend_date = date.today()
                                return_date = date.today() + timedelta(days = 10)
                                self.bookdict.update({(book, user):return_date})
                                library.count_book_dict[book][0] -= 1
                                for value in self.bookdict.keys():
                                    if value == (book, user):
                                        print("{} book is issued to your name {} on {}. the book can be lended".format(value[0], value[1], lend_date))
                                        print("Please read the book under 10 days. If you exceed the deadline fine should be paid.")
                                        print(self.max_book_count)
                            else:
                                print("The maximum number of books that a member can issue is 5.")
                        else:
                            print("Only after paying the fine the member can issue other books.")
                    else:
                        print("The book that the member wants to issue is already issued.")
                else:
                    print("The desired book is out of stock.")
            else:
                print("The book issued is not in the library.")


    # checking if the member has any fine left or not        
    def check_previous_fine(self ,book, user):
        current_date = date.today()
        for key,value in self.bookdict.items():
            if key[1] == user:
                return_date = self.bookdict[key]
                if current_date > return_date:
                    delay_days = (current_date - return_date).days
                    total_fine = delay_days*10
                    return total_fine
                else:
                    return 0 
                
    def return_book(self, library, book, user):   
    # return book,updating records and if dealy then charge fine 10rs/day.
        if (book, user)in self.bookdict.keys():
            return_date =  self.bookdict[(book, user)]
            current_date = date.today()
            if current_date > return_date:
                delay_days = (current_date - return_date).days
                total_fine = delay_days*10
                print("The fine to be paid: {} rupess" .format(total_fine))
                print("Redirecting to payment:")
                self.payment(library, book, user)
            else:
                self.max_book_count[user].remove(book)
                self.bookdict.pop((book, user))
                library.count_book_dict[book][0] += 1
                print("Book returned.")
        else:
            print("Please enter correct username and book name.")
            
    # payment process        
    def payment(self, library, book, user):
        print("PLease choose yes if you want to pay the fine: ")
        choice = input("yes/no: ")
        if choice == "yes":
            print("Payment is being processed:")
            print("Payment successful:")
            self.max_book_count[user].remove(book)
            self.bookdict.pop((book, user))
            library.count_book_dict[book][0] += 1
        else:
            print("Redirecting to home")
            
    #checking whether the fine to be paid is there or not      
    def check_fine(self, library, book, user):
        if (book,user)in self.bookdict.keys():
            return_date =  self.bookdict[(book, user)]
            current_date = date.today()
            if current_date > return_date:
                delay_days = (current_date - return_date).days
                total_fine = delay_days*10
                print("The fine to be paid: {} rupess" .format(total_fine))
                print("Do want to procced the payment:")
                choice = input("yes/no")
                if choice == "yes":
                    self.payment(library, book, user)
                else:
                    print("Redirecting to home")
            else:
                print("No fine record to be paid.")
        else:
            print("Enter correct information")
