public class _3_MergeSort {
    public static void main(String[] args) {
        int [] arr = {1,5,3,7,9,2,4,8};
        mergeSort(arr);
        for(int x : arr){
            System.out.print(x);
        }
    }
    private static void mergeSort(int[] arr){
        int length = arr.length;
        if(length <= 1) return;
        int middle = length/2;
        int[] leftArr = new int[middle];
        int[] rightArr = new int[length-middle];
        int j = 0;
        for (int i = 0;i<length;i++){
            if(i < middle){
                leftArr[i] = arr[i];
            } else {
                rightArr[j] = arr[i];
                j++;
            }
        }
        mergeSort(leftArr);
        mergeSort(rightArr);
        merge(leftArr, rightArr, arr);
    }
    private static void merge(int[] leftArr, int[] rightArr, int[] array){
        int leftSize = array.length / 2;
        int rightSize = array.length -leftSize;
        int i = 0, l =0, r = 0;
        while (l < leftSize && r < rightSize){
            if(leftArr[l] < rightArr[r]){
                array[i++] = leftArr[l++];
            } else {
                array[i++] = rightArr[r++];
            }
        }
        while (l < leftSize){
            array[i++] = leftArr[l++];
        }
        while (r < rightSize){
            array[i++] = rightArr[r++];
        }
        for(int x : array){
            System.out.print(x);
        }
        System.out.println();
    }
}
