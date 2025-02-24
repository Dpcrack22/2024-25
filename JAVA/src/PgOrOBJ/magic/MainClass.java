package PgOrOBJ.magic;

import java.lang.Math;
import java.util.Arrays;

public class MainClass {

	public static void main(String[] args) {
		Carta[] cartas = new Carta[20];
		
		cartas[0] = new Carta("Puerta de Baldur", 0, 7, 4, 1);
		cartas[1] = new Carta("Gobblin", 5, 5, 4, 3);
		cartas[2] = new Carta("Guerrero", 6, 4, 5, 4);
		cartas[3] = new Carta("Zorro de 9 colas", 4, 5, 4, 1);
		cartas[4] = new Carta("Cifosoa", 5, 3, 6, 1);
		cartas[5] = new Carta("Piedrin", 1, 8, 1, 1);
		cartas[6] = new Carta("Slime", 2, 3, 2, 2);
		cartas[7] = new Carta("Guiverno", 7, 4, 6, 9);
		cartas[8] = new Carta("Ferrosaurio", 8, 6, 5, 7);
		cartas[9] = new Carta("Balatro Balátrez", 6, 2, 3, 5);
		cartas[10] = new Carta("Slime de Oro", 2, 1, 9, 10);
		cartas[11] = new Carta("Gólem de piedra", 7, 8, 10, 1);
		cartas[12] = new Carta("LoboLava", 2, 4, 5, 6);
		cartas[13] = new Carta("Lightning ", 5, 6, 4, 5);
		cartas[14] = new Carta("Minotauro", 3, 2, 2, 6);
		cartas[15] = new Carta("Hacienda",9 , 10, 5, 7);
		cartas[16] = new Carta("Gustavo Fring", 3, 7, 1, 6);
		cartas[17] = new Carta("Rusello", 6, 6, 2, 4);
		cartas[18] = new Carta("Hombre Menguante", 8, 8, 9, 4);
		cartas[19] = new Carta("Business Mundo", 5, 5, 5, 2);
		
		
//		for (int i=0; i<cartas.length; i++) {
//			if (cartas[i] != null) { 
//				System.out.println("**************************************");
//				System.out.println(cartas[i]);
//			}
//		}
		
		JugadorCartas[] jugadores_cartas = new JugadorCartas[11];
		jugadores_cartas[0] = new JugadorCartas("12345678L", "Gervasio", "de León Mora", 22, 20, 20);
		jugadores_cartas[1] = new JugadorCartas("46464646A", "Pepe", "García García", 22, 20, 20);
		jugadores_cartas[2] = new JugadorCartas("11111111H","Margarita","Flores Giménez",22,20,20);
		jugadores_cartas[3] = new JugadorCartas("88888888Y", "Eustaquio", "Avichuela", 22, 20, 20);
		jugadores_cartas[4] = new JugadorCartas("45678934Z", "Cristian" , "Navarro Gonzalez", 22, 20, 20);
		jugadores_cartas[5] = new JugadorCartas("46845365N","Dolores","Suárez Castillo", 22, 20, 20);
		jugadores_cartas[6] = new JugadorCartas("12312312A", "Pedro", "Sanchez", 22, 20, 20);
		jugadores_cartas[7] = new JugadorCartas("11223344M", "Ezequiel", "De todos los santos", 22, 20, 20);
		jugadores_cartas[8] = new JugadorCartas("76547821D", "Marcos", "Fernández Martín", 22, 20, 20);
		jugadores_cartas[9] = new JugadorCartas("84267193J","Inmaculada","Ponce",22,20,20);
		jugadores_cartas[10] = new JugadorCartas("11112222A","Pablo","Suarez",22,20,20);
		
		
		
		
		
		
		
		
		
		


		
		
		ContenedorCartas contenedorCartas = new ContenedorCartas();
		contenedorCartas.addCarta(new Carta("Lightning ", 5, 6, 4, 5));
		contenedorCartas.mostrarCartas();
		contenedorCartas.resetCartas();
		System.out.println("-----------------------------------");
		contenedorCartas.mostrarCartas();
	}
}

class PartidaCartas {
	private ContenedorCartas contenedor_cartas_partida;
	private ContenedorJugadoresCartas contenedor_jugadores_partida;
	JugadorCartas[] jugadores_turno;
	public PartidaCartas(ContenedorCartas contenedor_cartas_partida,
			ContenedorJugadoresCartas contenedor_jugadores_partida, JugadorCartas[] jugadores_turno) {
		super();
		this.contenedor_cartas_partida = contenedor_cartas_partida;
		this.contenedor_jugadores_partida = contenedor_jugadores_partida;
		this.jugadores_turno = jugadores_turno;
	}
	public void repartir_cartas() {
		JugadoresCartas[] jugadores_contenedor = contenedor_jugadores_partida.getJugadoresContenedor();
		for (int i == 0; i<contenedor_jugadores_partida.getNUMERO_JUGADORES();i++) {
			
		}
	}
}


class jugador {
	String dni;
	String nombre;
	String apelidos;
	
	public jugador(String dni, String nombre, String apelidos) {
		super();
		this.dni = dni;
		this.nombre = nombre;
		this.apelidos = apelidos;
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

	public String getApelidos() {
		return apelidos;
	}

	public void setApelidos(String apelidos) {
		this.apelidos = apelidos;
	}

	@Override
	public String toString() {
		return "jugador [dni=" + dni + ", nombre=" + nombre + ", apelidos=" + apelidos + "]";
	}
	
	
}

class JugadorCartas extends jugador{
	private int numero_cartas;
	private Carta[] cartas_jugador;
	private int mana;
	private int vida;
	private int vida_inicial;
	private int mana_inicial;
	public JugadorCartas(String dni, String nombre, String apelidos, int numero_cartas, Carta[] cartas_jugador,
			int mana, int vida) {
		super(dni, nombre, apelidos);
		this.numero_cartas = numero_cartas;
		this.cartas_jugador = cartas_jugador;
		this.mana = mana;
		this.vida = vida;
		vida_inicial = vida;
		mana_inicial = mana;
		cartas_jugador = new Carta[numero_cartas];
	}
	public JugadorCartas(String string, String string2, String string3, int i, int j, int k) {
		// TODO Auto-generated constructor stub
	}
	public void reset_mana() {
		mana = mana_inicial;
	}
	
