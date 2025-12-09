import javax.swing.*;
import java.awt.*;

public class MiPrimeraGUI {

    public static void main(String[] args) {

        // Crear ventana (JFrame)
        JFrame ventana = new JFrame("Mi primera GUI");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setSize(350, 150);

        // Crear panel
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout()); // Puedes cambiarlo por GridLayout si quieres

        // Crear componentes
        JLabel label = new JLabel("Escribe tu nombre:");
        JTextField campoTexto = new JTextField(15);
        JButton boton = new JButton("Saludar");

        // Añadir comportamiento al botón
        boton.addActionListener(e -> {
            String nombre = campoTexto.getText().trim();

            if (nombre.isEmpty()) {
                JOptionPane.showMessageDialog(
                        ventana,
                        "El campo está vacío. Por favor, escribe tu nombre.",
                        "Error",
                        JOptionPane.ERROR_MESSAGE
                );
            } else {
                JOptionPane.showMessageDialog(
                        ventana,
                        "Hola, " + nombre + "! Bienvenido/a a tu primera GUI en Java.",
                        "Saludo",
                        JOptionPane.INFORMATION_MESSAGE
                );
            }
        });

        // Añadir componentes al panel
        panel.add(label);
        panel.add(campoTexto);
        panel.add(boton);

        // Añadir panel a la ventana
        ventana.add(panel);

        // Hacer ventana visible
        ventana.setVisible(true);
    }
}
