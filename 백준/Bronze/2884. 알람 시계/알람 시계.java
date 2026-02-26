import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int H =sc.nextInt();
		int M = sc.nextInt();
		
		int T = H*60 +M - 45;
		
		int hh = T/60;
		int mm =T%60;
		
		if(mm<0) {
			hh=23;
			mm+=60;
		}
				
		
		System.out.println(hh+" "+mm);	}
}