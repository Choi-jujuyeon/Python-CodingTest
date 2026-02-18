import java.util.Arrays;
import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		sc.nextLine();
		for(int tc=1; tc<=T; tc++) {
			
			String[] s= sc.nextLine().split("");
			
			String check="0";
			int cnt=0;
			for(int i=0; i<s.length; i++) {
				if(s[i].equals(check)) continue;
				else {
					check=s[i];
					cnt++;
				}
			}
			System.out.println("#"+tc+" "+cnt);
		}
	}
}