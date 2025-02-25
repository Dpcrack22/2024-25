package ClasesAbstractas1;

public class MainCLass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Figura[] figuras = new Figura[10];
		figuras[0] = new Cuadrado(5,5,5);
		figuras[1] = new Circulo(6,6,6);
		for (int i = 0; i<figuras.length; i++) {
			if (figuras[i] != null) {
				System.out.println(figuras[i].);
			}
		}

		
	}

abstract class Figura {
	int posicionx;
	int posiciony;
	public Figura(int posicionx, int posiciony) {
		super();
		this.posicionx = posicionx;
		this.posiciony = posiciony;
	}
	public int getPosicionx() {
		return posicionx;
	}
	public void setPosicionx(int posicionx) {
		this.posicionx = posicionx;
	}
	public int getPosiciony() {
		return posiciony;
	}
	public void setPosiciony(int posiciony) {
		this.posiciony = posiciony;
	}
	public float area() {
		return 0;
	}
	public float perimetro() {
		return 0;
	}
	
	@Override
	public String toString() {
		return "Figura [posicionx=" + posicionx + ", posiciony=" + posiciony + "]";
	}
	

}

class Cuadrado extends Figura{
	int lado;
	
	
	public Cuadrado(int posicionx, int posiciony, int lado) {
		super(posicionx, posiciony);
		this.lado = lado;
	}
	public int areaDelCuadrado() {
		return lado*lado;
		
	}
	public int perimetroDelCuadrado() {
		return 4*lado;
	}
	
}
class Circulo extends Figura{
	float radio;
	
	public Circulo(int posicionx, int posiciony, float radio) {
		super(posicionx, posiciony);
		this.radio = radio;
	}
	public float areaC() {
		return (float) (Math.PI*radio*radio);
	}
	public float perimetroC() {
		return (float) (2*Math.PI*radio);
	}
}
final class Triangulo extends Figura{
	float base;
	float altura;
	public Triangulo(int posicionx, int posiciony, float base, float altura) {
		super(posicionx, posiciony);
		this.base = base;
		this.altura = altura;
	}
	
}
}
