'''
This is an application to view my SQL database, insert information, update information. Matthew Thomas 27/05/24
'''
#Importing Modules
import sqlite3
from time import sleep
from datetime import date
import glob

#Code to locate correct file name for Database
files = glob.glob('books.db')
#Intializing variables
DATABASE = files[0]
admin = False
#If the code does not work, It is likely an error with the database location, please ensure the database in the same directory as the this file!
user_input = None

#Defining Functions
def search_for_books_by_an_author():
    """Function to filter the database by an author provided by the user based on the author table"""
    valid_ids = []
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Show All Author Information
    query1 = "SELECT * FROM author;"
    cursor.execute(query1)
    author_table = cursor.fetchall()
    print("| ID  | Author Name                                       |")
    print("-----------------------------------------------------------")
    for author in author_table:
        print(f"| {author[0]:<4}| {author[1]:<50}|")
    print("-----------------------------------------------------------")
    print("| ID  | Author Name                                       |")
    #Generates a list of valid ids from the database
    for i in author_table:
        valid_ids.append(i[0])

    #Loop to gather the user input, the id of the author
    while True:
        try:
            id = int(input("Please enter the id of the author who's books you want to view! "))
            if id in valid_ids:
                query2 = f"SELECT book.name, author.name FROM book JOIN author ON author.id = book.author WHERE author.id = {id} ORDER BY book.name ASC"
                cursor.execute(query2)
                results = cursor.fetchall()
                #Print out the Results
                print("| Book Title                                        | Author Name         |")
                print("---------------------------------------------------------------------------")
                for data in results:
                    print(f"| {data[0]:<50}| {data[1]:<20}|")
                print("---------------------------------------------------------------------------")
                print("| Book Title                                        | Author Name         |")
                print("---------------------------------------------------------------------------")
                db.close()
                break
            else:
                #Returns an error message if the id does not exist in the database
                print("That id is not in the database, please try again")
                continue
        except ValueError:
            #Returns an error message if the user input was not an integer
            print("Your input was not an integer, please try again")
            continue
def search_by_wordcount_return_title_author_genre_wordcount():
    """Function to display the book, author, genre, and word count of books with more or less words than a user input"""
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    more_or_less = ['>=', '<=']
    #More or Less and integer Gatherer
    while True:
        more_less = input("Would you like to search for books with more or less words than a given word count? (more/less) ").lower()
        #SQL Statement converter
        if more_less == "more" or more_less == "less":
            if more_less == "more":
                more_less = more_or_less[0]
            if more_less == "less":
                more_less = more_or_less[1]
            break
        else:
            #Error Message
            print("Your input was not the word more or the word less. This is not casesensitive. Please try again!")

    #Word Count Generator
    while True:
        try:
            word_count = int(input("Please enter the word count you would like to filter by! "))
            if word_count <= 0:
                print("You input was negative, you can't have a negative number of words, or zero for that matter.")
                continue
            else:
                break
        except ValueError:
            print("It appears that your word count was not an integer, please try again!")
    
    #Query formatting, execution, and result printing
    query = f"SELECT book.name, author.name, genre.genre, book.word_count FROM book JOIN author on author.id = book.author JOIN genre on genre.id = book.genre WHERE book.word_count {more_less} {word_count} ORDER BY book.word_count DESC"
    cursor.execute(query)
    results = cursor.fetchall()
    if len(results) == 0:
        print("It appears there was no data!")
    else:
        print("| Book Title                                        | Author Name         | Genre       | Word Count  |")
        print("-------------------------------------------------------------------------------------------------------")
        for data in results:
            print(f"| {data[0]:<50}| {data[1]:<20}| {data[2]:<12}| {data[3]:<12}|")
        print("-------------------------------------------------------------------------------------------------------")
        print("| Book Title                                        | Author Name         | Genre       | Word Count  |")
        print("-------------------------------------------------------------------------------------------------------")
    db.close()
