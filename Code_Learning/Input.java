import java.util.Scanner;

public class Input {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String name = sc.next();
		String address = sc.next();
		System.out.println("Name: " + name);
		System.out.println("Address: " + address);

        int a = sc.nextInt();
		int b = sc.nextInt();
		System.out.println(a + b);

        String name1 = sc.next();
		int age = sc.nextInt();
		System.out.println("In 15 years, age of " + name1 + " will be " + (age + 15));

        double r = sc.nextDouble();
		double pi = 3.14;
		System.out.println("Circumference = " + (2 * pi * r));

        char c = sc.next().charAt(0);
        c += 1;
        System.out.println(c);

        int d = sc.nextInt();
        int f = sc.nextInt();
        System.out.println(d > f);
	}
}