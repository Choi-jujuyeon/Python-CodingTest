import java.util.Scanner;

class Solution{
	
	static int[] arr;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb;
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			sb = new StringBuilder();
			
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			arr = new int[n+1];
			for(int i=0; i<n; i++) arr[i] = i;
			
			for(int i=0; i<m; i++) {
				int flag = sc.nextInt();
				int a = sc.nextInt();
				int b = sc.nextInt();
				
				//합
				if(flag == 0) {
					union(a,b);
				}
				else {
					if( find(a)!= find(b)) sb.append(0);
					else sb.append(1);
				}
			}
			System.out.println("#"+tc+" "+sb);
		}
	}
	static void union(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		
		if(rootA != rootB) arr[rootB] = rootA;
		
		
	}
	static int find(int x) {
		if(arr[x]!= x) arr[x] = find(arr[x]);
		return arr[x];
	}
}