import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class Solution{
	static int N,K;
	static char[][] map;
	
	static int[] dr = {-1,0,1,0};
	static int[] dc = {0,1,0,-1};
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			
			map = new char[N][N];
			
			int startR = -1;
			int startC = -1;
			
			//시작점 찾기
			for(int i=0; i<N; i++) {
				String s = br.readLine();
				for(int j=0; j<N; j++) {
					map[i][j] =s.charAt(j);
					
					if(map[i][j] == 'X') {
						startR = i;
						startC=j;
					}
				}
			}
			
			//최단거리찾기
			int ans = bfs(startR, startC);
			System.out.println("#"+tc+" "+ans);
		}
			
	}
	
	static int bfs(int sr, int sc) {
		Queue<int[]> q = new ArrayDeque<>();
		
		boolean[][][][] visited = new boolean[N][N][4][K+1]; 		//위치,방향,cut
		
		//시작
		q.offer(new int[] {sr,sc,0,0,0});
		visited[sr][sc][0][0] = true;
		
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			
			int r = cur[0];
			int c = cur[1];
			int dir = cur[2];
			int cut = cur[3];
			int cnt = cur[4];
			
			if(map[r][c]== 'Y') {
				return cnt;
			}
			//방향 체크 -> 위치변경x 회전만함!==dir만 변경
			//좌회전
			int leftDir = (dir + 3)%4;
			if(!visited[r][c][leftDir][cut]) {
				visited[r][c][leftDir][cut] = true;
				q.offer(new int[] {r,c,leftDir,cut,cnt+1});
			}
			//우회전
			int rightDir = (dir + 1)%4;
			if(!visited[r][c][rightDir][cut]) {
				visited[r][c][rightDir][cut] = true;
				q.offer(new int[] {r,c,rightDir,cut,cnt+1});
			}
			
			//전진
			int nr = r+ dr[dir];
			int nc = c+dc[dir];
			
			if(nr>=0 && nr<N && nc>=0 && nc<N ) {
				if(map[nr][nc]=='G' || map[nr][nc]=='Y') {
					if(!visited[nr][nc][dir][cut]) {
						visited[nr][nc][dir][cut] = true;
						q.offer(new int[]{nr,nc,dir,cut,cnt+1});
					}
				}
				else if(map[nr][nc] =='T') {
					if(cut<K && !visited[nr][nc][dir][cut+1]) {
						visited[nr][nc][dir][cut+1]= true;
						q.offer(new int[] {nr,nc,dir,cut+1, cnt+1});
					}
				}
			}
					
		}
		return -1;
	}
}