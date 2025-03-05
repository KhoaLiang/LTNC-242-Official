class Rectangle {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    public double getArea() {
        return width * height;
    }
}
class Parallelepiped {
    private Rectangle base;
    private double depth;

    public Parallelepiped(double width, double height, double depth) {
        this.base = new Rectangle(width, height);
        this.depth = depth;
    }

    public double getWidth() {
        return base.getWidth();
    }

    public double getHeight() {
        return base.getHeight();
    }

    public double getDepth() {
        return depth;
    }

    public double getBaseArea() {
        return base.getArea();
    }

    public double getVolume() {
        return getBaseArea() * depth;
    }

    public double getSurfaceArea() {
        return 2 * (getHeight() * getWidth() + getHeight() * getDepth() + getWidth() * getDepth());
    }
}
public class Parallelepiped_Test_Composition {
    public static void main(String[] args) {
        testParallelepiped();
    }

    public static void testParallelepiped() {
        Parallelepiped parallelepiped = new Parallelepiped(3.0, 4.0, 5.0);

        // Test getWidth
        assert parallelepiped.getWidth() == 3.0 : "Width should be 3.0";

        // Test getHeight
        assert parallelepiped.getHeight() == 4.0 : "Height should be 4.0";

        // Test getDepth
        assert parallelepiped.getDepth() == 5.0 : "Depth should be 5.0";

        // Test getBaseArea (from Rectangle)
        assert parallelepiped.getBaseArea() == 12.0 : "Base area should be 12.0";

        // Test getVolume
        assert parallelepiped.getVolume() == 60.0 : "Volume should be 60.0";

        // Test getSurfaceArea
        assert parallelepiped.getSurfaceArea() == 94.0 : "Surface area should be 94.0";

        System.out.println("All tests passed.");
    }
}
