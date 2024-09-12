import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Properties;

public class _3_props {
    private static void createprops(String filename){
        Properties props = new Properties();
        try (FileOutputStream output = new FileOutputStream(filename)) {
            props.setProperty("username", "admin");
            props.setProperty("password", "124");
            props.store(output, "User Configuration");
            System.out.println("Properties file created.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static void accessprops(String filename){
        Properties props = new Properties();
        try (FileInputStream input = new FileInputStream(filename)) {
            props.load(input);
            String username = props.getProperty("username");
            String password = props.getProperty("password");

            System.out.println("Username: " + username);
            System.out.println("Password: " + password);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        createprops("config.properties");
        accessprops("config.properties");
        
    }
}
