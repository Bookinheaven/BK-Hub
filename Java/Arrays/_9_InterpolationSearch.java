import java.util.Arrays;

public class _9_InterpolationSearch {
    private static int interpolationSearch(int arr[], int value){
        int high = arr.length - 1;
        int low = 0; 
        while(arr[low] <= value && arr[high] >= value && high >= low){
            int probe = low + (high - low) * (value - arr[low]) / (arr[high]- arr[low]);
            if(arr[probe] == value){
                return probe;
            }
            else if(arr[probe] < value){
                low = probe + 1;
            } else {
                low = probe - 1;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        int arr[] = new int[]{1,2,3,4,5,6,7,8};
        int index = interpolationSearch(arr, 5);
        System.out.println(Arrays.toString(arr));
        System.out.println(index);
    }    
}
