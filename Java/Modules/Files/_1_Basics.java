
import java.io.File;
import java.io.IOException;

public class _1_Basics {
    private static void createFile(String filename){
        File file = new File(filename);
        try {
            if(file.createNewFile()) {
                System.out.println("File Created "+file.getName());
            } else {
                System.out.println("File already exists.");
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static void accessFile(String filename){
        File file = new File(filename);
        if(file.exists()){
            System.out.println("File name: " + file.getName());
            System.out.println("File path: " + file.getAbsolutePath());
            System.out.println("Writable: " + file.canWrite());
            System.out.println("Readable: " + file.canRead());
            System.out.println("File size: " + file.length() + " bytes");
        } else {
            System.out.println("The file does not exist.");
        }
    }
    private static void deleteFile(String filename){
        File file = new File(filename);

        if (file.delete()) {
            System.out.println("Deleted the file: " + file.getName());
        } else {
            System.out.println("Failed to delete the file.");
        }
    }
    public static void main(String[] args) {
        createFile("ex.txt");
        accessFile("ex.txt");
        deleteFile("ex.txt");

    }
}
