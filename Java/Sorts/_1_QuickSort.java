
class _1_QuickSort{
    public static void main(String[] args) {
        int[] arr = {5, 3, 2, 6, 4, 1, 3, 7};
        int n = arr.length;
        quickSort(arr, 0, n - 1);
        for (int val : arr) {
            System.out.print(val + " ");  
        }
    }
    private static void quickSort(int arr[], int low, int high){
        if (low < high){
            int part = partition(arr, low, high);
            quickSort(arr, low, part - 1);
            quickSort(arr, part + 1, high);
        } 
    }
    private static int partition(int arr[], int low, int high){
        int pivot = arr[high];
        int i = low -1;
        for(int j = low; j < high; j++){
            if(arr[j]<pivot){
                i++;
                swap(arr, i, j);
            }
        }
        for (int val : arr) {
            System.out.print(val + " ");  
        }
        System.out.println();  
        i++;
        swap(arr, i, high);
        return i;
    }
    private static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i]= arr[j];
        arr[j] = temp;
    }

}