def search_by_pagecount():
    """Function to display the book, author, genre, and page count of books with more or less pages than a user input"""
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    more_or_less = ['>=', '<=']
    #More or Less and integer Gatherer
    while True:
        more_less = input("Would you like to search for books with more or less pages than a given page count? (more/less) ").lower()
        #SQL Statement converter
        if more_less == "more" or more_less == "less":
            if more_less == "more":
                more_less = more_or_less[0]
            if more_less == "less":
                more_less = more_or_less[1]
            break
        else:
            #Error Message
            print("Your input was not the word more or the word less. This is not casesensitive. Please try again!")

    #Page Count Generator
    while True:
        try:
            pages = int(input("Please enter the page count you would like to filter by! "))
            if pages <= 0:
                print("You input was negative, you can't have a negative number of pages, or zero for that matter.")
                continue
            else:
                break
        except ValueError:
            print("It appears that your page count was not an integer, please try again!")
    
    #Query formatting, execution, and result printing
    query = f"SELECT book.name, author.name, genre.genre, book.pages FROM book JOIN author on author.id = book.author JOIN genre on genre.id = book.genre WHERE book.pages {more_less} {pages} ORDER BY book.word_count DESC"
    cursor.execute(query)
    results = cursor.fetchall()
    if len(results) == 0:
        print("It appears there was no data!")
    else:
        print("| Book Title                                        | Author Name         | Genre       | Page Count  |")
        print("-------------------------------------------------------------------------------------------------------")
        for data in results:
            print(f"| {data[0]:<50}| {data[1]:<20}| {data[2]:<12}| {data[3]:<12}|")
        print("-------------------------------------------------------------------------------------------------------")
        print("| Book Title                                        | Author Name         | Genre       | Page Count  |")
        print("-------------------------------------------------------------------------------------------------------")
    db.close()
def book_names_and_page_count_and_author_and_genre_pages_less_than_333():
    '''Function to display all the books, their page counts, author, and genre, where there are less than 333 pages'''
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, book.pages, author.name, genre.genre FROM book JOIN author ON author.id = book.author JOIN genre ON genre.id = book.genre WHERE pages < 333 ORDER BY book.pages DESC"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print("| Book Title                                        | Page Count  | Author Name         | Genre          |")
    print("----------------------------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<12}| {data[2]:<20}| {data[3]:<15}|")
    print("----------------------------------------------------------------------------------------------------------")
    print("| Book Title                                        | Page Count  | Author Name         | Genre          |")
    print("----------------------------------------------------------------------------------------------------------")
    db.close()
def book_names_and_authors_and_genres():
    '''Function to display all the books, their authors, and their genre'''
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, author.name, genre.genre FROM book JOIN author ON author.id = book.author JOIN genre ON genre.id = book.genre ORDER BY genre.genre ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print("| Book Title                                        | Author Name         | Genre       |")
    print("-----------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<20}| {data[2]:<12}|")
    print("-----------------------------------------------------------------------------------------")
    print("| Book Title                                        | Author Name         | Genre       |")
    print("-----------------------------------------------------------------------------------------")
    db.close()
def book_names_and_authors_and_release_date():
    '''Function to display all the books, their authors, and their release date'''
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, author.name, book.release_date FROM book JOIN author ON author.id = book.author ORDER BY book.release_date ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print("| Book Title                                        | Author Name         | Release Date   |")
    print("--------------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<20}| {data[2]:<14}|")
    print("--------------------------------------------------------------------------------------------")
    print("| Book Title                                        | Author Name         | Release Date   |")
    print("--------------------------------------------------------------------------------------------")
    db.close()
def book_names_and_author_and_general_reviews():
    '''Function to display all the books, their authors, and their general review average'''
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, author.name, book.review FROM book JOIN author ON author.id = book.author ORDER BY book.name ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print("Note: Reviews are on a scale from 1 to 5.")
    print("| Book Title                                        | Author Name         | Reviews |")
    print("-------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<20}| {data[2]:<8}|")
    print("-------------------------------------------------------------------------------------")
    print("| Book Title                                        | Author Name         | Reviews |")
    print("-------------------------------------------------------------------------------------")
    db.close()
