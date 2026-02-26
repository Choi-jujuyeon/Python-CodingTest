import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine().trim();

		if (s.isEmpty()) {
		    System.out.println(0);
		} else {
		    String[] sArray = s.split(" ");
		    System.out.println(sArray.length);
		}
	}
}