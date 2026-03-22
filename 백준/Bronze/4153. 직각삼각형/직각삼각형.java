import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main{
	  public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			if(a == 0 && b==0 && c==0) break;
			
			int max = Math.max(a, Math.max(b, c));
			
			boolean check=false;
			if(a==max) check = (a*a == b*b+c*c);
			else if(b==max) check = (b*b == a*a+c*c);
			else check = (c*c == b*b+a*a);
			
			System.out.println(check?"right":"wrong");
			
			
		}
	}
}