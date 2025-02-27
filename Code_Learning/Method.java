import java.util.Scanner;

public class Method {
	public static int sumOfArray(int[] arr) {
		int sum = 0;
        for(int i = 0; i < arr.length; i++){
            sum += arr[i];
        }
        return sum;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		System.out.print(sumOfArray(arr));
	}
}

//print array
// import java.util.Scanner;

// public class Method {
// 	public static void show(int[] arr){
//         for(int i = 0; i < arr.length; i++){
//             if((arr[i] % 3 == 0) && (arr[i] % 5 != 0)){
//                 System.out.print(arr[i] + " ");
//             }
//         }
//     }

// 	public static void main(String[] args) {
// 		Scanner sc = new Scanner(System.in);
// 		int n = sc.nextInt();
// 		int[] arr = new int[n];
// 		for (int i = 0; i < n; i++) {
// 			arr[i] = sc.nextInt();
// 		}
// 		show(arr);
// 	}
// }