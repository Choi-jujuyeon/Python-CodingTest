import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] s =br.readLine().split(" ");
		
		int N =Integer.parseInt(s[0]);
		int sum = Integer.parseInt(s[1]);
		
		int[] arr = new int[N];
		String[] arr2 = br.readLine().split(" ");
		for(int i=0; i<N; i++) arr[i] = Integer.parseInt(arr2[i]);
		
		
		int max=0;
		for(int i=0; i<N; i++) {
			for(int j=i+1; j<N; j++) {
				for(int k=j+1; k<N; k++) {
					int total = arr[i]+arr[j]+arr[k];
					if(total<=sum && total>max) max=total;
					
				}
			}
		}
		System.out.println(max);
		
	}
}