import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int T = sc.nextInt();
		for(int i=0; i<T; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			System.out.println((a==b)? "#"+(i+1)+" =" : ((a>b)? "#"+(i+1)+" >":"#"+(i+1)+" <"));	
		}	
	}
}