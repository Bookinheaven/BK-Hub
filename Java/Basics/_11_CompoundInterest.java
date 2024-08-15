import java.util.Scanner;
import java.lang.Math;
public class _11_CompoundInterest {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the Principal: ");
        int p = sn.nextInt();
        System.out.print("Enter the Time period: ");
        int t = sn.nextInt();
        System.out.print("Enter the rate (without %): ");
        Float r = sn.nextFloat();
        double result = compoundInterest(p, t, r);
        System.out.printf("Compound interest = %.2f%%", result);
        sn.close();
    }  
    public static double compoundInterest(int p, int t, float r){
        return (p * Math.pow((1 + (r / 100)), t)) - p;
    }       
}
