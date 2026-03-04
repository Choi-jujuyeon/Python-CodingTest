import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution{
    static int N;
    static int wx, wy, hx, hy;
    static int[] cx, cy;
    static boolean[] visited;
    static int best;
	
	//계산
	static int dist(int x1, int y1, int x2, int y2) {
		return Math.abs(x1-x2) + Math.abs(y1-y2);
	}
	//고객수, 현재위치, 누적이동거리
	static void dfs(int idx, int curX, int curY,int sum) {
		if(sum>=best) return;
		
		if(idx ==N) {
			sum+= dist(curX, curY, hx, hy);
			best = Math.min(sum, best);
			return;
		}
		for(int i=0; i<N; i++) {
			if(visited[i]) continue;
			
			visited[i] = true;
		    dfs(idx + 1, cx[i], cy[i], sum + dist(curX, curY, cx[i], cy[i]));
			visited[i] = false;
		}

	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine().trim());
		
		for(int tc =1; tc<=T; tc++) {
			N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			
			wx = Integer.parseInt(st.nextToken());
			wy = Integer.parseInt(st.nextToken());
			
			hx = Integer.parseInt(st.nextToken());
			hy = Integer.parseInt(st.nextToken());
			
			cx = new int[N];
			cy = new int[N];
			
			for(int i=0; i<N; i++) {
				cx[i] = Integer.parseInt(st.nextToken());
				cy[i] = Integer.parseInt(st.nextToken());
			}
			
			visited = new boolean[N];
			best = Integer.MAX_VALUE;
			
			dfs(0,wx,wy,0);
			
			System.out.println("#"+tc+" "+best);
			
			
			
		}
		
	}
	
	
	
}