import java.util.HashSet;
import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			int N =sc.nextInt();
			
			HashSet<Integer> set = new HashSet<>();
			for(int i=0; i<N; i++) set.add(sc.nextInt());
			System.out.println("#"+tc+" "+ (set.size() == N?"Yes":"No"));
		}
	}
}