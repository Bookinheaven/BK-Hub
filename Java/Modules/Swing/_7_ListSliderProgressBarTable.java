import java.awt.*;
import java.awt.event.ActionListener;
import javax.swing.*;

public class _7_ListSliderProgressBarTable extends JFrame {
    private JList<String> list;
    private JSlider slider;
    private JProgressBar progressBar;
    private JTable table;

    public _7_ListSliderProgressBarTable() {
        setTitle("JList, JSlider, JProgressBar, JTable Demo");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(0, 2, 10, 10));

        list = new JList<>(new String[]{"Item A", "Item B", "Item C", "Item D", "Item E"});
        add(new JLabel("Select an Item:"));
        add(new JScrollPane(list));

        slider = new JSlider(0, 100, 50);
        slider.setMajorTickSpacing(20);
        slider.setPaintTicks(true);
        slider.setPaintLabels(true);
        add(new JLabel("Adjust the Value:"));
        add(slider);

        progressBar = new JProgressBar(0, 100);
        progressBar.setValue(50);
        add(new JLabel("Progress Bar:"));
        add(progressBar);

        String[][] data = {{"1", "Alice"}, {"2", "Bob"}, {"3", "Charlie"}};
        String[] columns = {"ID", "Name"};
        table = new JTable(data, columns);
        add(new JLabel("Data Table:"));
        add(new JScrollPane(table));

        add(createButton("Get List Selection", e -> {
            String selectedValue = list.getSelectedValue();
            showMessage("Selected Item: " + (selectedValue != null ? selectedValue : "None"));
        }));
        
        add(createButton("Get Slider Value", e -> showMessage("Slider Value: " + slider.getValue())));
        
        add(createButton("Set Progress Bar Value", e -> {
            int newValue = slider.getValue(); 
            progressBar.setValue(newValue);
        }));
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
            _7_ListSliderProgressBarTable frame = new _7_ListSliderProgressBarTable();
            frame.setVisible(true);
        });
    }
}