def book_names_and_isbn_13_classification_and_release_date():
    '''Function to display all the books, their isbn-13 classification, and their release date'''
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, book.isbn, book.release_date FROM book ORDER BY book.release_date ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print("| Book Title                                        | ISBN          | Release Date |")
    print("------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<14}| {data[2]:<13}|")
    print("------------------------------------------------------------------------------------")
    print("| Book Title                                        | ISBN          | Release Date |")
    print("------------------------------------------------------------------------------------")
    db.close()
def search_for_books_released_in_a_year():
    '''Function to display book titles, authors, and release dates based on a used input of a year'''
    search_query = None
    while True:
        try:
            search_query = int(input("Enter which year's book releases you would like to view! (Positive Numbers Only Please!) "))
            if search_query <= 0:
                search_query = 0
                print("Please enter a positive whole number")
                search_for_books_released_in_a_year()
                continue
        except ValueError:
            print("Please enter a series of positive whole numbers")
        #Establish Interface
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        #Execute and Fetch Data, Sorting by the year provided
        query = f"SELECT book.name, author.name, book.release_date FROM book JOIN author ON author.id = book.author WHERE release_date LIKE '{search_query}/%'"
        cursor.execute(query)
        results = cursor.fetchall()
        #Print out the Results
        if len(results) != 0:
            print("| Book Title                                        | Author              | Release Date |")
            print("------------------------------------------------------------------------------------------")
            for data in results:
                print(f"| {data[0]:<50}| {data[1]:<20}| {data[2]:<13}|")
            print("------------------------------------------------------------------------------------------")
            print("| Book Title                                        | Author              | Release Date |")
            print("------------------------------------------------------------------------------------------")
        else:
            print("It appears there was no data for that year!")
        db.close()
        break
def add_data_to_genre_table():
    """Function to Insert a Genre Into the Genre Table"""
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Show the existing genres and establish the target id for
    query1 = "SELECT * FROM genre;"
    cursor.execute(query1)
    genre_table = cursor.fetchall()
    print("| ID  | Genre          |")
    print("------------------------")
    for genre in genre_table:
        print(f"| {genre[0]:<4}| {genre[1]:<15}|")
    print("------------------------")
    print("| ID  | Genre          |")
    target_id = genre_table[-1][0] + 1
    #Gather, Format, and Sanatise Input
    sanatiser = []
    sanatiser.append(input("Insert a Genre to add to the a Genre Table \n").title())
    #Enter Data
    query2 = f"INSERT INTO genre (id, genre) VALUES ({target_id}, '{sanatiser[0]}')"
    cursor.execute(query2)
    #Finalise Insertion
    db.commit()
    print("Sucessfully added to the database!")
    db.close()
def add_data_to_author_table():
    """Function to Insert an Author into the Author Table"""
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Show the existing author and establish the target id for
    query1 = "SELECT * FROM author;"
    cursor.execute(query1)
    author_table = cursor.fetchall()
    print("| ID  | Author Name                                       |")
    print("-----------------------------------------------------------")
    for author in author_table:
        print(f"| {author[0]:<4}| {author[1]:<50}|")
    print("-----------------------------------------------------------")
    print("| ID  | Author Name                                       |")
    target_id = author_table[-1][0] + 1
    #Gather, Format, and Sanatise Input
    sanatiser = []
    sanatiser.append(input("Insert an Author to add to the a Author Table \n").title())
    #Enter Data
    query2 = f"INSERT INTO author (id, name) VALUES ({target_id}, '{sanatiser[0]}')"
    cursor.execute(query2)
    #Finalise Insertion
    db.commit()
    print("Sucessfully added to the database!")
    db.close()
