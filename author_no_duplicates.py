# Author object
import author


class Author:

    # This will run automatically when you create a new author
    # Self is the specific author being used at that moment
    def __init__(self, name):
        self.name = name
        self.books = []  # Each author starts with empty book list

    # Adds book title to author's list
    def publish(self, title):
        self.books.append(title)  # Adds to the end of the list

    # Runs automatically when an author is printed
    def __str__(self):
        return f"{self.name} has published: {', '.join(self.books)}"  # .join will put the list of titles into one string separated by commas


# Author that won't publish the same title twice
class UniqueAuthor(Author):

    # Only decides yes or no, doesn't print or change the list
    def is_duplicate(self, title):
        return title in self.books  # 'in' already evaluates to True or False

    # Only job is talking to the user
    def report_duplicate(self, title):
        print(f"Error: {self.name} has already published {title}.")

    # Overrides Author.publish, so this version runs instead
    def publish(self, title):
        if self.is_duplicate(title):
            self.report_duplicate(title)
        else:
            Author.publish(self, title)  # Hands off to Author.publish to do the append


# Call and test above methods
def main():
    shakespeare = UniqueAuthor('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Romeo and Juliet')
    shakespeare.publish('Hamlet')  # Duplicate, should print the error

    rowling = UniqueAuthor("J.K. Rowling")
    rowling.publish("The Prisoner of Azkaban")

    print(shakespeare)
    print(rowling)


if __name__ == "__main__":
    main()