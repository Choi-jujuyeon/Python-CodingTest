import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution{
	
	static int[] a;
	static int[] b;
	static int[] order;

	static boolean[] selected;
	static boolean[] visited;

	static int win, lose, idx;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine().trim());
		for(int tc = 1; tc <= T; tc++) {
			a = new int[9];
			b = new int[9];
			order = new int[9];
			
			selected = new boolean[19];
			visited = new boolean[9];
		
			win = 0;
			lose = 0;
			
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			for(int i = 0; i < 9; i++) {
				a[i] = Integer.parseInt(st.nextToken());
				selected[a[i]] = true;
			}
			
			idx = 0;
			for(int i = 1; i < 19; i++) {
				if(!selected[i]) {
					b[idx++] = i;
				}
			}
			
			check(0);
			
			System.out.println("#" + tc + " " + win + " " + lose);
		}
	}
	
	static void check(int num) {
		if(num == 9) {
			int gyuScore = 0;
			int inScore = 0;
			
			for(int i = 0; i < 9; i++) {
				int sum = a[i] + order[i];
				
				if(a[i] > order[i]) gyuScore += sum;
				else inScore += sum;
			}

			if(gyuScore > inScore) win++;
			else lose++;

			return;
		}
		
		for(int i = 0; i < 9; i++) {
			if(visited[i]) continue;
			
			visited[i] = true;
			order[num] = b[i];
			check(num + 1);
			visited[i] = false;
		}
	}
}