def add_data_to_book_table():
    """Function to Insert a Book and all its Correlating Information to the Book table"""
    #Establish Interface and Storage
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    data = []
    polarity = ["Y", "N"]

    #Gather Id Information
    id_query = "SELECT MAX(id)+1 FROM book"
    cursor.execute(id_query)
    id_deterimnant = cursor.fetchall()
    next_id = id_deterimnant[0][0]

    #Book Title
    title = input("Please insert the title of the book you would like to enter!\n")
    data.append(title)

    """Subset Function to Gather Author"""
    #Establish and Show Author Table for Refrence
    query1 = "SELECT * FROM author;"
    cursor.execute(query1)
    author_table = cursor.fetchall()
    generated_author_id = author_table[-1][0] + 1
    print("| ID  | Author Name                                       |")
    print("-----------------------------------------------------------")
    for author in author_table:
        print(f"| {author[0]:<4}| {author[1]:<50}|")
    print("-----------------------------------------------------------")
    print("| ID  | Author Name                                       |")
    while True:
        #Loop to Gather Author Information
        #Checks where the author information will come from, adding an author or refrencing an existing author
        gatherer = input("Is the author you want to enter in the table above? (Y/N) ") 
        if gatherer not in polarity:
            #Checks if the Yes/No input is Valid
            print("That input is invalid, please try again!")
            continue
        elif gatherer == "Y":
            #If the input is Yes, Request the numerical id of the author and check that it is a valid range
            try:
                author_id = int(input("Please enter the numerical id of the author who wrote the book you are entering data for, this can be found in the above table! "))
                if author_id <= generated_author_id and author_id > 0:
                    data.append(author_id)
                    break
                else:
                    #If value is outside the valid range, return an error and request info again
                    print("That id is not in the Table")
                    continue
            except ValueError:
                #If the input is not an integer, return an error and request info again
                print("That is an invalid input")
                continue
        elif gatherer == "N":
            #Redirect the user to the function to add an author to the table and use the generated id
            print("You will now be redirected to the method to add an author to the author table, this will automatically be selected. \n")
            add_data_to_author_table()
            data.append(generated_author_id)
            break


    """Subset Function to Gather Genre"""
    #Establish and Show Genre Table for Refrence
    query1 = "SELECT * FROM genre;"
    cursor.execute(query1)
    genre_table = cursor.fetchall()
    generated_genre_id = genre_table[-1][0] + 1
    print("| ID  | Genre          |")
    print("------------------------")
    for genre in genre_table:
        print(f"| {genre[0]:<4}| {genre[1]:<15}|")
    print("------------------------")
    print("| ID  | Genre          |")
    while True:
        #Loop to Gather Genre Information
        #Checks where the genre information will come from, adding an genre or refrencing an existing genre
        gatherer = input("Is the genre you want to enter in the table above? (Y/N) ") 
        if gatherer not in polarity:
            #Checks if the Yes/No input is Valid
            print("That input is invalid, please try again!")
            continue
        elif gatherer == "Y":
            #If the input is Yes, Request the numerical id of the genre and check that it is a valid range
            try:
                genre_id = int(input("Please enter the numerical id of the genre of the book you are entering data for, this can be found in the above table! "))
                if genre_id <= generated_genre_id and genre_id > 0:
                    data.append(genre_id)
                    break
                else:
                    #If value is outside the valid range, return an error and request info again
                    print("That id is not in the Table")
                    continue
            except ValueError:
                #If the input is not an integer, return an error and request info again
                print("That is an invalid input")
                continue
        elif gatherer == "N":
            #Redirect the user to the function to add an author to the table and use the generated id
            print("You will now be redirected to the method to add an author to the genre table, this will automatically be selected. \n")
            add_data_to_genre_table()
            data.append(generated_genre_id)
            break
    

    #Page Count
    while True:
        try:
            pages = int(input("Please enter the number of pages in the book! "))
            #Check Data
            if pages > 0:
                data.append(pages)
                break
            else:
                print("Please enter a positive whole number")
                continue
        except:
            print("That is an invalid input, please enter a positive whole number")
            continue
    
    #Word Count
    while True:
        try:
            words = int(input("Please enter the number of words in the book! "))
            #Check Data
            if words > 0:
                data.append(words)
                break
            else:
                print("Please enter a positive whole number")
                continue
        except:
            print("That is an invalid input, please enter a positive whole number")
            continue
    
    #Release Date
    while True:
        try:
            #Gather Release Date
            release_date = input("Please enter the release date of the book in the format YYYY/MM/DD using numerical representation! ")
            #Restructure Data
            year, month, day = release_date.split('/')
            #Date validation
            d = date(int(year), int(month), int(day))
            data.append(release_date)
            break
        except ValueError:
            #Checks for non-numerical characters in invalid places by Value Errors
            print("Invalid Input, letters in the allocated spaces for year, month, and day numbers")
            continue
    
    #ISBN
    while True:
        try:
            #Gather Input and Generate Test String
            isbn = int(input("Please enter the books ISBN number, this should be a 13 digit number without hyphens! "))
            isbn_test = str(isbn)
            #Test for valid string length
            if len(isbn_test) != 13:
                print("That number has too many or few digits, please try again.")
                continue
            else:
                data.append(isbn)
                break
        except ValueError:
            #Checks if the string is purely numerical using Value Errors
            print("Your input was invalid, it likely contained hyphens or connecting strings, if this error is a result of copy pasting, please type it manually")
            continue
    
    #Review
    while True:
        try:
            #Gather Input and generate test string
            print("To gather the data for the review I used www.goodreads.com")
            review = float(input("Please enter the books review on a scale from 1 to 5, this should a number with one decimal place. "))
            review_test = str(review)
            if len(review_test) == 3 and review >= 1 and review <= 5:
                data.append(review)
                break
            else:
                print("Your input was outside the range of 1 to 5(inclusive), contained more than one decimal place or contained no decimal places. Please Try Again!")
        except ValueError:
            print("Your Input contained non numerical characters in such a way that the value was not recognised as a decimal.1")
            continue

    final_query = f"INSERT INTO book (id, name, author, genre, pages, word_count, release_date, isbn, review) VALUES ({next_id}, '{data[0]}', {data[1]}, {data[2]}, {data[3]}, {data[4]}, '{data[5]}', {data[6]}, {data[7]})"
    cursor.execute(final_query)
    print("\n")
    print("Sucessfully added the data to the database.")
    print("\n")
    db.commit()
    db.close()
