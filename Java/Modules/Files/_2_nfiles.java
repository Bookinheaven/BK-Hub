
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;



public class _2_nfiles {
    private static void createFile(String filepath){
        Path path = Paths.get(filepath);

        try {
            Files.createFile(path);
            System.out.println("File created: " + path.getFileName());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
        public static void main(String[] args) {
            createFile("ex.txt");
   

    }    
}
