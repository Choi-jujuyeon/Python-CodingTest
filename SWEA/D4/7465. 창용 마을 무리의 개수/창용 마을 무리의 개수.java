import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class Solution{
	static int[] arr;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			arr = new int[N+1];
			for(int i=0; i<=N; i++) arr[i] = i;
			
			for(int i=0; i<M; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				
				union(a,b);
				
			}
			Set<Integer> set = new HashSet<>();
			for(int i=1; i<=N; i++) {
				set.add(find(i));
			}
			System.out.println("#"+tc+" "+set.size());
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