import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		while(true) {
			String s= sc.next();
			if(s.equals("0")) break;
			
			boolean flag = true;
			for(int i=0; i<s.length()/2; i++) {
				if(s.charAt(i) != s.charAt(s.length()-i-1)) {
					System.out.println("no");
					flag = false;
					break;
					
				}
			}
			if(flag) System.out.println("yes");	
		}	
	}
}