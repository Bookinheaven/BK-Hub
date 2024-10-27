
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

public class _1_ThreeButtons{
    public static void main(String[] args) {
        SwingUtilities.invokeLater(()-> {
            JFrame frame = new JFrame();
            frame.setSize(new Dimension(400,180));
            frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            frame.setTitle("Button");
            frame.setLocationRelativeTo(null);

              JPanel panel = new JPanel();
            panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

            JButton yesButton = new JButton("YES");
            yesButton.setFont(new Font("Arial", Font.PLAIN, 20));

            JButton noButton = new JButton("No");
            noButton.setFont(new Font("Arial", Font.PLAIN, 20));

            JButton closeButton = new JButton("CLOSE");
            closeButton.setFont(new Font("Arial", Font.PLAIN, 20));

            JLabel result = new JLabel(" ");
            result.setFont(new Font("Arial", Font.PLAIN, 15));

            yesButton.setMaximumSize(new Dimension(Integer.MAX_VALUE, yesButton.getMinimumSize().height));
            noButton.setMaximumSize(new Dimension(Integer.MAX_VALUE, noButton.getMinimumSize().height));
            closeButton.setMaximumSize(new Dimension(Integer.MAX_VALUE, closeButton.getMinimumSize().height));

            yesButton.addActionListener((ActionEvent e) -> result.setText("Button Yes is pressed"));
            noButton.addActionListener((ActionEvent e) -> result.setText("Button No is pressed"));
            closeButton.addActionListener((ActionEvent e) -> System.exit(0));

            panel.add(yesButton);
            panel.add(noButton);
            panel.add(closeButton);
            panel.add(result);

            frame.setLayout(new BorderLayout());
            frame.add(panel, BorderLayout.CENTER);
            frame.setVisible(true);
        });
        
    }
}