	public void reset_vida() {
		vida = vida_inicial;
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
	public void reset_cartas_jugador() {
		cartas_jugador = new Carta[numero_cartas];
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
	
	public Carta getCartaAleatoria() {
		int numero_aleatorio = (int) (numero_cartas*Math.random());
		return cartas_jugador[numero_aleatorio];
	}
	
	@Override
	public String toString() {
		return "JugadorCartas [numero_cartas=" + numero_cartas + ", cartas_jugador=" + Arrays.toString(cartas_jugador)
				+ ", mana=" + mana + ", vida=" + vida + "]";
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
	
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
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

	public String toString() {
		return "Carta [Nombre=" + nombre + ", ataque=" + ataque + ", defensa=" + defensa + ", costeMana=" + costeMana
				+ ", agilidad=" + agilidad + "]";
	}
}
class ContenedorCartas{
	private final int NUMEROCARTAS = 22;
	private Carta[] cartas = new Carta[NUMEROCARTAS];
	private int[] cartasEscogidas = new int[NUMEROCARTAS];
	public void addCarta(Carta carta) {
		for (int i=0; i<cartas.length;i++) {
			if (cartas[i] == null) {
				cartas[i] = carta;
				System.out.println("Imprime carta insertada en la posicion "+i);
				return;
			}
		}
		System.out.println("No hay espacios para mas cartas");
	}
	public int getNUMEROCARTAS() {
		return NUMEROCARTAS;
	}
	public void resetCartas() {
		cartas = new Carta[20];
		cartasEscogidas = new int[cartas.length];
	}
	public void resetCartasEscogidas() {
		cartasEscogidas = new int[cartas.length];
	}
	public void mostrarCartas( ) {
		for (int i=0; i<cartas.length;i++) {
			if (cartas[i] != null) {
				System.out.println(cartas[i]);
			}
		}
	}
	public Carta getCartaAleatoria() {
		 int numRandom;
		 int numCartasEscogidas = 0;
		 
		 if (!contenedor_lleno() ) {
			 System.out.println("Todavia faltan cartas por insertar");
			 return null;
		 }
		 for (int i=0; i<NUMEROCARTAS;i++) {
			 numCartasEscogidas += cartasEscogidas[i];
		 }
		 if (numCartasEscogidas == NUMEROCARTAS) {
			 System.out.println("Ya no se pueden escojer mas cartas");
			 return null;
		 }
		 
		// numRandom = (int)(NUMEROCARTAS*Math.random());
		// while (cartasEscogidas[numRandom] == 1) {
		// 	numRandom = (int)(NUMEROCARTAS*Math.random());
			
		do {
			numRandom = (int)(NUMEROCARTAS*Math.random());
		}while (cartasEscogidas[numRandom] == 1);
		// }
			
		cartasEscogidas[numRandom] = 1;
		return cartas[numRandom];
		
	
	}
	
	public boolean contenedor_lleno() {
		for (int i=0;i<NUMEROCARTAS; i++) {
			if (cartas[i]==null){
				return false;
			}
		}
		return false;
	}
		
	
}



class ContenedorJugadoresCartas{
	private final int NUMERO_CARTAS = 3;
	private final int NUMERO_JUGADORES = 5;
	private JugadorCartas[] jugadores_contenedor = new JugadorCartas[NUMERO_JUGADORES];
	
	
	public void addJugador(JugadorCartas jugador) {
		for (int i = 0; i<NUMERO_JUGADORES; i++) {
			if (jugadores_contenedor[i] == null ) {
				jugadores_contenedor[i] = jugador;
				System.out.println("Jugador añadido correctamente");
				return ;
			}
		}
		System.out.println("No se ha podido añadir el jugador");
	}
	
	public JugadorCartas[] getJugadoresAleatorios() {
		JugadorCartas[] jugadores_aleatorios = new JugadorCartas[2];
		int numero_aleatorio;
		
		
		do {
			numero_aleatorio = (int) (NUMERO_JUGADORES*Math.random());

		}while (jugadores_contenedor[numero_aleatorio].getVida() == 0);
		
		if (contenedor_lleno() ) {
			System.out.println("LLENO");
		}
			return null
		}
		do {
			numero_aleatorio = (int) (NUMERO_JUGADORES*Math.random());

		}while(jugadores_aleatorios[0] == jugadores_contenedor[numero_aleatorio]);
		jugadores_aleatorios[0] = jugadores_contenedor[numero_aleatorio];

		return jugadores_aleatorios;
	}
	
	
	public boolean ganador() {
		int numero_jugadores_vida = 0;
		for(int i = 0; i<NUMERO_JUGADORES; i++) {
			if (jugadores_contenedor[i].getVida() > 0) {
				numero_jugadores_vida ++;
				
			}
		}
		if (numero_jugadores_vida > 1) {
			return false;
		}
		return false;
	}
	public boolean contenedor_lleno() {
		for(int i = 0; i<NUMERO_JUGADORES; i++) {
			if (jugadores_contenedor[i] == null) {

	}
	
	public JugadorCartas[] getJugadores_contenedor() {
		return jugadores_contenedor;
	}
}
