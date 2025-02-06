import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class _5_JTextField extends JFrame {
    private JTextField textField;
    private JTextArea textArea;

    public _5_JTextField() {
        setTitle("JTextField and JTextArea Methods Demo");
        setSize(500, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(0, 2, 10, 10));

        textField = new JTextField("Initial Text", 20);
        textField.setHorizontalAlignment(JTextField.CENTER);
        panel.add(new JLabel("JTextField:"));
        panel.add(textField);

        textArea = new JTextArea("Initial Multi-Line Text\nLine 2\nLine 3", 5, 20);
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);
        JScrollPane scrollPane = new JScrollPane(textArea);
        panel.add(new JLabel("JTextArea:"));
        panel.add(scrollPane);

        panel.add(createButton("Set JTextField Text", e -> textField.setText("New Text")));
        panel.add(createButton("Get JTextField Text", e -> showMessage("TextField Text: " + textField.getText())));
        panel.add(createButton("Set Columns", e -> textField.setColumns(30)));
        panel.add(createButton("Get Columns", e -> showMessage("TextField Columns: " + textField.getColumns())));
        panel.add(createButton("Set Editable", e -> textField.setEditable(false)));
        panel.add(createButton("Get Editable", e -> showMessage("TextField Editable: " + textField.isEditable())));
        panel.add(createButton("Set Alignment", e -> textField.setHorizontalAlignment(JTextField.RIGHT)));
        panel.add(createButton("Select Text", e -> textField.select(0, textField.getText().length())));
        panel.add(createButton("Get Selected Text", e -> showMessage("Selected Text: " + textField.getSelectedText())));
        panel.add(createButton("Set Caret Position", e -> textField.setCaretPosition(2)));
        panel.add(createButton("Get Caret Position", e -> showMessage("Caret Position: " + textField.getCaretPosition())));

        panel.add(createButton("Set JTextArea Text", e -> textArea.setText("New Multi-line Text\nLine 2\nLine 3")));
        panel.add(createButton("Get JTextArea Text", e -> showMessage("TextArea Text: " + textArea.getText())));
        panel.add(createButton("Append Text", e -> textArea.append("\nAppended Line")));
        panel.add(createButton("Insert Text", e -> textArea.insert("Inserted Line\n", 0)));
        panel.add(createButton("Replace Range", e -> textArea.replaceRange("Replaced", 0, 5)));
        panel.add(createButton("Set Rows", e -> textArea.setRows(10)));
        panel.add(createButton("Get Rows", e -> showMessage("TextArea Rows: " + textArea.getRows())));
        panel.add(createButton("Set Columns", e -> textArea.setColumns(25)));
        panel.add(createButton("Get Columns", e -> showMessage("TextArea Columns: " + textArea.getColumns())));
        panel.add(createButton("Set Line Wrap", e -> textArea.setLineWrap(false)));
        panel.add(createButton("Set Wrap Style Word", e -> textArea.setWrapStyleWord(false)));
        panel.add(createButton("Select All Text", e -> textArea.selectAll()));
        panel.add(createButton("Get Selected Text", e -> showMessage("Selected Text: " + textArea.getSelectedText())));
        panel.add(createButton("Set Caret Position", e -> textArea.setCaretPosition(10)));
        panel.add(createButton("Get Caret Position", e -> showMessage("Caret Position: " + textArea.getCaretPosition())));
        panel.add(createButton("Set Tab Size", e -> textArea.setTabSize(8)));
        panel.add(createButton("Get Tab Size", e -> showMessage("Tab Size: " + textArea.getTabSize())));

        add(panel, BorderLayout.CENTER);
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
            _5_JTextField frame = new _5_JTextField();
            frame.setVisible(true);
        });
    }
}

