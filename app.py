'''
This is an application to view my SQL database, insert information, update information. Matthew Thomas 27/05/24
'''
#Importing Modules
import sqlite3
import time

#Intializing variables
DATABASE = "Y11_Programming/SQLite3/Assesment-Database-Books/books.db"
user_input = None

#List of Existing Functions
def book_names_and_authors():
    '''Function to display all the books and their authors'''
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, author.name FROM book JOIN author ON author.id = book.author ORDER BY book.name ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print("| Book Title                                        | Author Name         |")
    print("---------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<20}|")
    print("---------------------------------------------------------------------------")
    print("| Book Title                                        | Author Name         |")
    db.close()
def book_names_and_author_and_wordcount_greater_than_150000():
    '''Function to display all the books, their word counts and their authors when the word count exceeds 150000'''
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, book.word_count, author.name FROM book JOIN author on author.id = book.author WHERE word_count > 150000 ORDER BY book.word_count DESC"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print("| Book Title                                        | Word Count  | Author Name         |")
    print("-----------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<12}| {data[2]:<20}|")
    print("----------------------------------------------------------------------------------------")
    print("| Book Title                                        | Word Count  | Author Name         |")
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
    print("-------------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<20}| {data[2]:<14}|")
    print("-------------------------------------------------------------------------------------------")
    print("| Book Title                                        | Author Name         | Release Date   |")
    db.close()
def book_names_and_author_and_my_enjoyment_and_general_reviews():
    '''Function to display all the books, their authors, my enjoyment, and their general review average'''
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, author.name, book.enjoyment, book.review FROM book JOIN author ON author.id = book.author ORDER BY book.name ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print("Note: Enjoyment and Reviews are on a scale from 1 to 5.")
    print("| Book Title                                        | Author Name         | Enjoyment | Reviews |")
    print("-------------------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<20}| {data[2]:<10}| {data[3]:<8}|")
    print("-------------------------------------------------------------------------------------------------")
    print("| Book Title                                        | Author Name         | Enjoyment | Reviews |")
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
    print("Note: Enjoyment and Reviews are on a scale from 1 to 5.")
    print("| Book Title                                        | ISBN          | Release Date |")
    print("------------------------------------------------------------------------------------")
    for data in results:
        print(f"| {data[0]:<50}| {data[1]:<14}| {data[2]:<13}|")
    print("------------------------------------------------------------------------------------")
    print("| Book Title                                        | ISBN          | Release Date |")
    db.close()

#Establish Array of Functions
function_array = {
    "1": book_names_and_authors,
    "2": book_names_and_author_and_wordcount_greater_than_150000,
    "3": book_names_and_page_count_and_author_and_genre_pages_less_than_333,
    "4": book_names_and_authors_and_genres,
    "5": book_names_and_authors_and_release_date,
    "6": book_names_and_author_and_my_enjoyment_and_general_reviews,
    "7": book_names_and_isbn_13_classification_and_release_date,
    "": quit,
}



#Major Code Loop
if __name__ == "__main__":
    #Loop to Provide 
    while True:
        print('---------------------------------------------------------------------------------------')
        print('Press Enter without providing and input to close the program')
        print('\n')
        print('1. Print all the book titles and authors')
        print('2. Print the book titles, word counts, and authors where there are more than 150,000 words')
        print('3. Print the book titles, page counts, authors, and genre of books with less than 333 pages.')
        print('4. Print all the book titles, authors, and genres.')
        print('5. Print all the book titles, authors, and release dates')
        print('6. Print all the book titles, authors, my enjoyment, and the general reviews')
        print('7. Print all the book titles, isbn-13 numbers, and release dates')
        user_input = input('Input the number associated with the function you wish to execute. \n')
        print("\n")
        if user_input in function_array.keys():
            function_array[user_input]()
            time.sleep(5)
        else:
            print("Invalid input, please enter the number before a function without any trailing spaces or symbols!")
            continue

        