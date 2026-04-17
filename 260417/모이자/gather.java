import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int[] arr = new int[T];
		
		for(int i=0; i<T; i++) arr[i] = sc.nextInt();
		
		
		int minV =Integer.MAX_VALUE;
		for(int i=1; i<=T; i++) {
			int diffSum =0;
			
			for(int j=1; j<=T; j++) {
				if(i==j) continue;
				
				diffSum +=(Math.abs(i-j) * arr[j-1]);
			}
			minV = Math.min(minV, diffSum);
		}
		
		System.out.println(minV);
	}
}