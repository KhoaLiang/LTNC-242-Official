interface Drawable {
    void draw();  // Abstract method
}

interface Area {
    double calculateArea();  // Abstract method to calculate area
}

class Rectangle implements Drawable, Area {
    private double length;
    private double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    public void draw() {
        System.out.println("Drawing Rectangle");
    }

    @Override
    public double calculateArea() {
        return length * width;
    }
}

public class Main_Interface {
    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle(5.0, 3.0);

        // Test the draw method
        rectangle.draw();

        // Test the calculateArea method
        System.out.println("Area of Rectangle: " + rectangle.calculateArea());
    }
}