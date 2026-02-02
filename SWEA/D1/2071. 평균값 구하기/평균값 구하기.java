import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int i=0; i<T; i++) {
			int result =0;
			for(int j =0; j<10; j++)
				result += sc.nextInt();
			System.out.printf("#%d %d\n", i+1, Math.round(result / 10.0));	
		}	
	}
}
