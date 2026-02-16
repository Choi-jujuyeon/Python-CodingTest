import java.util.ArrayList;
import java.util.Scanner;

class Solution{
	static ArrayList<Integer>[] g;
	static boolean[] visited;
	static int G;
	static int count;
	
	static void dfs(int now) {
		if(now ==G) {
			count++;
			return;			
		}
		
		for(int next: g[now]) {
			if(!visited[next]) {
				visited[next] = true;
				dfs(next);
				visited[next]=false;
			}
		}	
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int tc =1; tc<=T; tc++) {
			int N = sc.nextInt();
			int E = sc.nextInt();
			
			g= new ArrayList[N+1];
			
			for(int i=0; i<=N; i++) g[i] = new ArrayList<>();
			
			for(int i=0; i<E; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				g[a].add(b);
			}
			int S = sc.nextInt();
			G = sc.nextInt();
			
			visited = new boolean[N+1];
			visited[S] = true;
			
			count =0;
			dfs(S);
			System.out.println("#"+tc+" "+count);
		}
	}
}