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
    print("---------------------------------------------------------------------------")
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
    print("-----------------------------------------------------------------------------------------")
    print("| Book Title                                        | Word Count  | Author Name         |")
    print("-----------------------------------------------------------------------------------------")
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
    print("-------------------------------------------------------------------------------------------------")
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
    print("------------------------------------------------------------------------------------")
    db.close()
def search_for_books_released_in_a_year():
    '''Function to display book titles, authors, and release dates based on a used input of a year'''
    search_query = None
    while search_query == None:
        try:
            search_query = int(input("Enter which year's book releases you would like to view! (Positive Numbers Only Please!) "))
            if search_query <= 0:
                search_query = 0
                print("Please enter a positive whole number")
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
def add_data_to_a_table():
    #Establish Interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    tables = ['book', 'author', 'genre']
    names = []
    type = []
    print("Enter a Number Correlating to the table you want to edit")
    print("1. Books \n2. Authors \n3. Genres")
    table_id = 0
    while table_id == 0:
        try:
            table_id = int(input(""))
        except ValueError:
            print("Please Enter a Valid input.")
    query = f"PRAGMA table_info({tables[table_id-1]})"
    cursor.execute(query)
    table_data = cursor.fetchall()
    for column_data in table_data:
        names.append(column_data[1])
        type.append(column_data[2])
    print(table_data)
    print(names)
    print(type)




#Establish Array of Functions
function_array = {
    "1": book_names_and_authors,
    "2": book_names_and_author_and_wordcount_greater_than_150000,
    "3": book_names_and_page_count_and_author_and_genre_pages_less_than_333,
    "4": book_names_and_authors_and_genres,
    "5": book_names_and_authors_and_release_date,
    "6": book_names_and_author_and_my_enjoyment_and_general_reviews,
    "7": book_names_and_isbn_13_classification_and_release_date,
    "8": search_for_books_released_in_a_year,
    "9": add_data_to_a_table,
    "quit": quit,
}



#Major Code Loop
if __name__ == "__main__":
    while True:
        #Code to give the user a series of function options, these include prewritten querries, searches (WIP), and adding/removing data
        print('Use the string quit without providing an input to close the program')
        print('\n')
        print('1. Print all the book titles and authors')
        print('2. Print the book titles, word counts, and authors where there are more than 150,000 words')
        print('3. Print the book titles, page counts, authors, and genre of books with less than 333 pages.')
        print('4. Print all the book titles, authors, and genres.')
        print('5. Print all the book titles, authors, and release dates')
        print('6. Print all the book titles, authors, my enjoyment, and the general reviews')
        print('7. Print all the book titles, isbn-13 numbers, and release dates')
        print('8. Search for all the books released in a year')
        print('9. Add data to a table')
        #Gets the user input correlating to a function
        user_input = input('Input the number associated with the function you wish to execute. \n')
        print("\n")
        #Lookup and execute the correct function based on a function dictionary
        if user_input in function_array.keys():
            function_array[user_input.lower()]()
            time.sleep(2)
        else:
            #Return an error message if the function is not correlated to a function
            print("Invalid input, please enter the number before a function without any trailing spaces or symbols!")
            continue

        