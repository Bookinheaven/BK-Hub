import java.awt.*;
import java.awt.event.ActionListener;
import javax.swing.*;

public class _6_RadioCheckCombo extends JFrame {
    private JCheckBox checkBox;
    private JRadioButton option1;
    private JRadioButton option2;
    private JComboBox<String> comboBox;

    public _6_RadioCheckCombo() {
        setTitle("JCheckBox, JRadioButton, JComboBox Demo");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(0, 2, 10, 10));

        checkBox = new JCheckBox("Accept Terms");
        add(checkBox);

        option1 = new JRadioButton("Option 1");
        option2 = new JRadioButton("Option 2");
        
        ButtonGroup group = new ButtonGroup();
        group.add(option1);
        group.add(option2);
        
        add(option1);
        add(option2);

        comboBox = new JComboBox<>(new String[]{"Item 1", "Item 2", "Item 3"});
        add(new JLabel("Select an item:")); 
        add(comboBox);

        add(createButton("Check Checkbox", e -> showMessage("Checkbox is " + (checkBox.isSelected() ? "checked" : "unchecked"))));
        add(createButton("Get Radio Button", e -> {
            String selected = option1.isSelected() ? "Option 1" : (option2.isSelected() ? "Option 2" : "None");
            showMessage("Selected Radio Button: " + selected);
        }));
        add(createButton("Get ComboBox Selection", e -> showMessage("Selected ComboBox Item: " + comboBox.getSelectedItem())));
    }

    private JButton createButton(String label, ActionListener listener) {
        JButton button = new JButton(label);
        button.addActionListener(listener);
        return button;
    }

    private void showMessage(String message) {
        JOptionPane.showMessageDialog(this, message);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            _6_RadioCheckCombo frame = new _6_RadioCheckCombo();
            frame.setVisible(true);
        });
    }
}
