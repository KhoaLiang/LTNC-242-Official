class Rectangle2{
    private double width;
    private double length;
    private String color;

    public Rectangle2(){
        this.width = 1;
        this.length = 1;
        this.color = "red";
    }
    public Rectangle2(double width, double length){
        this.width = width;
        this.length = length;
        this.color = "red";
    }
    public Rectangle2(double width, double length, String color){
        this.width = width;
        this.length = length;
        this.color = color;
    }
    public double getWidth(){
        return width;
    }
    public void setWidth(){
        this.width = width;
    }
    public double getLength(){
        return length;
    }
    public void setLength(){
        this.length = length;
    }
    public String getColor(){
        return color;
    }
    public void setColor(){
        this.color = color;
    }
    public double getArea(){
        return width * length;
    }
    public String toString(){
        return "Rectangle[length=" + length + ",width=" + width + ",color=" + color + "]";
    }
}

class Cuboid extends Rectangle2{
    private double height;

    public Cuboid(){
        super();
        this.height = 1;
    }
    public Cuboid(double width, double length){
        super(width, length);
        this.height = 1;
    }
    public Cuboid(double width, double length, double height){
        super(width, length);
        this.height = height;
    }
    public Cuboid(double width, double length, double height, String color){
        super(width, length, color);
        this.height = height;
    }
    public double getHeight(){
        return height;
    }
    public void setHeight(){
        this.height = height;
    }
    public double getVolume(){
        return getArea() * height;
    }
    public double getSurfaceArea(){
        return 2 * (getArea() + getWidth() * getHeight() + getLength() * getHeight());
    }
    public String toString(){
        return "Cuboid[height=" + height + "," + super.toString() + "]";
    }
}