import java.util.Scanner;

public class Statement {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		if (n % 2 == 0) {
			System.out.println("n is an even number");
		} else {
			System.out.println("n is an odd number");
		}
	}
}

// Câu lệnh if trong Java
// import java.util.Scanner;

// public class Statement {
// 	public static void main(String[] args) {
// 		Scanner sc = new Scanner(System.in);
// 		String a = sc.next();
// 		String b = sc.next();
// 		if (a.equals(b)) {
// 			System.out.println("two people have the same name");
// 		} else {
// 			System.out.println("two people don't have the same name");
// 		}
// 	}
// }