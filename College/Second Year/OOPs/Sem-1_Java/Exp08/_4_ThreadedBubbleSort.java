import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class _4_ThreadedBubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static int[] mergeSortedArrays(List<int[]> sortedSubArrays) {
        int totalLength = sortedSubArrays.stream().mapToInt(arr -> arr.length).sum();
        int[] mergedArray = new int[totalLength];
        int[] indices = new int[sortedSubArrays.size()];
        for (int i = 0; i < totalLength; i++) {
            int minIndex = -1;
            int minValue = Integer.MAX_VALUE;
            for (int j = 0; j < sortedSubArrays.size(); j++) {
                if (indices[j] < sortedSubArrays.get(j).length && sortedSubArrays.get(j)[indices[j]] < minValue) {
                    minValue = sortedSubArrays.get(j)[indices[j]];
                    minIndex = j;
                }
            }
            mergedArray[i] = minValue;
            indices[minIndex]++;
        }
        return mergedArray;
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Tanvik URK23CS1261");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] inputArray = new int[n];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            inputArray[i] = scanner.nextInt();
        }
        System.out.print("Enter the number of threads: ");
        int numThreads = scanner.nextInt();

        int subArraySize = inputArray.length / numThreads;

        List<int[]> subArrays = new ArrayList<>();
        for (int i = 0; i < numThreads; i++) {
            int start = i * subArraySize;
            int end = (i == numThreads - 1) ? inputArray.length : start + subArraySize;
            subArrays.add(Arrays.copyOfRange(inputArray, start, end));
        }

        List<Thread> threads = new ArrayList<>();
        for (int i = 0; i < numThreads; i++) {
            final int index = i;
            Thread thread = new Thread(() -> {
                bubbleSort(subArrays.get(index));
                System.out.println("Thread " + index + " finished sorting: " + Arrays.toString(subArrays.get(index)));
            });
            threads.add(thread);
            thread.start();
        }

        for (Thread thread : threads) {
            thread.join();
        }

        Thread mergeThread = new Thread(() -> {
            int[] sortedArray = mergeSortedArrays(subArrays);
            System.out.println("Merged sorted array: " + Arrays.toString(sortedArray));
        });
        mergeThread.start();
        mergeThread.join();  
        scanner.close();
    }
}
