class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    # Adds book title to author's list, unless it's already there
    def publish(self, title):
        if title in self.books: #checks if title is already in list
            print(f"Error: You already entered {title} for {self.name}")
        else:
            self.books.append(title) # Only runs if the title is new

    def __str__(self):
        return f"{self.name} has published: {', '.join(self.books)}"

def main():
    tolkien = Author("J.R.R Tolkien")
    tolkien.publish("The Hobbit")
    tolkien.publish("The Fellowship of the Ring")
    tolkien.publish("The Hobbit") #Duplicate

    rowling = Author("J.K. Rowling")
    rowling.publish("The Prisoner of Azkaban")

    print(tolkien)
    print(rowling)

if __name__ == "__main__":
        main()