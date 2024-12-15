
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _9_ReaderWriter {
    public static void main(String[] args) throws IOException {
        InputStreamReader fs = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(fs);
        System.out.println("Enter your name");
        String name = br.readLine();
        System.out.println("Hello, "+ name+ "!");        
    }    
}
