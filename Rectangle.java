public class Rectangle {
    private double width;
    private double height;


    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    
    public double getArea() {
        return width * height;
    }

    
    public double getPerimeter() {
        return 2 * (width + height);
    }

    
    public void display() {
        System.out.println("Largeur du rectangle : " + width);
        System.out.println("Hauteur du rectangle : " + height);
        System.out.println("Aire : " + getArea());
        System.out.println("Périmètre : " + getPerimeter());
    }
}
