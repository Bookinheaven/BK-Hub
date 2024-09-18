import java.util.Scanner;

class Fuel {
    String fuel_name, state;
    double cost;
    Fuel(String fuel_name, String state, double cost) {
        this.fuel_name = fuel_name;
        this.state = state;
        this.cost = cost;
    }
    double calculateCost(double quantity) {
        return cost * quantity;
    }
}
class Petrol extends Fuel {
    Petrol(String state) {
        super("Petrol", state, switch (state) {
            case "Tamil Nadu" -> 97.46;
            case "Kerala" -> 98.35;
            case "Karnataka" -> 99.61;
            default -> 0;
        });
    }
}
class Diesel extends Fuel {
    Diesel(String state) {
        super("Diesel", state, switch (state) {
            case "Tamil Nadu" -> 96.08;
            case "Kerala" -> 97.37;
            case "Karnataka" -> 98.61;
            default -> 0;
        });
    }
}
class Kerosene extends Fuel {
    Kerosene(String state) {
        super("Kerosene", state, switch (state) {
            case "Tamil Nadu" -> 25.7;
            case "Kerala" -> 26.4;
            case "Karnataka" -> 27.6;
            default -> 0;
        });
    }
}
class AutoLPG extends Fuel {
    AutoLPG(String state) {
        super("Auto LPG", state, switch (state) {
            case "Tamil Nadu" -> 70.33;
            case "Kerala" -> 71.27;
            case "Karnataka" -> 72.08;
            default -> 0;
        });
    }
}
public class F2 {
    public static void main(String[] args) {
        System.out.println("Tanvik Sri Ram .R => URK23CS1261");
        Scanner sc = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("\n===== Fuel Cost Calculator Menu =====");
            System.out.println("1. Calculate Fuel Cost");
            System.out.println("2. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();
            sc.nextLine(); 

            switch (choice) {
                case 1:
                    System.out.print("Enter Customer Name: ");
                    String name = sc.nextLine();
                    System.out.print("Enter State (Tamil Nadu, Kerala, Karnataka): ");
                    String state = sc.nextLine();
                    System.out.print("Enter Fuel Type (Petrol, Diesel, Kerosene, Auto LPG): ");
                    String fuelType = sc.nextLine();
                    System.out.print("Enter Quantity (in liters/kg): ");
                    double quantity = sc.nextDouble();
                    Fuel fuel = switch (fuelType) {
                        case "Petrol" -> new Petrol(state);
                        case "Diesel" -> new Diesel(state);
                        case "Kerosene" -> new Kerosene(state);
                        case "Auto LPG" -> new AutoLPG(state);
                        default -> null;
                    };
                    if (fuel != null) {
                        System.out.printf("\nCustomer: %s\nState: %s\nFuel: %s\nQuantity: %.2f liters/kg\nTotal Cost: ₹%.2f\n",
                                name, fuel.state, fuel.fuel_name, quantity, fuel.calculateCost(quantity));
                    } else {
                        System.out.println("Invalid fuel type or state.");
                    }
                    break;

                case 2:
                    System.out.println("Exiting the program. Goodbye!");
                    exit = true;
                    break;

                default:
                    System.out.println("Invalid choice! Please select option 1 or 2.");
            }
        }

        sc.close();
    }
}
