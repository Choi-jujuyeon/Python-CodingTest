import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Solution {
	
	
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int T = sc.nextInt();
    	
    	for(int i=1; i<=T; i++) {
    		String s = sc.next();
    		System.out.println("#"+i+" "+check(s));
    	}
    }
    
    public static int check(String s) {
    	Deque<Character> dq = new ArrayDeque<>();
    	
    	for(int i=0; i<s.length(); i++) 
    		dq.addLast(s.charAt(i));
    	
    	while(dq.size()>1) {
    		char lp = dq.pollFirst();
    		char rp = dq.pollLast();
    		if(lp != rp ) return 0;
    	}
    	
		return 1;
    }
}