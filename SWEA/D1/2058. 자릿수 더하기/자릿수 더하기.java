import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String num = sc.next();
		int result =0;
		for(int i=0; i<num.length(); i++) {
			result += num.charAt(i)-'0';
		}
		System.out.println(result);
	}
}