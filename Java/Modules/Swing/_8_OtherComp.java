import java.awt.*;
import javax.swing.*;

public class _8_OtherComp extends JFrame {

    public _8_OtherComp() {
        setTitle("Menu, Tabbed Pane, Toolbar, and Scrollable Pane Demo");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JMenuBar menuBar = new JMenuBar();
        
        JMenu fileMenu = new JMenu("File");
        JMenuItem openItem = new JMenuItem("Open");
        openItem.addActionListener(e -> showMessage("Open menu item clicked"));
        fileMenu.add(openItem);
        fileMenu.addSeparator();
        JMenuItem exitItem = new JMenuItem("Exit");
        exitItem.addActionListener(e -> System.exit(0));
        fileMenu.add(exitItem);
        menuBar.add(fileMenu);

        JMenu editMenu = new JMenu("Edit");
        JMenuItem copyItem = new JMenuItem("Copy");
        copyItem.addActionListener(e -> showMessage("Copy menu item clicked"));
        editMenu.add(copyItem);
        menuBar.add(editMenu);
        
        setJMenuBar(menuBar);

        JToolBar toolBar = new JToolBar();
        JButton newButton = new JButton("New");
        newButton.addActionListener(e -> showMessage("New button clicked"));
        toolBar.add(newButton);
        toolBar.addSeparator();
        JButton saveButton = new JButton("Save");
        saveButton.addActionListener(e -> showMessage("Save button clicked"));
        toolBar.add(saveButton);
        add(toolBar, BorderLayout.NORTH);

        JTabbedPane tabbedPane = new JTabbedPane();
        tabbedPane.add("Tab 1", createScrollablePanel("Content for Tab 1"));
        tabbedPane.add("Tab 2", createScrollablePanel("Content for Tab 2"));
        tabbedPane.add("Tab 3", createScrollablePanel("Content for Tab 3"));
        add(tabbedPane, BorderLayout.CENTER);
    }

    private JPanel createScrollablePanel(String content) {
        JPanel panel = new JPanel();
        panel.add(new JLabel(content));
        
        JTextArea textArea = new JTextArea(10, 30);
        textArea.setText("Editable text area in " + content);
        JScrollPane scrollPane = new JScrollPane(textArea);
        panel.add(scrollPane);
        
        return panel;
    }

    private void showMessage(String message) {
        JOptionPane.showMessageDialog(this, message);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            _8_OtherComp frame = new _8_OtherComp();
            frame.setVisible(true);
        });
    }
}
