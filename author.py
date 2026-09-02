# Author object
class Author:

    # This will run automatically when you create a new author
    # Self is the specific author being used at that moment
    def __init__(self, name):
        self.name = name
        self.books = [] # Each author starts with empty book list

    # Adds book title to author's list
    def publish(self, title):
        self.books.append(title) # Adds to the end of the list

    # Runs automatically when an author is printed
    def __str__(self):
        return f"{self.name} has published: {', '.join(self.books)}" #.join will put the list of titles into one string separated by commas

# Call and test above methods
def main():
    tolkien = Author("J.R.R Tolkien")
    tolkien.publish("The Hobbit")
    tolkien.publish("The Fellowship of the Ring")

    rowling = Author("J.K. Rowling")
    rowling.publish("The Prisoner of Azkaban")

    print(tolkien)
    print(rowling)

if __name__ == "__main__":
    main()