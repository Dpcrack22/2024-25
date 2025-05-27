package PgOrOBJ.magic;

import java.lang.Math;
import java.util.*;
import java.util.Arrays;

public class MainClass2 {

public static void main(String[] args) {
		
		Carta[] cartas = new Carta[22];
		cartas[0] = new Carta("Cifosoa", 5, 3, 6, 1);
		cartas[1] = new Carta("Zorro de 9 colas", 4, 5, 4, 1);
		cartas[2] = new Carta("Gobblin", 5, 5, 4, 3);
		cartas[3] = new Carta("Guerrero", 6, 4, 5, 4);
		cartas[4] = new Carta("Piedrin", 1, 8, 1, 1);
		cartas[5] = new Carta("Slime", 2, 3, 2, 2);
		cartas[6] = new Carta("Puerta de Baldur", 0,7,4,1);
		cartas[7] = new Carta("Guiverno", 7, 4, 6, 9);
		cartas[8] = new Carta("Ferrosaurio", 8, 6, 5, 7);
		cartas[9] = new Carta("Balatro Balátrez",6,2,3,5);
		cartas[10] = new Carta("Slime de Oro", 2, 1, 9, 10);
		cartas[11] = new Carta("Gólem de piedra", 7, 8, 10, 1);
		cartas[12] = new Carta("LoboLava",2,4,5,6);
		cartas[13] = new Carta("Lightning ", 5, 6,4,5);
		cartas[14] = new Carta("Minotauro", 3, 2, 2, 6);
		cartas[15] = new Carta("Hacienda",9 , 10, 5, 7);
		cartas[16] = new Carta("Gustavo Fring", 3, 7, 1, 6);
		cartas[17] = new Carta("Rusello", 6, 6,2,4);
		cartas[18] = new Carta("Hombre Menguante",8,8,9,4);
		cartas[19] = new Carta("Business Mundo",5,5,5,2);
		cartas[20] = new Carta("Centinela", 2, 8, 5, 3);
		cartas[21] = new Carta("segarro", 9, 5, 4, 3);
		
		
		JugadorCartas[] jugadores_cartas = new JugadorCartas[11];
		jugadores_cartas[0] = new JugadorCartas("11111111H","Margarita","Flores Giménez",22,20,20);
		jugadores_cartas[1] = new JugadorCartas("12345678L", "Gervasio", "de León Mora", 22, 20, 20);
		jugadores_cartas[2] = new JugadorCartas("46464646A", "Pepe", "García García", 22, 20, 20);
		jugadores_cartas[3] = new JugadorCartas("88888888Y", "Eustaquio", "Avichuela", 22, 20, 20);
		jugadores_cartas[4] = new JugadorCartas("45678934Z", "Cristian" , "Navarro Gonzalez", 22, 20, 20); 
		jugadores_cartas[5] = new JugadorCartas("46845365N","Dolores","Suárez Castillo", 22, 20, 20);
		jugadores_cartas[6] = new JugadorCartas("12312312A", "Pedro", "Sanchez", 22, 20, 20);
		jugadores_cartas[7] = new JugadorCartas("11223344M", "Ezequiel", "De todos los santos", 22, 20, 20);
		jugadores_cartas[8] = new JugadorCartas("76547821D", "Marcos", "Fernández Martín", 22, 20, 20);
		jugadores_cartas[9] = new JugadorCartas("84267193J","Inmaculada","Ponce",22,20,20);
		jugadores_cartas[10] = new JugadorCartas("11112222A","Pablo","Suarez",22,20,20);
		
	}

}

class PartidaCartas{
	private ContenedorCartas contenedor_cartas_partida;
	private ContenedorJugadoresCartas contenedor_jugadores_partida;
	private JugadorCartas[] jugadores_turno;
	
	public PartidaCartas(ContenedorCartas contenedor_cartas_partida,
			ContenedorJugadoresCartas contenedor_jugadores_partida) {
		super();
		this.contenedor_cartas_partida = contenedor_cartas_partida;
		this.contenedor_jugadores_partida = contenedor_jugadores_partida;
	}
	
