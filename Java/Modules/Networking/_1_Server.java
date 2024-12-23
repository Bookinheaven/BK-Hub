import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
public class _1_Server {
    public static void main(String[] args) {
        try (ServerSocket ss = new ServerSocket(1234);){
            Socket con = ss.accept();
            BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            while (true){
                String data = br.readLine();
                System.out.println("Message: "+data);
            }
        } catch (Exception e){
            e.printStackTrace();
        }
    }
}
