import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class _10_BasicLogin {
    public static void setup(){
        JFrame frame = new JFrame();
        frame.setLayout(new BorderLayout());
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        JLabel userLabel = new JLabel("Username");
        
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(0, 20, 5, 20);
        panel.add(userLabel, gbc);
        
        JTextField userField = new JTextField(10);
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.insets = new Insets(0, 20, 5, 20);
        panel.add(userField, gbc);
        
        JTextField passField = new JTextField(10);
        gbc.gridx = 1;
        gbc.gridy = 1;
        panel.add(passField, gbc);
        
        JLabel passLabel = new JLabel("Password");
        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(passLabel, gbc);

        JButton button = new JButton("Login");
        gbc.gridx = 1;
        gbc.gridy = 2;
        panel.add(button, gbc);
        
        button.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				String username = userField.getText();
				String password = passField.getText();
				if(username.equals("burn") && password.equals("burn")) {
					JOptionPane.showMessageDialog(frame, "Login Successfull!", "Message", JOptionPane.INFORMATION_MESSAGE);					
				} else {
					JOptionPane.showMessageDialog(frame, "Login Failed!", "Message", JOptionPane.INFORMATION_MESSAGE);
				}
				 
			}

        });
        frame.add(panel);
        frame.setSize(new Dimension(400,400));
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setVisible(true);
    }
    public static void main(String[] args) {
        setup();
    }    
}