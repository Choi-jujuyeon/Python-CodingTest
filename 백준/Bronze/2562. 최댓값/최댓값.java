import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int ans=0;
		int max=Integer.MIN_VALUE;
		
		for(int i=0; i<9; i++) {
			int a = sc.nextInt();
			if(a>max) {
				max=a;
				ans=i+1;
			}
		}
		System.out.println(max+"\n"+ans);
	}
}