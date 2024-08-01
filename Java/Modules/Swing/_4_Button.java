import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class _4_Button {
    public static void main(String[] args){
        new MyFrame();
    }
}

class MyFrame extends JFrame implements ActionListener {
    JButton button;
    MyFrame(){
        button = new JButton();
        button.setBounds(0,0,350,100);
        button.setText("Click me");
        button.addActionListener(this);
        button.setFocusable(false);
        //button.addActionListener(e-> {
        //    System.out.println("Button Clicked");
        //});
        this.setLayout(null);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(500,500);
        this.setVisible(true);
        this.add(button);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == button){
            System.out.println("Button Clicked");
        }
    }
}

