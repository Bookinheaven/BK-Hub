import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;

public class _11_Choose {
    public static void setup(){
        JFrame frame = new JFrame();
        frame.setLayout(new BorderLayout());
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        JLabel userLabel = new JLabel("Please choose your favorite language:");
        
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(0, 20, 5, 20);
        gbc.anchor = GridBagConstraints.WEST;

        panel.add(userLabel, gbc);
        
        JRadioButton b1 = new JRadioButton("Java");
        Opened(b1);
        JRadioButton b2 = new JRadioButton("Python");
        Opened(b2);
        JRadioButton b3 = new JRadioButton("SQL");
        Opened(b3);
        
        ButtonGroup BG = new ButtonGroup();
        BG.add(b1);
        BG.add(b2);
        BG.add(b3);
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.insets = new Insets(0, 20, 5, 20);
        panel.add(b1, gbc);
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.insets = new Insets(0, 20, 5, 20);
        panel.add(b2, gbc);
        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.insets = new Insets(0, 20, 5, 20);
        panel.add(b3, gbc);
        

        frame.add(panel);
        frame.setSize(new Dimension(400,400));
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setVisible(true);
    }
    public static void Opened(JRadioButton b) {
    	b.addActionListener(new ActionListener() {
    		@Override
    		public void actionPerformed(ActionEvent e) {
    			JOptionPane.showMessageDialog(null,  "The %s option has been selected".formatted(b.getText()), "Message", JOptionPane.INFORMATION_MESSAGE);
    		}
    		
    	});
    }
    public static void main(String[] args) {
        setup();
    }    
}