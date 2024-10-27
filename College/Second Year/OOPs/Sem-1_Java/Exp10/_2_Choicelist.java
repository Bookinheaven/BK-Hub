
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;

import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class _2_Choicelist {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(()-> {
            JFrame frame = new JFrame();
            frame.setSize(new Dimension(400,400));
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.getContentPane().setBackground(Color.PINK);
            frame.setLocationRelativeTo(null);
            frame.setTitle("COMBO LIST");

            JPanel panel = new JPanel(new GridBagLayout());
            GridBagConstraints gbc = new GridBagConstraints();
            panel.setOpaque(false);

            JLabel subjectLabel = new JLabel("Select Subject");
            JComboBox subjects = new JComboBox<>(new String[]{"DATABASE MANAGEMENT SYSTEM", "JAVA","Python"});

            JLabel nameLabel = new JLabel("Select Name");
            JTextField result = new JTextField();
            result.setEditable(false);
            result.setText(subjects.getSelectedItem().toString());

            subjects.addActionListener((ActionEvent e)->{
                result.setText(subjects.getSelectedItem().toString());
            });
            gbc.gridx = 0;
            gbc.gridy = 0;
            gbc.anchor = GridBagConstraints.EAST;

            gbc.insets = new Insets(10, 10, 10, 10);
            panel.add(subjectLabel, gbc);

            gbc.gridx = 1;
            gbc.gridy = 0;
            gbc.anchor = GridBagConstraints.WEST;

            panel.add(subjects, gbc);
            gbc.gridx = 0;
            gbc.gridy = 1;
            gbc.anchor = GridBagConstraints.EAST;
            gbc.fill = GridBagConstraints.NONE;

            panel.add(nameLabel, gbc);
            gbc.gridx = 1;
            gbc.gridy = 1;
            gbc.fill = GridBagConstraints.HORIZONTAL;

            gbc.anchor = GridBagConstraints.WEST;

            panel.add(result, gbc   );

            frame.add(panel);


            frame.setVisible(true);
        });
    }    
}