	public void repartir_cartas() {
		JugadorCartas[] jugadores_contenedor = contenedor_jugadores_partida.getJugadores_contenedor();
		// reparto de cartas
		for (int i = 0; i<contenedor_jugadores_partida.getNUMERO_JUGADORES();i++) {
			for (int j=0; j< contenedor_jugadores_partida.getNUMERO_CARTAS();j++) {
				jugadores_contenedor[i].getCartas_jugador()[j] = contenedor_cartas_partida.getCartaAleatoria();
				
				
			}
		}
		// Fin reparto cartas
		JugadorCartas[] jugadores_turno = new JugadorCartas[2];
		int numero_aleatorio = (int) (5*Math.random());
		
	}
}

class Jugador{
	private String dni;
	private String nombre;
	private String apellidos;
	
	public Jugador(String dni, String nombre, String apellidos) {
		super();
		this.dni = dni;
		this.nombre = nombre;
		this.apellidos = apellidos;
	}

	public String toString() {
		return "Jugador [dni=" + dni + ", nombre=" + nombre + ", apellidos=" + apellidos + "]";
	}

	public String getDni() {
		return dni;
	}

	public void setDni(String dni) {
		this.dni = dni;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getApellidos() {
		return apellidos;
	}

	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}
	
}

class JugadorCartas extends Jugador{
	private int numero_cartas;
	private Carta[] cartas_jugador;
	private int mana;
	private int vida;
	private int vida_inicial;
	private int mana_inicial;
	
	public JugadorCartas(String dni, String nombre, String apellidos, int numero_cartas, int mana, int vida) {
		super(dni, nombre, apellidos);
		this.numero_cartas = numero_cartas;
		this.mana = mana;
		this.vida = vida;
		vida_inicial = vida;
		mana_inicial = mana;
		cartas_jugador = new Carta[numero_cartas];
	}
	
	public void resetMana() {
		mana = mana_inicial;
	}
	
	public void resetVida() {
		vida = vida_inicial;
	}
	
	public void resetCartasJugador() {
		cartas_jugador = new Carta[numero_cartas];
	}

	public String toString() {
		return super.toString() + "\n" + "JugadorCartas [cartas_jugador=" + Arrays.toString(cartas_jugador)
				+ ", mana=" + mana + ", vida=" + vida + "]";
	}
	
	public Carta getCartaAleatoria() {
		int numero_aleatorio = (int)(numero_cartas*Math.random());
		return cartas_jugador[numero_aleatorio];
	}


	public int getNumero_cartas() {
		return numero_cartas;
	}

	public void setNumero_cartas(int numero_cartas) {
		this.numero_cartas = numero_cartas;
	}

	public Carta[] getCartas_jugador() {
		return cartas_jugador;
	}

	public void setCartas_jugador(Carta[] cartas_jugador) {
		this.cartas_jugador = cartas_jugador;
	}

	public int getMana() {
		return mana;
	}

	public void setMana(int mana) {
		this.mana = mana;
	}

	public int getVida() {
		return vida;
	}

	public void setVida(int vida) {
		this.vida = vida;
	}
	
	
}

class Carta{
	private String nombre;
	private int ataque;
	private int defensa;
	private int costeMana;
	private int agilidad;
	
	
	public Carta(String nombre, int ataque, int defensa, int costeMana, int agilidad) {
		super();
		this.nombre = nombre;
		this.ataque = ataque;
		this.defensa = defensa;
		this.costeMana = costeMana;
		this.agilidad = agilidad;
	}


	public String toString() {
		return "Carta [nombre=" + nombre + ", ataque=" + ataque + ", defensa=" + defensa + ", costeMana=" + costeMana + ", agilidad="
				+ agilidad + "]";
	}


	public int getAtaque() {
		return ataque;
	}


	public void setAtaque(int ataque) {
		this.ataque = ataque;
	}


	public int getDefensa() {
		return defensa;
	}


	public void setDefensa(int defensa) {
		this.defensa = defensa;
	}


	public int getCosteMana() {
		return costeMana;
	}


	public void setCosteMana(int costeMana) {
		this.costeMana = costeMana;
	}


	public int getAgilidad() {
		return agilidad;
	}


	public void setAgilidad(int agilidad) {
		this.agilidad = agilidad;
	}


	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

}

class ContenedorCartas{
	private final int NUMERO_CARTAS = 22;
	private Carta[] cartas = new Carta[NUMERO_CARTAS];
	private int[] cartasEscogidas = new int[NUMERO_CARTAS];
	
	
	public void addCarta(Carta carta) {
		for (int i= 0; i<cartas.length;i++) {
			if (cartas[i] == null) {
				cartas[i] = carta;
				System.out.println("Carta insertada en la posición "+i);
				return;
			}
		}
		System.out.println("No hay espacio para más cartas");
	}
	public void resetCartas() {
		cartas = new Carta[NUMERO_CARTAS];
		cartasEscogidas = new int[cartas.length];
	}
	
