public class Parallelepiped_Test {
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

        // Test getArea (from Rectangle)
        assert parallelepiped.getArea() == 12.0 : "Area should be 12.0";

        // Test getVolume
        assert parallelepiped.getVolume() == 60.0 : "Volume should be 60.0";

        // Test getSurfaceArea
        assert parallelepiped.getSurfaceArea() == 94.0 : "Surface area should be 94.0";

        System.out.println("All tests passed.");
    }
}