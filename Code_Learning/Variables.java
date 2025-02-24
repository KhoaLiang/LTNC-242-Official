public class Variables {
	public static void main(String[] args) {
		// Khai báo biến a kiểu số nguyên và gán giá trị cho a = 438
		int a = 254;
		// Khai báo biến b kiểu số nguyên và gán giá trị cho b = 238
		int b = 343;
		System.out.println("a + b = " + (a + b));


        String name = "Codelearn";
		System.out.println("Hello " + name);

        double c = 10.5;
		double d = 7;
		System.out.println("c / d = " + c / d);

        char character = 'x';
		System.out.println(character);

        char toAdd = 'a' + 3;
		System.out.println(toAdd);
	}
}

/* Trong ngôn ngữ lập trình Java có các kiểu dữ liệu lưu trữ số nguyên như: byte, short, int, long, ...


Sự khác biệt giữa các kiểu dữ liệu này là miền giá trị:


Miền giá trị của kiểu byte là từ -128 tới  127.


Miền giá trị của kiểu short là từ -32768 tới 32767.


Miền giá trị của kiểu int là từ -2147483648 tới 2147483647.


Miền giá trị của kiểu long là từ -9223372036854775808 tới 9223372036854775807.


Có thể thấy miền giá trị của kiểu long là lớn nhất, bạn có thể dùng kiểu dữ liệu này để thay cho các kiểu dữ liệu khác nhưng bù lại dùng 
kiểu dữ liệu này sẽ tốn bộ nhớ hơn (kiểu dữ liệu có miền giá trị càng lớn sẽ càng tốn bộ nhớ). Do đó bạn cần sử dụng các kiểu dữ liệu một 
cách hợp lý, ví dụ biến để lưu trữ số học sinh trong một lớp học nên là kiểu short vì thường một lớp chỉ có vài chục học sinh. */