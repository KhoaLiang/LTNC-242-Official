class Parallelepiped extends Rectangle{
    private double depth;

    public Parallelepiped(double width, double height, double depth) {
        super(width, height);
        this.depth = depth;
    }
    public double getDepth(){
        return depth;
    }
    public double getVolume(){
        return getArea() * depth;
    }
    public double getSurfaceArea(){
        return 2 * (getHeight() * getWidth() + getHeight() * getDepth() + getWidth() * getDepth());
    }
}