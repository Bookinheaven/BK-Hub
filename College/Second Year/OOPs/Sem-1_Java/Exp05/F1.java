import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

class Employee {
	int bs;
	double dp;
	double hra;
	double tax;
	int epf;
	double CalculateGross() {return 0.00;}
	double netSalary() { return 0.00;}
	double taxCal() {return 0.00;}
}
class Job extends Employee {
	Job(int bs, double dp, double hra, double tax,int epf){
		this.bs = bs;
		this.dp = dp;
		this.hra = hra;
		this.tax = tax;
		this.epf = epf;
	}
	double CalculateGross() {
		return (double)(bs + (bs * (dp/100))+ (bs * (hra/100))- (bs * (tax/100)) - epf);
	}
	double netSalary() {
		return (double)(bs + (bs * (dp/100))+ (bs * (hra/100)));
	}
	double taxCal() {
		return (double)(bs * (tax/100));
	}
}
public class F1 {
	private static Map<String, Object> takeIn(Scanner sc) {
		Map<String, Object> map = new TreeMap<String, Object>();
		System.out.print("Enter the Basic Salary: ");
		int bs = sc.nextInt();
		map.put("bs", bs);
		System.out.print("Enter the DA Pay: ");
		double dp = sc.nextInt();
		map.put("dp", dp);
		System.out.print("Enter the HRA: ");
		double hra = sc.nextInt();
		map.put("hra", hra);
		System.out.print("Enter the tax: ");
		double tax = sc.nextInt();
		map.put("tax", tax);
		System.out.print("Enter the epf: ");
		int epf = sc.nextInt();
		map.put("epf", epf);
		
		return map;
		
	}
	public static void main(String args[]) {
		System.out.println("Tanvik Sri Ram .R => URK23CS1261");
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.print("Menu\nChoose the Group\n1.Manager\n2.Engineer\n3.Exit\nchoice: ");
			int choice = sc.nextInt();
			switch (choice) {
			case 1 , 2:
				Map<String, Object> map= takeIn(sc);
				while (true) {
					System.out.print("Choose:\n1.Calculate Gross Salary\n2.Calculate Net Salary\n3.Calculate Tax\n4.Print the Pay Details\n5.Quit\nChoice: ");
					int choice1 = sc.nextInt();
					Job man = new Job((int)map.get("bs"),(double)map.get("dp"),(double)map.get("hra"),(double)map.get("tax"),(int)map.get("epf"));
					double cs = man.CalculateGross();
					double ns = man.netSalary();
					double tax = man.taxCal();
					switch(choice1) {
					case 1:
						System.out.print("\nGross : %.2f\n".formatted(cs));
						break;
					case 2:
						System.out.print("\nNet Salary : %.2f\n".formatted(ns));
						break;
					case 3:
						System.out.print("\nTax : %.2f\n".formatted(tax));
						break;
					case 4:
					
						System.out.print("\nGross : %.2f\nNet Salary : %.2f\nTax : %.2f\n".formatted(cs,ns, tax));
						break;
					case 5:
						System.out.print("Quit");
						sc.close();
						System.exit(0);
					}			
				}
			case 3:
				System.out.print("Quit");
				sc.close();
				System.exit(0);
			}
		}
	}
}
