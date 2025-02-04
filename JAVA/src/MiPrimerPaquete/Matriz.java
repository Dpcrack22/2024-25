package MiPrimerPaquete;
import java.util.Random;


public class Matriz {

	public static void main(String[] args) {
        int[][] matriz = new int[10][5];
        Random rand = new Random();

        // Llenar la matriz con valores aleatorios
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 5; j++) {
                matriz[i][j] = rand.nextInt(100) + 1; // Números entre 1 y 100
            }
        }

        // Imprimir la matriz
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
}
}
