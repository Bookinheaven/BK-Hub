import javax.swing.*;
import java.awt.*;

public class _3_Panels {
    public static void main(String[] args) {

        JLabel label = new JLabel();
        label.setText("Hi");

        JPanel rpanel = new JPanel();
        rpanel.setBackground(Color.red);
        rpanel.setBounds(0,0,250,250);

        JPanel bpanel = new JPanel();
        bpanel.setBackground(Color.blue);
        bpanel.setBounds(250,0,250,250);

        JPanel gpanel = new JPanel();
        gpanel.setBackground(Color.green);
        gpanel.setBounds(0,250,500,250);

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(750,750);
        frame.setLayout(null);
        rpanel.add(label);
        frame.add(rpanel);
        frame.add(bpanel);
        frame.add(gpanel);
        frame.setVisible(true);
    }
}