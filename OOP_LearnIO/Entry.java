// import java.util.Scanner;

// class Student{
// 	String name;
//     int age;

//     public void display(){
//         System.out.println("Name: " + name);
//         System.out.print("Age: " + age);
//     }
//     public void getInformation(){
//         Scanner sc = new Scanner(System.in);
//         name = sc.next();
// 		age = sc.nextInt();
//     }
// }


// public class Entry {
// 	public static void main(String[]args) {
// 		Student s1 = new Student();
// 		s1.getInformation();
// 		s1.display();
// 	}
// }


//recontangle

import java.util.Scanner;

class Rectangle{
	double length;
    double width;

    public void getInformation(){
        Scanner sc = new Scanner(System.in);
        length = sc.nextDouble();
		width = sc.nextDouble();
    }
    
    public double getArea(){
        return length * width;
    }
    public double getPerimeter(){
        return (2 * (length + width));
    }
    public void display(){
        System.out.println("Area: " + getArea());
        System.out.print("Perimeter: " + getPerimeter());
    }
}

public class Entry {
	public static void main(String[]args) {
		Rectangle r = new Rectangle();
		r.getInformation();
		r.display();
	}
}