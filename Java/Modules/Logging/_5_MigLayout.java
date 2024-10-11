import net.miginfocom.swing.MigLayout;
import javax.swing.*;
import java.awt.*;

public class _5_MigLayout {
    public static void main(String[] args) {
        JFrame frame = new JFrame("MigLayout Example 1");
        frame.setLayout(new MigLayout("wrap 3", "[grow,fill]", "[]20[]")); // 3 columns, growing and filling components
        frame.setSize(new Dimension(600, 400));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.add(new JLabel("Name:"), "span 1"); // Takes up 1 cell
        frame.add(new JTextField(15), "span 2");  // Takes up 2 cells, filling the row
        frame.add(new JLabel("Email:"), "span 1");
        frame.add(new JTextField(15), "span 2");
        frame.add(new JButton("Submit"), "span 3, center"); // Button spans 3 columns, centered

        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}