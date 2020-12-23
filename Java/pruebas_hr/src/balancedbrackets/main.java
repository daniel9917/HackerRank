package balancedbrackets;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class main {
	
	
	
	public static void main (String args []) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		
		
		String s = "";
		boolean stop = false;
		while (!stop){		
		s= input.readLine();
		if (s.equals("123")) {
			stop = true;
			break;
		}
		System.out.println(isBalanced(s));
		
		}

		
	}
    public static String isBalanced(String s) throws IOException {
		int i = 0;		
		String cadena = s;
		Stack<String> OpenBrackets = new Stack<String>();
		
		String [] balanced = cadena.split("");
		
		if (balanced[0].equals("}") || balanced[0].equals(")") || balanced[0].equals("]")) {
			return "NO";
			
		}
		
		//procesar espacios
		for  (i =0; i < balanced.length; i++) {
			//System.out.print(balanced[i]);
			
			if (balanced[i].equals("{") || balanced[i].equals("(") || balanced[i].equals("[")) {
				OpenBrackets.add(balanced[i]);
				//System.out.println("Adding Openning Bracket:"+ balanced[i]);
			}
			else if (balanced[i].equals("}") || balanced[i].equals(")") || balanced[i].equals("]")) {
				if (OpenBrackets.isEmpty()) {
					return "NO";
				}
				if(filter(OpenBrackets.peek().toString(), balanced[i])) {					
					//System.out.println("Closing pair:"+OpenBrackets.pop()+" and "+balanced[i]);
					OpenBrackets.pop();
				}
				else {
					//System.out.println("Unbalanced:"+balanced[i]);
					return "NO";
				}	
			}
		//System.out.println();
		}									

		if (OpenBrackets.isEmpty()) {
			return "YES";
		}else {
			return "NO";
		}

    }
	
	public static String balance () throws IOException{
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));	
		int i = 0;
		System.out.println("Ingresar cadena de brackets: ");
		String cadena = input.readLine();
		
		
		
		Stack<String> OpenBrackets = new Stack<String>();
		
		String [] balanced = cadena.split("");
		
		//procesar espacios
		for  (i =0; i < balanced.length; i++) {
			//System.out.print(balanced[i]);
			if (balanced[i].equals("{") || balanced[i].equals("(") || balanced[i].equals("[")) {
				OpenBrackets.add(balanced[i]);
				System.out.println("Adding Openning Bracket:"+ balanced[i]);
			}
			else if (balanced[i].equals("}") || balanced[i].equals(")") || balanced[i].equals("]")) {
				if(filter(OpenBrackets.peek().toString(), balanced[i])) {					
					System.out.println("Closing pair:"+OpenBrackets.pop()+" and "+balanced[i]);
				}
				else {
					System.out.println("Unbalanced:"+balanced[i]);
					return "NO";
				}
	
			}
		System.out.println();
		}		
				
		
		

		if (OpenBrackets.size() == 0) {
			return "YES";
		}else {
			return "NO";
		}
	}
	
	public static boolean filter (String left, String right) {
		if (left.equals("{") && right.equals("}")) {
			return true;
		}
		else if (left.equals("(") && (right.equals(")"))) {
			return true;
			
		}else if (left.equals("[") && (right.equals("]"))) {
			return true;
		}
		return false;
	}

}
