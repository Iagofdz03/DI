import javax.swing.*;
import java.awt.*;

public class VentanaColores {

    public static void main(String[] args) {

        // Crear la ventana
        JFrame ventana = new JFrame("Ventana con colores");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setSize(400, 200);

        // Crear panel principal
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());

        // Crear botones
        JButton btnRojo = new JButton("Rojo");
        JButton btnVerde = new JButton("Verde");
        JButton btnAzul = new JButton("Azul");

        // Añadir eventos a los botones
        btnRojo.addActionListener(e -> panel.setBackground(Color.RED));
        btnVerde.addActionListener(e -> panel.setBackground(Color.GREEN));
        btnAzul.addActionListener(e -> panel.setBackground(Color.BLUE));

        // Añadir botones al panel
        panel.add(btnRojo);
        panel.add(btnVerde);
        panel.add(btnAzul);

        // Añadir panel a la ventana
        ventana.add(panel);

        // Hacer visible la ventana
        ventana.setVisible(true);
    }
}
