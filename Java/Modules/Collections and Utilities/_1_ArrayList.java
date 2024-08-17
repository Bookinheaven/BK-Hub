import java.util.ArrayList;

public class _1_ArrayList{
    public static void main(String args[]){
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("Apple");
        arrayList.add("Date");   
        arrayList.add("Mango"); 
        arrayList.get(0);               
        arrayList.set(1, "Blueberry");    
        arrayList.remove(2);             
        arrayList.size();              
        arrayList.isEmpty();            
        arrayList.contains("Apple");
        System.out.println(arrayList);

        for (String fruit : arrayList) {
            System.out.println(fruit);
        }
        
        arrayList.forEach(fruit -> System.out.println(fruit));
        
        for (int i = 0; i < arrayList.size(); i++) {
            System.out.println(arrayList.get(i));
        }
        
    }
}