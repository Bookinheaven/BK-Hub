import java.util.ArrayList;
import java.util.Scanner;

public class _6_Matrix {
    
    public static int[][] addition(ArrayList<int[][]> arrays) {
        if (arrays.size() < 2) {
            System.out.println("Need at least two matrices for addition.");
            return null;
        }
        int[][] result = arrays.get(0);
        int rows = result.length;
        int columns = result[0].length;

        for (int i = 1; i < arrays.size(); i++) {
            int[][] matrix = arrays.get(i);
            if (matrix.length != rows || matrix[0].length != columns) {
                System.out.println("Matrices dimensions do not match for addition.");
                return null;
            }
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < columns; col++) {
                    result[row][col] += matrix[row][col];
                }
            }
        }
        return result;
    }

    public static int[][] transpose(int[][] matrix) {
        int rows = matrix.length;
        int columns = matrix[0].length;
        int[][] transposed = new int[columns][rows]; 

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < columns; col++) {
                transposed[col][row] = matrix[row][col];
            }
        }
        return transposed;
    }
    public static int[][] multiplication(ArrayList<int[][]> arrays) {
        if (arrays.size() < 2) {
            System.out.println("Need at least two matrices for multiplication.");
            return null;
        }
        int[][] result = arrays.get(0);
        for (int i = 1; i < arrays.size(); i++) {
            int[][] matrix = arrays.get(i);
            if (result[0].length != matrix.length) {
                System.out.println("Matrices dimensions do not match for multiplication.");
                return null;
            }
            int[][] tempResult = new int[result.length][matrix[0].length];

            for (int row = 0; row < result.length; row++) {
                for (int col = 0; col < matrix[0].length; col++) {
                    for (int k = 0; k < result[0].length; k++) {
                        tempResult[row][col] += result[row][k] * matrix[k][col];
                    }
                }
            }
            result = tempResult;
        }
        return result;
    }

    public static void display(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of matrices: ");    
        int arraysSize = sc.nextInt();
        ArrayList<int[][]> arrays = new ArrayList<>();

        for (int i = 0; i < arraysSize; i++) {
            System.out.print("Enter the number of rows for matrix " + (i + 1) + ": ");    
            int rows = sc.nextInt();
            System.out.print("Enter the number of columns for matrix " + (i + 1) + ": ");  
            int columns = sc.nextInt();
            int[][] arr = new int[rows][columns];
            System.out.println("Enter elements for matrix " + (i + 1) + ":");
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < columns; col++) {
                    System.out.print("Element (r: " + (row + 1) + " c: " + (col + 1) + "): ");
                    arr[row][col] = sc.nextInt();
                }
            }
            arrays.add(arr);
        }

        int[][] result = addition(arrays);
        if (result != null) {
            System.out.println("Resultant matrix after addition:");
            display(result);
        }

        int[][] resultM = multiplication(arrays);
        if (resultM != null) {
            System.out.println("Resultant matrix after multiplication:");
            display(resultM);
        }
        
        int [][]transpose = transpose(resultM);
        System.out.println("Resultant matrix after transpose:");
        display(transpose);

        sc.close();
    }   
}
