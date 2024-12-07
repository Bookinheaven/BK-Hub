import java.util.LinkedList;
import java.util.SequencedCollection;

public class _4_SequencedCollection {
    public static void main(String[] args) {
        SequencedCollection<String> names = new LinkedList<>();

        names.addFirst("Tanvik");
        names.addLast("Dharvik");
        names.addLast("Gidi");

        System.out.println(names.getFirst()); 
        System.out.println(names.getLast()); 

        names.removeFirst();
        System.out.println(names.getFirst());

        SequencedCollection<String> reversedNames = names.reversed();
        reversedNames.forEach(System.out::println);
    }
}

