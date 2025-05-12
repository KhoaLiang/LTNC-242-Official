class Vehicle{
    private String brand;
    private int year;

    Vehicle(){
        this.brand = "Unknown";
        this.year = 0;
    }

    Vehicle(String brand, int year){
        this.brand = brand;
        this.year = year;
    }
    public String getBrand(){
        return brand;
    }
    public int getYear(){
        return year;
    }
    public void setBrand(String brand){
        this.brand = brand;
    }
    public void setYear(int year){
        this.year = year;
    }
    public void display() {
        System.out.println("Brand: " + brand);
        System.out.println("Year: " + year);
    }
}
class Car extends Vehicle{
    private String model;

    Car(){
        super();
        this.model = "Unknown";
    }
    Car(String brand, int year, String model){
        super(brand, year);
        this.model = model;
    }
    @Override public void display(){
        super.display();
        System.out.println("Model: " + model);
    }
}

class Bike extends Vehicle{
    private int engineCapacity;

    Bike(){
        super();
        this.engineCapacity = 0;
    }
    Bike(String brand, int year, int engineCapacity){
        super(brand, year);
        this.engineCapacity = engineCapacity;
    }
    @Override public void display(){
        super.display();
        System.out.println("Engine capacity: " + engineCapacity);
    }
}
public class Main_Inheritance_Vehicle{
    public static void main(String[] args) {
        Vehicle vehicle = new Vehicle("Toyota", 2020);
        vehicle.display();
        System.out.println();

        Car defaultCar = new Car();
        defaultCar.display();
        System.out.println();
        // Create a Car object using the parameterized constructor
        
        Car car = new Car("Honda", 2021, "Civic");
        car.display();
        System.out.println();

        Bike defaultBike = new Bike();
        defaultBike.display();
        System.out.println();
        // Create a Bike object using the parameterized constructor

        Bike bike = new Bike("Yamaha", 2019, 150);
        bike.display();
    }
}