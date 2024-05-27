'''
This is an application to view my SQL database, insert information, update information. Matthew Thomas 27/05/24
'''
#Importing Modules
import sqlite3

#Intilizing constants

DATABASE = "books.db"

def book_names_and_authors():
    '''Function to display all the books and their authors'''
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Execute and Fetch Data
    query = "SELECT book.name, author.name FROM book JOIN author ON author.id = book.author;"
    cursor.execute(query)
    results = cursor.fetchall()
    #Print out the Results
    print(results)
    db.close()

if __name__ == "__main__":
    book_names_and_authors()