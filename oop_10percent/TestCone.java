class Circle {
    private double radius;
    private String color;

    public Circle(){
        radius = 1.0;
        color = "red";
    }
    public Circle(double radius){
        this.radius = radius;
        color = "red";
    }
    public Circle(double radius, String color){
        this.radius = radius;
        this.color = color;
    }
    public double getRadius(){
        return radius;
    }
    public void setRadius(double radius){
        this.radius = radius;
    }
    public String getColor(){
        return color;
    }
    public void setColor(String color){
        this.color = color;
    }
    public double getArea(){
        return Math.PI * radius * radius;
    }
    public String toString(){
        return "Circle[radius=" + radius + ",color=" + color + "]";
    }
}
class Cone extends Circle{
    private double height;

    public Cone(){
        super();
        height = 1.0;
    }
    public Cone(double radius){
        super(radius);
        height = 1.0;
    }
    public Cone(double radius, double height){
        super(radius);
        this.height = height;
    }
    public Cone(double radius, double height, String color){
        super(radius, color);
        this.height = height;
    }
    public double getHeight(){
        return height;
    }
    public void setHeight(double height){
        this.height = height;
    }
    public double getVolume(){
        return getArea() * height / 3;
    }
}
public class TestCone {
    public static void main(String[] args) {
    }
}
