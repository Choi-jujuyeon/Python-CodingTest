import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int i=0; i<T; i++) {
			String s = sc.next();
			int ans =0;
			
			int cnt=0;
			for(int j=0; j<s.length(); j++) {
				
				if(s.charAt(j) == 'O') {
					cnt++;
					ans+=cnt;
				}
				else
					cnt=0;
				
			}
			System.out.println(ans);
		}
		
	}
}