
import java.io.File;
import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
public class _4_Profile {
    public static void writeText(String filename){
        try {
            File profile = new File(filename);
            if(profile.exists()){    
               FileWriter file = new FileWriter(filename);
                file.write("STEVE JOBS NECK\n");
                file.write("Role: Software Engineer\n");
                file.write("Skills: IDK\n");
                file.flush();
        
            } else {
                System.out.println("File not found!");
            }
        } catch(Exception e){
            e.printStackTrace();
        }
    }
    public static void copyTo(String fileName, String newFileName) {
        try {
            File oldFile = new File(fileName);
            File newFile = new File(newFileName);
            if(oldFile.exists()){
                Files.copy(oldFile.toPath(), newFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
            } 
        } catch(Exception e){
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        writeText("Profile.txt");
        copyTo("Profile.txt", "Profile1.txt");
    }    
}
