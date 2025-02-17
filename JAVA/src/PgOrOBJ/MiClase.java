package PgOrOBJ;

import java.util.Arrays;

public class MiClase {
	private int a;
	private String b;
	private int[] array;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	public void salidar() {
		System.out.println("Holas");
	}
	
	public int devuelve_a() {
		return a;
	}
	public int getA() {
		return a;
	}
	public void setA(int a) {
		this.a = a;
	}
	public String getB() {
		return b;
	}
	public void setB(String b) {
		this.b = b;
	}
	public int[] getArray() {
		return array;
	}
	public void setArray(int[] array) {
		this.array = array;
	}
	
	public MiClase(int a, String b, int[] array) {
		super();
		this.a = a;
		this.b = b;
		this.array = array;
	}
	
	
	public String toString() {
		return "MiClase [a=" + a + ", b=" + b + ", array=" + Arrays.toString(array) + "]";
	}
	
	
}
