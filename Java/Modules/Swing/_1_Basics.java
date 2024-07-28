import javax.swing.*;
import java.awt.*;

public class _1_Basics {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        JFrame frame = new JFrame();
        frame.setTitle("APP");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //ImageIcon image = new ImageIcon("path");
        //frame.setIconImage(image.getImage());
        frame.getContentPane().setBackground(Color.red);
        frame.getContentPane().setBackground(new Color(50,150,140));
        frame.setResizable(false);
        frame.setSize(430,430);
        frame.setVisible(true);
    }
}