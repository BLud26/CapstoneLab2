class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        return f"{self.name} has published: {', '.join(self.books)}"

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