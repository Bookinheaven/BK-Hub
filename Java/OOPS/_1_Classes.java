public class _1_Classes {
    public static void main(String[] args) {
        Car car1 = new Car("Toyota", 2020, "Red");
        Car car2 = new Car("Honda", 2018, "Blue");

        car1.displayInfo();
        car2.displayInfo();
    }    
}
class Car {
    // Attributes
    String model;
    int year;
    String color;

    // Constructor
    public Car(String model, int year, String color) {
        this.model = model;
        this.year = year;
        this.color = color;
    }

    // Method
    public void displayInfo() {
        System.out.println("Model: " + model + ", Year: " + year + ", Color: " + color);
    }
}