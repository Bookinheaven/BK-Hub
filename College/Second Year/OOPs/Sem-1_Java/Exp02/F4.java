import java.util.Scanner;

public class F4 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int[][] arr = new int[3][3];
        int[][] transpose_arr = new int[3][3];
        System.out.println("Enter the elements;");
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
            	System.out.print("("+(i+1)+", "+(j+1)+"): ");
                arr[i][j] = sc.nextInt(); 
            }
        }
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
            	System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
                transpose_arr[i][j] = arr[j][i]; 
            }
        }
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
                System.out.print(transpose_arr[i][j] + " ");
            }
            System.out.println();
        }
        sc.close();
    }
    
}