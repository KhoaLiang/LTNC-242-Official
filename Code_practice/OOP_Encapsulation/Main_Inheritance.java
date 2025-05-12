class Superclass {
    public void display() {
        System.out.println("Superclass");
    }
}
class Subclass extends Superclass {
    @Override
    public void display() {
        System.out.println("Subclass");
    }
}
public class Main_Inheritance {
    public static void main(String[] args) {
        Superclass obj = new Subclass(); 
        obj.display(); // Output: Subclass
        // The method display() in Subclass overrides the method in Superclass
    }
}
