# Exercise 6 - Library Management System in Python


# RULES

# Write a Library class with and books as two instance variables. Write a program to create
# a library from this Library class and show how you can print all books, add a book and get the number
# of books using different methods. Show that your program doesnt persist the books after the program
# is stopped! 






# Author: Ravi Shankar

class Library:
    def __init__(self,library_name):
        self.no_of_books = 0
        self.books = []
        self.library_name = library_name
    
    def addBook(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f'Library Name: {self.library_name}')
        print(f'\nBooks Quantity: {self.no_of_books}')
        print(f'\n BOOKS lIST: \n')
        for b in self.books:
            print(b,'\n')
        print('\n\n')



l1 = Library('Ravi Library')
l1.addBook('Harry Potter and the creatives')
l1.addBook('Business and Its Fundamentals')
l1.addBook('Journey To The YouTube')
l1.addBook('The House of The Dragons')
l1.showInfo()



l2 = Library('MG ROAD LIBRARY')
l2.addBook('The People and their Journey')
l2.addBook('The Mistakes Of Our 20s')
l2.addBook('Life And Its Hurdles')
l2.showInfo()

        
l3 = Library(library_name)
l2.addBook(book)


()