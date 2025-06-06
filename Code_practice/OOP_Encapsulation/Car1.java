public class Car1{
    private String brand;
    private String model;
    private int year;

    public Car1(){
        this.brand = "Empty";
        this.model = "Empty";
        this.year = 0;
    }
    public Car1(String brand, String model, int year){
        this.brand = brand;
        this.model = model;
        this.year = year;
    }
    public String getBrand(){
        return brand;
    }
    public String getModel(){
        return model;
    }
    public int getYear(){
        return year;
    }
    public void setBrand(String brand){
        this.brand = brand;
    }
    public void setModel(String model){
        this.model = model;
    }
    public void setYear(int year){
        this.year = year;
    }
    public void display() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }
}