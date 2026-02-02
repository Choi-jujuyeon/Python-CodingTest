import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int T = sc.nextInt();
		
		int arr[] = new int[10];
		
		for(int k=0; k<T; k++) {
			int result =0;
			for(int i=0; i<10; i++)
				arr[i] = sc.nextInt();
			
			Arrays.sort(arr);
			for(int i=1; i<9; i++)
				result+=arr[i]; 
		
			System.out.printf("#%d %d\n",k+1, Math.round(result/8.0));
		}
	}
}