	public void resetCartasEscogidas() {
		cartasEscogidas = new int[cartas.length];
	}
	
	public void mostrarCartas() {
		for (int i=0; i<cartas.length;i++) {
			System.out.println("**********************");
			System.out.println(cartas[i]);
		}
	}
	
	public Carta getCartaAleatoria() {
		int numRandom;
		int num_cartas_escogidas = 0;
		
		if (!contenedor_lleno()) {
			System.out.println("Todavía faltan cartas por insertar.");
			return null;
		}
		
		for (int i=0; i< NUMERO_CARTAS;i++) {
			num_cartas_escogidas += cartasEscogidas[i];
		}
		if (num_cartas_escogidas == NUMERO_CARTAS) {
			System.out.println("Ya no puedes escoger más cartas");
			return null;
		}
		
		do {
			numRandom = (int)(NUMERO_CARTAS*Math.random());
		}
		while (cartasEscogidas[numRandom]==1);
		
		/*numRandom = (int)(NUMERO_CARTAS*Math.random());
		 * while (cartasEscogidas[numRandom]==1) {
			numRandom = (int)(NUMERO_CARTAS*Math.random());
		}*/
		
		cartasEscogidas[numRandom] = 1;
		return cartas[numRandom];
	}
	
	public boolean contenedor_lleno() {
		for (int i=0;i<NUMERO_CARTAS;i++) {
			if (cartas[i] == null) {
				return false;
			}
		}
		return true;
	}
	
	public int getNUMERO_CARTAS() {
		return NUMERO_CARTAS;
	}
	

	
}

class ContenedorJugadoresCartas{
	private final int NUMERO_CARTAS = 3;
	private final int NUMERO_JUGADORES = 5;
	private JugadorCartas[] jugadores_contenedor = new JugadorCartas[NUMERO_JUGADORES];
	
	public void addJugador(JugadorCartas jugador) {
		for (int i=0; i<NUMERO_JUGADORES;i++) {
			if (jugadores_contenedor[i] == null) {
				jugadores_contenedor[i] = jugador;
				System.out.println("Jugador añadido correctamente.");
				return;
			}
		}
		System.out.println("No se ha podido añadir al jugador.");
	}
	
	public boolean contenedorLleno() {
		for (int i=0; i<NUMERO_JUGADORES;i++) {
			if (jugadores_contenedor[i] == null) {
				return false;
			}
		}
		return true;
	}
	
	public JugadorCartas[] getJugadoresAleatorios() {
		JugadorCartas[] jugadores_aleatorios = new JugadorCartas[2];
		int numero_aleatorio;
		
		if (!contenedorLleno()) {
			System.out.println("Primero llena el contenedor.");
			return null;
		}
		
		do {
			numero_aleatorio = (int)(NUMERO_JUGADORES*Math.random());
		} while (jugadores_contenedor[numero_aleatorio].getVida()==0);
		jugadores_aleatorios[0] = jugadores_contenedor[numero_aleatorio];
		
		do {
			numero_aleatorio = (int)(NUMERO_JUGADORES*Math.random());
		} while (jugadores_aleatorios[0] == jugadores_contenedor[numero_aleatorio] || jugadores_contenedor[numero_aleatorio].getVida()== 0);
		jugadores_aleatorios[1] = jugadores_contenedor[numero_aleatorio];
		
		return jugadores_aleatorios;
	}
	
	public boolean ganador() {
		int numero_jugadores_vida = 0;
		for (int i=0; i<NUMERO_JUGADORES;i++) {
			if (jugadores_contenedor[i].getVida() > 0) {
				numero_jugadores_vida++;
			}
		}
		if (numero_jugadores_vida > 1) {
			return false;
		}
		return true;
	}

	public JugadorCartas[] getJugadores_contenedor() {
		return jugadores_contenedor;
	}

	public int getNUMERO_CARTAS() {
		return NUMERO_CARTAS;
	}

	public int getNUMERO_JUGADORES() {
		return NUMERO_JUGADORES;
	}
	
	
	
}



