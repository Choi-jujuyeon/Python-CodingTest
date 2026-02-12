import java.util.Scanner;

class Solution{
    static int N, L;
    static int[] t, k;
    static int max;
    
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			N=sc.nextInt();
			L = sc.nextInt();
			
			t = new int[N];
			k = new int[N];
			for(int i=0; i<N; i++) {t[i]=sc.nextInt(); k[i]=sc.nextInt();}
			
			max =Integer.MIN_VALUE;
			
			dfs(0,0,0);
			System.out.println("#"+tc+" "+max);
		}
	}
	//점수 넘지 않는 선에서 맛평가 최고
	static void dfs(int idx,int score, int cal) {
		if(cal>L) return;
		
		if(idx == N) {
			if(score>max) max=score;
			return;
		}
		dfs(idx+1, score,cal);
		dfs(idx+1, score+t[idx], cal+k[idx]);

	}
}