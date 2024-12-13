
import java.io.FileInputStream;
import java.io.IOException;

public class _8_ByteReader {
    public static void main(String[] args) {
        String filePath = "example.txt";
        try (FileInputStream fis = new FileInputStream(filePath);){
            int byteData;
            while((byteData = fis.read()) != -1){
                System.out.println((char)byteData);
            }
        } catch (IOException e){
            e.printStackTrace();
        } 
    }
}