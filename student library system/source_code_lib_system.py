class library:
    def __init__(self,book_list):
        self.books=book_list
    def display_books(self):
        for book in self.books:
            print("Available Books: ")
            print(book)
    def borrow_books(self,book_name):
        if book_name in self.books:
            print(f"You have borrowed {book_name}.Please return in 30 days.")
            self.books.remove(book_name)
        else:
            print(f"Your book is not available in our library.")
    def return_books(self,book_name):
        self.books.append(book_name)
        print(f"Thanks for returning {book_name}")
class Student:
    def request_book(self):
        Book=input("Enter the name of book you want to borrow. ")
        return Book
    def return_book(self):
        Book=input("Enter the name of book you want to return. ")
        return Book
def main():
    Library=library(["Peer e Kamil","Jannat ky Patty","Halim","Mushaf","Namal","A kite Runner","The Thousand Splendid Suns","Forty Rules of love"])
    student=Student()
    while True:
        print("---Student Library Management System----")
        print("1) Display Books ")
        print("2) Borrow Book ")
        print("3) Return Books ")
        print("4) Exit ")
        choice=(input("Enter choice(1-4): "))
        if choice=="1":
            Library.display_books()
        elif choice=="2":
            Book=student.request_book()
            Library.borrow_books(Book)    
        elif choice=="3":
            Book=student.return_book()
            Library.return_books(Book)
        elif choice=="4":
            print("Thanks for Visiting our library.")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()                        
        
        
        
        
    
     
        
                
                                
        
        