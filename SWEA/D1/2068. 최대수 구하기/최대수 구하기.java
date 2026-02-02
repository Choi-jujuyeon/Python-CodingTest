import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int T = sc.nextInt();
		for(int j=0; j<T; j++) {
			int[] arr = new int[10];
			for(int i=0; i<10; i++) 
				arr[i]= sc.nextInt();
			Arrays.sort(arr);
		System.out.println("#"+(j+1)+" "+arr[9]);
		}
	}
}