def remove_data_from_genre_table():
    """Function to Remove Data from the Genre Table"""
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    genres = []
    
    #Display Table for Refrence
    gather_query = "SELECT * FROM genre;"
    cursor.execute(gather_query)
    genre_table = cursor.fetchall()
    print("| ID  | Genre          |")
    print("------------------------")
    for genre in genre_table:
        print(f"| {genre[0]:<4}| {genre[1]:<15}|")
    print("------------------------")
    print("| ID  | Genre          |")

    #Gather Id
    for genre in genre_table:
        genres.append(genre[0])
    #Gather Id and check against list
    while True:
        try:
            id = int(input("Please enter the id of the genre you want to remove from the genre table! "))
            if id in genres:
                break
            else:
                print("That id is not in the table, please try again!")
                continue
        except ValueError:
            print("Your entry was not a number please try again.")
            continue
    
    #Execute Genre Removal Query and coresponding books to remove errors
    query = f"DELETE FROM genre WHERE id = {id}"
    cursor.execute(query)
    query2 = f"DELETE FROM book WHERE genre = {id}"
    cursor.execute(query2)
    print("Sucessfully removed from the database!")

    db.commit()
    db.close()
def remove_data_from_author_table():
    """Function to Remove Data from the Author Table"""
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    authors = []
    
    #Display Table for Refrence
    gather_query = "SELECT * FROM author;"
    cursor.execute(gather_query)
    author_table = cursor.fetchall()
    print("| ID  | Author Name                                       |")
    print("-----------------------------------------------------------")
    for author in author_table:
        print(f"| {author[0]:<4}| {author[1]:<50}|")
    print("-----------------------------------------------------------")
    print("| ID  | Author Name                                       |")
    #Gather Id list
    for author in author_table:
        authors.append(author[0])
    #Gather Id and check against list
    while True:
        try:
            id = int(input("Please enter the id of the author you want to remove from the author table! "))
            if id in authors:
                break
            else:
                print("That id is not in the table, please try again!")
                continue
        except ValueError:
            print("Your entry was not a number please try again.")
            continue
    
    #Execute Author Removal Query and remocing coresponding books to prevent errors
    query = f"DELETE FROM author WHERE id = {id}"
    cursor.execute(query)
    query2 = f"DELETE FROM book WHERE author = {id}"
    cursor.execute(query2)
    print("Sucessfully removed from the database!")

    db.commit()
    db.close()
