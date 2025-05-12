class A {
    int x;
    A(int x) {
        this.x = x;
    }
}

class B extends A {
    int y;
    B(int x, int y) {
        super(x);
        this.y = y;
    }
}

public class Test {
    public static void main(String[] args) {
        B obj = new B(5, 10);
        System.out.println(obj.x + " " + obj.y);
    }
}
