public class _6_InsertionSort {
    private static void insertionSort(int[] arr){
        for (int i = 1; i < arr.length; i++) {
            int temp = arr[i];
            int j = i - 1;
            
            while (j >= 0 && arr[j] > temp){
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
    }
    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        insertionSort(arr);

        for (int val : arr) {
            System.out.print(val + " ");  
        }
    }    
}
