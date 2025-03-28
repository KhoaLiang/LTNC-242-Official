class Circle {
    private double radius;
    private String color;

    public Circle() {
        radius = 1.0;
        color = "red";
    }

    public Circle(double radius) {
        this.radius = radius;
        color = "red";
    }

    public Circle(double radius, String color) {
        this.radius = radius;
        this.color = color;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public double getArea() {
        return Math.PI * radius * radius;
    }

    public String toString() {
        return "Circle[radius=" + radius + ",color=" + color + "]";
    }
}

class Cone {
    private Circle base;
    private double height;

    public Cone() {
        base = new Circle();
        height = 1.0;
    }

    public Cone(double radius) {
        base = new Circle(radius);
        height = 1.0;
    }

    public Cone(double radius, double height) {
        base = new Circle(radius);
        this.height = height;
    }

    public Cone(double radius, double height, String color) {
        base = new Circle(radius, color);
        this.height = height;
    }

    public double getRadius() {
        return base.getRadius();
    }

    public void setRadius(double radius) {
        base.setRadius(radius);
    }

    public String getColor() {
        return base.getColor();
    }

    public void setColor(String color) {
        base.setColor(color);
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double getArea() {
        return base.getArea();
    }

    public double getVolume() {
        return base.getArea() * height / 3;
    }

    public String toString() {
        return "Cone[base=" + base + ",height=" + height + "]";
    }
}

public class TestConeComposition {
    public static void main(String[] args) {
        Cone cone1 = new Cone();
        System.out.println("Cone:"
                + " radius=" + cone1.getRadius()
                + " height=" + cone1.getHeight()
                + " base area=" + cone1.getArea()
                + " volume=" + cone1.getVolume());
        Cone cone2 = new Cone(5.0, 2.0);
        System.out.println("Cone:"
                + " radius=" + cone2.getRadius()
                + " height=" + cone2.getHeight()
                + " base area=" + cone2.getArea()
                + " volume=" + cone2.getVolume());
    }
}