package twodimension_arrayds;

import java.util.ArrayList;

public class main {
	public static void main(String args[]) {
		
		int [][] test = {
				{-1, -1, 0 -9, -2, -2},
				{-2, -1, -6, -8, -2, -5},
				{-1, -1, -1, -2, -3, -4},
				{-1, -9, -2, -4, -4, -5},
				{-7, -3, -3, -2, -9, -9},				
				{-1, -1, -1, -4, -4, -1}				
		};
		
		System.out.println("La mayor suma es: "+hourglassSum(test));
		
	}
	
    static int hourglassSum(int[][] arr) {
    	ArrayList <Integer> sumas= new ArrayList<Integer>();
    	
		for (int i = 0; i < 4 ; i ++) {
			for (int j = 0; j < 4; j++) {
				int suma = 	arr [i][j]+ 
							arr [i][j + 1]+ 
							arr [i][j + 2]+ 
							arr [i + 1][j + 1]+
							arr [i + 2][j]+
							arr [i + 2][j + 1]+
							arr [i + 2][j + 2];
				
				sumas.add(suma);
			}
		}
		
		int mayor = sumas.get(0);
		for (int i = 0; i < sumas.size(); i++) {
			
			if (sumas.get(i) > mayor) {
				mayor = sumas.get(i);
			}							
		}
    	return mayor;
    }
    

    
    
}
