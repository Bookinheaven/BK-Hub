import java.util.Scanner;

public class _10_SimpleInterest {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the Principal: ");
        int p = sn.nextInt();
        System.out.print("Enter the Time period: ");
        int t = sn.nextInt();
        System.out.print("Enter the rate (without %): ");
        Float r = sn.nextFloat();
        double result = simpleInterest(p, t, r);
        System.out.println("Simple interest = "+result+" %");
        sn.close();
    }  
    public static double simpleInterest(int p, int t, float r){
        return (p * t * r) / 100;
    }   
}
