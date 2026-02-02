import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int[] days = {31,28,31,20,31,30,31,31,30,31,30,31};
		
		for(int i=0; i<T; i++) {
			String date = sc.next();
			String y =date.substring(0,4);
			int m= Integer.parseInt(date.substring(4,6));
			int d= Integer.parseInt(date.substring(6,8));
			
			
			//true일경우 처리
			boolean check = (1<=m && m<=12) && (d>=1 && d<=days[m-1]);
			
			if(check)
				System.out.printf("#%d %s/%02d/%02d\n",i+1,y,m,d);
			else
				System.out.printf("#%d -1\n",i+1);	
		}
	}
}
