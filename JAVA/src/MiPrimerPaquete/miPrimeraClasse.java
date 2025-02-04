package MiPrimerPaquete;

import java.util.Iterator;
import java.util.Scanner;

public class miPrimeraClasse {

	public static void main(String[] args) {
		
		// Escaners = Inputs pero de diversa forma buscar informacion
		/*
		int entrada;
		
		Scanner sc = new Scanner(System.in);
		
		entrada = sc.nextInt();
		System.out.print(entrada);
		*/
		// While
		/*
		Scanner sc = new Scanner(System.in);
		int entrada = 5;
		while (entrada < 10) {
			entrada = sc.nextInt();
		}
		*/
		
		/*
		int entrada;
		Scanner sc = new Scanner(System.in);
		
		
		do {
			System.out.println();
			entrada = sc.nextInt();
		}while(entrada < 10);
		System.out.println();
		
		for (int i = 0;i < 10; i++) {
			System.out.println(i);
		}
		
		*/
		
		// Arrays
		/*
		int[] array = new int[10];
		System.out.println(array.length);
		for (int i = 0;i < array.length; i++) {
			System.out.println(array[i]);
		} */
		
//		double entrada;
	//	entrada = (int) (10 * Math.random() + 50);
		//System.out.println(entrada);
		
		
		int[] array = new int[10];
		System.out.println(array.length);
		for (int i = 0;i < array.length; i++) {
			array[i] = (int) (50*Math.random() +50);
			System.out.println(array[i]);
			
			for (int j = 0; j < array.length; j++) {
				
			}
			
		}
	}
	
	

}
