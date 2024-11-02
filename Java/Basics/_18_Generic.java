import java.util.List;

class Box<T> {
    private T item;

    public void setItem(T item) {
        this.item = item;
    }
    public T getItem(){
        return item;
    }
}
class BoundedEx<T extends Number> {
    public static <T extends Number> double sumNum(T num1, T num2) {
        return num1.doubleValue() + num2.doubleValue();
    }

}
public class _18_Generic {
    public static void printList(List<?> list) {
        for (Object element : list) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
    public static <T> void printArray(T[] array){
        for (T element : array){
            System.out.println(element + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Box<Integer> intBox = new Box<>();
        intBox.setItem(20);
        Box<String> strBox = new Box<>();
        strBox.setItem("BK");
        System.out.println(intBox.getItem() + " " + strBox.getItem());
        
        Integer[] intArray = {1, 2, 3, 4};
        String[] strArray = {"A", "B", "C"};
        printArray(intArray);
        printArray(strArray);
        
        System.out.println(BoundedEx.sumNum(3, 4));   
        System.out.println(BoundedEx.sumNum(3.12, 4.56));   

        List<Integer> intList = List.of(1, 2, 3);
        List<String> strList = List.of("A", "B", "C");
        printList(intList); 
        printList(strList); 
    }    
}
