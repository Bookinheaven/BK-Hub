import java.io.*;
import java.util.*;

abstract class Book {
	abstract void display();
}
class MyBook extends Book {
	private String title;
	private String author;
	private int price;
	MyBook(String title, String author, int price){
		this.title= title;
		this.author= author;
		this.price= price;;
	}

	@Override
	void display() {
		System.out.print("Title: %s\nAuthor: %s\nPrice: %d".formatted(title, author, price));
	}
    
}
public class F1 {

    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	String title = sc.nextLine();
    	String author = sc.nextLine();
    	int price = sc.nextInt();
    	MyBook b1 = new MyBook(title, author,price);
    	b1.display();
    	sc.close();
    }
}