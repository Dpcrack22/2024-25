package MiPrimerPaquete;
import java.util.Arrays;
import java.util.Random;


public class Matriz {

	public static void main(String[] args) {
		/*ARRAYS*/
		
		int[][] array=new int[5][10];
		int[][] array1=new int[5][10];
		//String[] array= new String[10];
		//System.out.println(array.length);
		//System.out.println(entrada2);
		
		for (int fila=0; fila<array.length; fila++) {
			for (int columna=0; columna<array[0].length; columna++) {
			array[fila][columna]=(int)(10*Math.random());
		}}
			
		for (int fila=0; fila<array.length; fila++) {
			System.out.println(Arrays.toString(array[fila]));
		}
		System.out.println("*******************************************************************");

		
		for (int fila=0; fila<array1.length; fila++) {
			for (int columna=0; columna<array1[0].length; columna++) {
				for (int i=fila-1; i<=fila+1;i++) {
					for (int j=columna-1; j<=columna+1;j++) {
						if(i>=0 && i<array.length && j>=0 && j<array[0].length && (i !=fila|| j!=columna )) {
							array1[fila][columna]+=array[i][j];
					
					}}}}}
			
		for (int fila=0; fila<array1.length; fila++) {
			System.out.println(Arrays.toString(array1[fila]));
		}
	}}
		
		//-------------------------------------------------------------------
