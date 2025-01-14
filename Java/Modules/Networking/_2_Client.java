import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;
public class _2_Client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 1234)) {
            Scanner sc = new Scanner(System.in);
            PrintWriter pr = new PrintWriter(socket.getOutputStream());
            while (true) {
                System.out.println("Enter data: "); 
                String data = sc.nextLine(); 
                pr.println(data);
                pr.flush();
            }
        } catch (Exception e){
            e.printStackTrace();
        }
    }    
}
