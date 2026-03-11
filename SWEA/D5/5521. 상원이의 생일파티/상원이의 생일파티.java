import java.util.ArrayList;
import java.util.Scanner;

class Solution{
	
	static boolean[] visited;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			visited = new boolean[N+1];
			
			ArrayList<Integer>[] arr = new ArrayList[N+1];
			for(int i=0; i<=N; i++) {
				arr[i] = new ArrayList<>();
			}
			
			for(int i=0; i<M; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				
				arr[a].add(b);
				arr[b].add(a);
			}
			
			for(int friend: arr[1]) {
				visited[friend] = true;
				
				for(int friendF: arr[friend]){
					if(friendF !=1)
						visited[friendF] = true;
				}
			}
			
			int cnt =0;
			for(int i=2; i<=N; i++) {
				if(visited[i]) cnt++;
			}
			System.out.println("#"+tc+" "+cnt);
		}
	}
}