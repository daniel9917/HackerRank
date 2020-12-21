package sockmerchant;

import java.util.ArrayList;

public class Main {
	public static void main (String [] args) {
		int [] test = new int[]{10,20,20,10,10,30,50,10,20,10,40,50,30,30,10,20,30,10,40,40};
		
		ArrayList<Integer> tipos = hallar_tipos(test);
		ArrayList<Integer> medias = clasificacion(tipos, test);		
		int pares = 0;
		for (int media : medias) {
			if ( media % 2 == 0) {
				pares = pares + (media/2);
			}
			else if (media != 1) {
				pares = pares + ((media - 1)/2);
				
			} 
		}
		System.out.println("El total de pares es: "+pares);
	}
	
	public static ArrayList<Integer> clasificacion (ArrayList<Integer> tipos, int [] medias){
		ArrayList<Integer> cantidad = new ArrayList<Integer>();
		
		for (int tipo: tipos) {
			cantidad.add(0);			
		}
		
		for (int i = 0; i < tipos.size(); i++) {
			for (int j = 0; j < medias.length; j ++) {
				if(tipos.get(i) == medias [j]) {
					cantidad.set(i, cantidad.get(i) + 1); 
				}				
			}
		}
		
		return cantidad;
		
	}
	
	public static ArrayList<Integer> hallar_tipos (int[] valores ) {		
		ArrayList<Integer> tipos = new ArrayList<Integer>();
		
		tipos.add(valores[0]);
		for (int i = 0; i < valores.length; i++) {
			if (!existeTipo(valores[i], tipos)) {
				tipos.add(valores[i]);
			}
		}
		
		return tipos;
	}
	
	public static boolean existeTipo(int valor, ArrayList<Integer> tipos) {
		for (int i = 0; i < tipos.size(); i++) {
			if(tipos.get(i) == valor){
				return true;
			}
		}			
		return false;
	}
	

}
