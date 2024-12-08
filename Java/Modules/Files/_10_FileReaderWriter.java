
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
public class _10_FileReaderWriter {
    public static void main(String[] args) {
        String fileIn = "file1.txt";
        String fileOut = "file2.txt";
        try (
            FileWriter fs = new FileWriter(fileOut);
            FileReader fr = new FileReader(fileIn);
        ) {
            int chat;
            while((chat = fr.read())!=-1){
                System.out.println((char)chat);
                fs.write(chat);
            }
                
        } catch (IOException e){
            e.printStackTrace();
        }
    }    
}