def remove_data_from_book_table():
    """Function to Remove Data from the Book Table"""
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    books = []

    #Display all the relevant information
    query = "SELECT book.id, book.name, author.name, genre.genre FROM book JOIN author ON author.id = book.author JOIN genre on genre.id = book.genre ORDER BY book.id ASC"
    cursor.execute(query)
    book_table = cursor.fetchall()
    print("| ID  | Book Title                                        | Author Name         | Genre          |")
    print("--------------------------------------------------------------------------------------------------")
    for book in book_table:
        print(f"| {book[0]:<4}| {book[1]:<50}| {book[2]:<20}| {book[3]:<15}|")
    print("--------------------------------------------------------------------------------------------------")
    print("| ID  | Book Title                                        | Author Name         | Genre          |")

    #generate list of ids
    for book in book_table:
        books.append(book[0])
    #Gather target id and check for validity
    while True:
        try:
            id = int(input("Using the table above, enter the id of the row you want to remove from the database! "))
            if id in books:
                break
            else:
                print("That id is not in the database, Please try again.")
        except ValueError:
            print("The id you tried to enter is not a numeral, please try again.")

    #Remove data from desired id
    query2 = f"DELETE FROM book WHERE id = {id}"
    cursor.execute(query2)
    print("Sucessfully removed from the database!")
    db.commit()
    db.close()
def remove_data():
    """Function to Authorise and Redirect to Data Removal Functions"""
    #Array of Data removal functions
    func_array = {
        "1": remove_data_from_author_table,
        "2": remove_data_from_book_table,
        "3": remove_data_from_genre_table,
    }
    global admin
    #Checks if the user has admin permissions with a password
    while True:
        if admin == True:
            print("Access Granted!")
            break
        print("For development and testing purposes, the username is username and the password is password, all in lowercase.")
        username = input("Username: ")
        password = input("Password: ")
        if username == "username" and password == "password":
            print("Access Granted!")
            admin = True
            break
        else:
            print("Wrong Username/Password")
            continue
    #List of tables
    print("1. Author \n2. Book \n3. Genre")
    #Gathers the table and redirects to the correct function
    while True:
        location = input("Enter the id of table you want to remove data from using the above list. ")
        if location in func_array.keys():
            func_array[location]()
            break
        else:
            print("Invalid Input, Please try again!")
            continue


#Establish Array of Functions
function_array = {
    "1": search_for_books_by_an_author,
    "2": search_by_wordcount_return_title_author_genre_wordcount,
    "3": search_by_pagecount,
    "4": book_names_and_authors_and_genres,
    "5": book_names_and_authors_and_release_date,
    "6": book_names_and_author_and_general_reviews,
    "7": book_names_and_isbn_13_classification_and_release_date,
    "8": search_for_books_released_in_a_year,
    "9": add_data_to_genre_table,
    "10": add_data_to_author_table,
    "11": add_data_to_book_table,
    "12": remove_data,
    "quit": quit,
}



#Major Code Loop
if __name__ == "__main__":
    while True:
        #Code to give the user a series of function options, these include prewritten querries, searches (WIP), and adding/removing data
        print("="*150)
        print('Enter the word quit to close the application!')
        print('1. Search for all the books written by an author')
        print('2. Return the title, author, genre, and word count of books with a larger or smaller word count than an user input')
        print('3. Return the title, author, genre, and page count of books with a larger or smaller page count than an user input')
        print('4. Print all the book titles, authors, and genres')
        print('5. Print all the book titles, authors, and release dates')
        print('6. Print all the book titles, authors, and the general reviews')
        print('7. Print all the book titles, isbn-13 numbers, and release dates')
        print('8. Search for all the books released in a year')
        print('9. Add data to the genre table')
        print('10. Add data to the author table')
        print('11. Add data to the book table')
        print('12. Remove data from a table')
        #Gets the user input correlating to a function
        user_input = input('Input the number associated with the function you wish to execute. \n')
        #Lookup and execute the correct function based on a function dictionary
        if user_input.lower() in function_array.keys():
            function_array[user_input.lower()]()
            sleep(2)
        else:
            #Return an error message if the function is not correlated to a function
            print("Invalid input, please enter the number before a function without any trailing spaces or symbols!")
            continue

        