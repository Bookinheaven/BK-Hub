import java.util.Scanner;

public class F5 {
	 public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int arr1[],arr2[];

        System.out.println("Enter array 1 size");
        int arr1_size = sc.nextInt();
        arr1 = new int[arr1_size];
        System.out.println("Enter array elements");
        for(int i=0; i<arr1.length; i++){
            arr1[i]= sc.nextInt();
        }

        System.out.println("Enter array 2 size");
        int arr2_size = sc.nextInt();
        arr2 = new int[arr2_size];
        System.out.println("Enter array elements");
        for(int i=0; i<arr2.length; i++){
            arr2[i]= sc.nextInt();
        }
        System.out.println("Common elements");
         for(int i=0; i<arr1.length; i++){
            for(int j=0; j<arr2.length; j++){
                if (arr1[i] == arr2[j]){
                    System.out.print(arr1[i] + ", ");
                }
            }
         }
         sc.close();
    }
}
