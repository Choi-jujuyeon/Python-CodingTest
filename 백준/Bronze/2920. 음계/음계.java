import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String ascending ="12345678";
		String descending="87654321";

		String input = sc.nextLine().replace(" ", "");
		System.out.println(input.equals(ascending)?"ascending":(input.equals(descending)?"descending":"mixed"));
	}
}