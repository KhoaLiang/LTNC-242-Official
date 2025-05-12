public class Entry_Car {
    public static void main(String[] args) {
        // Create a Car object using the default constructor
        Car1 car1 = new Car1();
        car1.display();
        System.out.println();

        // Create a Car object using the parameterized constructor
        Car1 car2 = new Car1("Toyota", "Camry", 2020);
        car2.display();
        System.out.println();
    }
}