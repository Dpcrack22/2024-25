package MiPrimerPaquete;

import java.util.Scanner;

public class Burbuja {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*ARRAYS*/
        Scanner sc=new Scanner(System.in);
        double Entrada ;
        int entrada2 = 0;
        Entrada=(int)(50*Math.random()+50);

        
        int[] array=new int[10];
        //String[] array= new String[10];
//        System.out.println(array.length);
//        System.out.println(entrada2);

        
        for (int i=0; i<array.length; i++) {
            array[i]=(int)(50*Math.random()+50);
            System.out.println(array[i]);
        }
        
        for (int i=0;i<array.length-1;i++) {
            for (int j=0;j<array.length-1-i;j++)
                if(array[j]<array[j+1]) {
                    int aux=array[j];
                    array[j]=array[j+1];
                    array[j+1]=aux;
                }
                
        }
        System.out.println("--------------------------------------------------------------");

        for (int i=0; i<array.length; i++) {
            System.out.println(array[i]);
        }
        
	}

}
