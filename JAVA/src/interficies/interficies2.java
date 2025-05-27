package interficies;

import java.util.*;

public class interficies2 {

	public static void main(String[] args) {
		String cabecera=String.format("%-15s%10s%6.2sf", "Nombres","Edad","Velocidad maxima");

		ArrayList<Atleta> atletas=new ArrayList<Atleta>();
		atletas.add(new Atleta("Pablo",25,30f));
		atletas.add(new Atleta("Mariano",5,30f));
		atletas.add(new Atleta("Jose",2,30f));
		atletas.add(new Atleta("Misae",50,30f));
		atletas.add(new Atleta("Sinosuke",5,30f));
		atletas.add(new Atleta("Himawary",25,30f));
		atletas.add(new Atleta("Bochan",25,30f));
		atletas.add(new Atleta("Masao",25,30f));
		System.out.println("*****************Participantes Atletas*****************");
		System.out.println(cabecera);

		for (Atleta atleta:atletas) {
			System.out.println(atleta.datos());
		}
		System.out.println("*****************ORDENAMOS POR Nombre*****************");
		System.out.println(cabecera);

		Collections.sort(atletas);
		for (Atleta atleta:atletas) {
			System.out.println(atleta.datos());
		}
		System.out.println("*****************ORDENAMOS POR Edad*****************");
		System.out.println(cabecera);

		Collections.sort(atletas,new OrdenarPorEdad());
		for (Atleta atleta:atletas) {
			System.out.println(atleta.datos());
		}
	}
}

class Atleta implements Comparable<Atleta>{
	private String nombre;
	private int edad;
	private float velocidad_max;
	public Atleta(String nombre, int edad, float velocidad_max) {
		super();
		this.nombre = nombre;
		this.edad = edad;
		this.velocidad_max = velocidad_max;
	}
	
	public String datos() {
		return String.format("%-15s%10d%6.2f", nombre,edad,velocidad_max);
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public float getVelocidad_max() {
		return velocidad_max;
	}

	public void setVelocidad_max(float velocidad_max) {
		this.velocidad_max = velocidad_max;
	}

	public int compareTo(Atleta arg0) {
//		return edad - arg0.getEdad();
//		return arg0.getEdad() -edad ;
		// asi es si queremos comparar strings(nombres)
		return this.nombre.compareTo(arg0.getNombre());
	}
}


class OrdenarPorEdad implements Comparator<Atleta>{
	public int compare(Atleta o1, Atleta o2) {
		return o1.getEdad()-o2.getEdad();
	}
	
}
class OrdenarPorVelocidad implements Comparator<Atleta>{
	public int compare(Atleta o1, Atleta o2) {
		return  (int) (o1.getVelocidad_max()-o2.getVelocidad_max());
	}
	
}



