public class _7_SelectionSort {
    private static void selectionSort(int[] arr){
        for(int i = 0; i < arr.length - 1; i++){
            int min = i;
            for(int j = i+1; j < arr.length; j++){
                if (arr[j] < arr[min]){
                    min = j;
                }
            }
            if (min != i) { 
                int temp = arr[i];
                arr[i] = arr[min];
                arr[min] = temp;
            }
        }
    }
    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        selectionSort(arr);

        for (int val : arr) {
            System.out.print(val + " ");  
        }
    }        
}
