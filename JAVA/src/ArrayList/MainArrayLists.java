package ArrayList;

import java.util.*;

public class MainArrayLists {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<ClaseA> numeros = new ArrayList<ClaseA>(); // Esto es una arraylist de enteros el cual se especifica con el integer que es lo mismo que int
		//for (int i = 0; i < 10; i++) {
		//	numeros.add((int) (Math.random()*100));
		//}
		
		//numeros.set(5, 1000);
		//for (int i = 0; i > numeros.size(); i++) {
		//	System.out.println(numeros.get(i));
		//}
		
		//numeros.remove(5);
		//for (int i = 0; i > 10; i++) {
		//	System.out.println(numeros.get(i));
		//}
		
		for (int i = 0; i<10; i++) {
			numeros.add(new ClaseA(i));
		}
		
		ClaseA classes = new ClaseA(1000);
		numeros.add(5, classes);
		
		for (int i = 0; i<10; i++) {
			System.out.println(numeros.get(i));
		}		
		System.out.println("*****************");
		numeros.remove(classes);

		//numeros.remove(new ClaseA(1000));
		
		for (int i = 0; i<10; i++) {
			System.out.println(numeros.get(i));
		}
		
		for (ClaseA nombre_temporal_que_le_doy_a_cada_objeto : numeros) {
			System.out.println(nombre_temporal_que_le_doy_a_cada_objeto.getIdObjetos());
		}
		
		for (int pasadas = 0; pasadas<numeros.size()-1; pasadas++) {
			for (int i = 0; i < numeros.size()-1-pasadas; i++) {
				if (numeros.get(i).getIdObjetos() < numeros.get(i+1).getIdObjetos()) {
					ClaseA aux = numeros.get(i);
					numeros.set(i, numeros.get(i));
					numeros.set(i+1,aux);

				}
			}
		}
		for (ClaseA nombre_temporal_que_le_doy_a_cada_objeto : numeros) {
			System.out.println(nombre_temporal_que_le_doy_a_cada_objeto.getIdObjetos());
		}
		
	} 
	
}
 class ClaseA {
	 int idObjetos;

	public ClaseA(int idObjetos) {
		super();
		this.idObjetos = idObjetos;
	}

	public int getIdObjetos() {
		return idObjetos;
	}

	public void setIdObjetos(int idObjetos) {
		this.idObjetos = idObjetos;
	}

	@Override
	public String toString() {
		return "ClaseA [idObjetos=" + idObjetos + "]";
	}
	 
 }