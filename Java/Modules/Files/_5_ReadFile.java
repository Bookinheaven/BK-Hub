import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class _5_ReadFile {
    public static String replaceChar(String data, char[] changeFrom, char changeTo) {
        StringBuilder sb = new StringBuilder(data);
        for (int i = 0; i < sb.length(); i++) {
            for (char c : changeFrom) {
                if (sb.charAt(i) == c) {
                    sb.setCharAt(i, changeTo);
                }
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        File oldFile = new File("Profile.txt");
        try (Scanner sc = new Scanner(oldFile);
        FileWriter fw = new FileWriter("ProfileEdit.txt");){
            ArrayList arr = new ArrayList<String>();
            while(sc.hasNextLine()){
                arr.add(sc.nextLine());
            }
            String modified = replaceChar(String.join("\n", arr), new char[]{'a', 'b'}, '*');
            fw.write(modified);
            fw.flush();

        } catch (Exception e) {
            System.out.println("Error: %s".formatted(e.getMessage()));
        }
    }
}