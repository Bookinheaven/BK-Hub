import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class _3_List {
    public static void main(String[] args) {
        List<String> name = new ArrayList<>(List.of("One", "two", "three", "four", "get", "on", "the", "dance", "floor", "Gidi"));
        name.add("Tanvik");
        name.add("Burn");
        name.remove("One");
        name.forEach(System.out::println);
        // Stream<String> nameStream = name.stream();
        name.stream().filter(n -> ((String) n).length() > 4).map(String::toUpperCase).forEach(System.out::println);
        List<String> saveMe = name.stream().filter(n -> ((String) n).length() > 4).collect(Collectors.toList());
        for (String x : saveMe) {
            System.out.println(x);
        }
        Map<String, Integer> nameLengthMap = name.stream().collect(
            Collectors.toMap(name1 -> name1, name1 -> name1.length())
        );
        System.out.println("Name to Length Map: " + nameLengthMap);

        String joinedString = name.stream()
        .collect(Collectors.joining(", "));

        System.out.println("Joined String: " + joinedString);
    }
}