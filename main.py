import datetime as dt
from datetime import timedelta, date


class Library:
    def __init__(self):
        self.library = {}
        self.cart = {}
        self.count = 0
        self.library['Book1'] = {'Barcode': 101, 'Book_Title': 'Harry Potter', 'Author': 'J.K. Rowling', 'Genre': 'Fiction'}
        self.library['Book2'] = {'Barcode': 102, 'Book_Title': 'Game Of Thrones', 'Author': 'George R. R. Martin', 'Genre': 'Fantasy Fiction'}
        self.library['Book3'] = {'Barcode': 103, 'Book_Title': 'Tryst With Destiny', 'Author': 'Stanley Wolpert', 'Genre': 'Biography'}
        self.library['Book4'] = {'Barcode': 104, 'Book_Title': 'The Island Of The White Cow', 'Author': 'Deborah Tall', 'Genre': 'Travel'}
        self.library['Book5'] = {'Barcode': 105, 'Book_Title': 'The Alchemist', 'Author': 'Paula Coelho', 'Genre': 'Quest'}

    def menu(self):
        print("""
        ===== GBC Library =====
            1. Rent Book
            2. View Cart
            3. Find Book
            4. Checkout
            5. EXIT
        """)

        menu = int(input("Enter An Option: "))
        while 1 <= menu <= 5:
            if menu == 1:
                self.rent()
            elif menu == 2:
                self.view_book()
            elif menu == 3:
                self.find_book()
            elif menu == 4:
                self.receipt()
            elif menu == 5:
                exit(0)

    def rent(self):
        for books in self.library:
            print("\nBarcode: " + str(self.library[books]['Barcode']))
            print("Book Title: " + str(self.library[books]['Book_Title']))
            print("Author: " + str(self.library[books]['Author']))
            print("Genre: " + str(self.library[books]['Genre']))
        choice = int(input("\nPlease Enter Barcode To Rent A Book: "))
        while choice >= 101:
            if choice == 101:
                quantity = int(input("Enter Quantity: "))
                if not self.cart.get('Book1'):
                    self.cart['Book1'] = {'Barcode': 101, 'Book_Title': 'Harry Potter', 'Author': 'J.K. Rowling', 'Genre': 'Fiction', 'Quantity': int(quantity)}
                else:
                    self.cart['Book1']['Quantity'] += int(quantity)
            elif choice == 102:
                quantity = int(input("Enter Quantity: "))
                if not self.cart.get('Book2'):
                    self.cart['Book2'] = {'Barcode': 102, 'Book_Title': 'Game Of Thrones', 'Author': 'George R. R. Martin', 'Genre': 'Fantasy Fiction', 'Quantity': int(quantity)}
                else:
                    self.cart['Book2']['Quantity'] += int(quantity)
            elif choice == 103:
                quantity = int(input("Enter Quantity: "))
                if not self.cart.get('Book3'):
                    self.cart['Book3'] = {'Barcode': 103, 'Book_Title': 'Tryst With Destiny', 'Author': 'Stanley Wolpert', 'Genre': 'Biography', 'Quantity': int(quantity)}
                else:
                    self.cart['Book3']['Quantity'] += int(quantity)
            elif choice == 104:
                quantity = int(input("Enter Quantity: "))
                if not self.cart.get('Book4'):
                    self.cart['Book4'] = {'Barcode': 104, 'Book_Title': 'The Island Of The White Cow', 'Author': 'Deborah Tall', 'Genre': 'Travel', 'Quantity': int(quantity)}
                else:
                    self.cart['Book4']['Quantity'] += int(quantity)
            elif choice == 105:
                quantity = int(input("Enter Quantity: "))
                if not self.cart.get('Book5'):
                    self.cart['Book5'] = {'Barcode': 105, 'Book_Title': 'The Alchemist', 'Author': 'Paula Coelho', 'Genre': 'Quest', 'Quantity': int(quantity)}
                else:
                    self.cart['Book5']['Quantity'] += int(quantity)
            else:
                quantity = int(input("Please Enter A Valid Input: "))
            print("\nBook Successfully Added.")
            break

        print("\nPlease Enter A Valid Option.")
        self.return_menu()

    def view_book(self):
        if self.cart:
            for books in self.cart:
                print("\nBarcode: " + str(self.cart[books]['Barcode']))
                print("Book Title: " + str(self.cart[books]['Book_Title']))
                print("Author: " + str(self.cart[books]['Author']))
                print("Genre: " + str(self.cart[books]['Genre']))
                print("Quantity: " + str(self.cart[books]['Quantity']) + '\n')

        else:
            self.return_menu()

        self.return_menu()

    def find_book(self):
        book = str(input("Enter Book Title / Author / Genre or BACK To Return To Main Menu: "))
        for books in self.library:
            if book == self.library[books]['Book_Title'] or book == self.library[books]['Author'] or book == self.library[books]['Genre']:
                print("\nBarcode: " + str(self.library[books]['Barcode']))
                print("Book Title: " + str(self.library[books]['Book_Title']))
                print("Author: " + str(self.library[books]['Author']))
                print("Genre: " + str(self.library[books]['Genre']) + '\n')

                menu = int(input("Enter 1 To Search Again or 2 To Return To Main Menu: "))
                while menu > 0:
                    if menu == 1:
                        self.find_book()
                    elif menu == 2:
                        self.menu()
                    else:
                        menu = int(input("Please Enter A Valid Input. 1 To Checkout or 2 To Return To Main Menu: "))

            elif book.lower() == 'back':
                self.menu()

            else:
                book = int(input("\nITEM NOT FOUND.\nPress 1 To Try Again or 2 To Return To The Main Menu: "))
                while book > 0:
                    if book == 1:
                        self.find_book()
                    elif book == 2:
                        self.menu()
                    else:
                        book = int(input("Please Enter A Valid Input: "))

    def receipt(self):
        current = date.today().isoformat()
        if self.cart:
            file = open('Details.txt', 'w+')
            file.write('===== GBC Library =====')
            file.write('\n\tDate: ' + current)
            for books in self.cart:
                file.write("\n\nBarcode: " + str(self.cart[books]['Barcode']))
                file.write("\nBook Title: " + str(self.cart[books]['Book_Title']))
                file.write("\nAuthor: " + str(self.cart[books]['Author']))
                file.write("\nGenre: " + str(self.cart[books]['Genre']))
                file.write("\nQuantity: " + str(self.cart[books]['Quantity']) + '\n')
            file.write("\n\nYour Return Date Is 1 Week From Now: " + (date.today() + timedelta(days=7)).isoformat())
            print("\nYour Receipt Is Ready. Thank You.")
            file.close()
            exit(0)

        else:
            self.return_menu()

    def return_menu(self):
        menu = int(input('Press 1 To Add Items or 2 For Main Menu: '))
        while menu > 0:
            if menu == 1:
                self.rent()
            elif menu == 2:
                self.menu()
            else:
                menu = int(input("Please Enter A Valid Input: "))


gbc = Library()
gbc.menu()