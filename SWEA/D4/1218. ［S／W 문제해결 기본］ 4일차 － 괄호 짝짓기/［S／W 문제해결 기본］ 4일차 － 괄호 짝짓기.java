import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {

    static BufferedReader br;
    static Map<Character, Character> map;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));

        map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        map.put('>', '<');

        for (int tc = 1; tc <= 10; tc++) {
            System.out.println("#" + tc + " " + check());
        }
    }
	
	static int check() throws Exception {
	    int len = Integer.parseInt(br.readLine());
	    String s = br.readLine();

	    Stack<Character> st = new Stack<>();

	    for (int i = 0; i < len; i++) {
	        char c = s.charAt(i);

	        if (c=='(' || c=='[' || c=='{' || c=='<') {
	            st.push(c);
	        } else { // 닫는 괄호
	            if (st.isEmpty() || st.pop() != map.get(c)) {
	                return 0;
	            }
	        }
	    }
	    return st.isEmpty() ? 1 : 0;
	}

}