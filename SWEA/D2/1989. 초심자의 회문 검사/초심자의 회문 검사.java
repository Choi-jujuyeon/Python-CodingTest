import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			boolean result = true;
			String[] s = sc.next().split("");
			
			for(int i=0; i<s.length/2; i++) {
				if(s[i].equals(s[s.length-1-i])) {
					continue;
				}else {
					result=false;
					break;
				}
			}
			if(result)
				System.out.println("#"+ tc+" "+1);
			else
				System.out.println("#"+tc+" "+0);
			
		}
		
	}
}