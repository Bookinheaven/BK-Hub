import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;

public class _2_Labels {
    public static void main(String[] args) {
        JLabel label = new JLabel();
        //ImageIcon image = new ImageIcon("path");
        label.setText("Im Burn");
        Border border = BorderFactory.createLineBorder(Color.BLUE, 3);
        //label.setIcon(image);
        //label.setIconTextGap(10);
        label.setHorizontalTextPosition(JLabel.CENTER);
        label.setFont(new Font("MV Boli",Font.PLAIN,20));
        label.setForeground(new Color(0x00FF00));
        label.setHorizontalAlignment(JLabel.CENTER);
        label.setOpaque(true);
        label.setBackground(new Color(0xFFF01F));
        label.setBorder(border);
        label.setVerticalAlignment(JLabel.CENTER);
//        label.setBounds(0, 0, 250, 250);


        JFrame frame = new JFrame();
        frame.add(label);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,400);
//        frame.setLayout(null);
        frame.pack();
        frame.setVisible(true);
    }
}