
class Book {
    private String title;
    private String author;
    private String ISBN;
    private double price;
    private int stock;

    public Book() {
        this.title = "Unknown";
        this.author = "Unknown";
        this.ISBN = "000-0-00-000000-0";
        this.price = 0.0;
        this.stock = 0;
    }
    public Book(String title, String author, String ISBN, double price, int stock) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
        this.price = price;
        this.stock = stock;
    }
    public String getTitle() {
        return title;
    }
    public String getAuthor() {
        return author;
    }
    public String getISBN() {
        return ISBN;
    }
    public double getPrice() {
        return price;
    }
    public int getStock() {
        return stock;
    }
    public void setTitle(String title) {
        this.title = title;
    }
    public void setAuthor(String author) {
        this.author = author;
    }
    public void setISBN(String ISBN) {
        this.ISBN = ISBN;
    }
    public void setPrice(double price) {
        this.price = price;
    }
    public void setStock(int stock) {
        this.stock = stock;
    }
    public void display() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("ISBN: " + ISBN);
        System.out.println("Price: $" + price);
        System.out.println("Stock: " + stock);
    }
}

class Library {
    private String name;
    private String location;
    private Book[] books;
    private int bookCount;

    public Library() {
        this.name = "Unknown Library";
        this.location = "Unknown Location";
        this.books = new Book[10];
        this.bookCount = 0;
    }
    public Library(String name, String location) {
        this.name = name;
        this.location = location;
        this.books = new Book[10];
        this.bookCount = 0;
    }
    public void addBook(Book book) {
        if (bookCount < books.length) {
            books[bookCount++] = book; //shalow copy assigns the reference of the book object to the books array.
            // This means that the books array will hold references to the same Book objects that are passed to the addBook method.
            // If you modify the book object after adding it to the array, the changes will be reflected in the array as well.

            // books[bookCount++] = new Book(book.getTitle(), book.getAuthor(), book.getISBN(), book.getPrice(), book.getStock()); //deep copy
        } else {
            System.out.println("Library is full. Cannot add more books.");
        }
    }
    public void displayBooks() {
        System.out.println("Books in " + name + ":");
        for (int i = 0; i < bookCount; i++) {
            books[i].display();
            System.out.println();
        }
    }
}

public class Main_Lib_Book {
    public static void main(String[] args) {
        // Create a Library object using the default constructor
        Library library1 = new Library();
        library1.displayBooks();
        System.out.println();

        // Create a Library object using the parameterized constructor
        Library library2 = new Library("City Library", "123 Main St");
        library2.addBook(new Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 10.99, 5));
        library2.addBook(new Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 7.99, 3));
        library2.displayBooks();
    }
}
