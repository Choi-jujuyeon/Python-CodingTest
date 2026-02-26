import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;
		for(int i=0; i<N; i++) {
			int n = sc.nextInt();
			if(min>n) min = n;
			if(max<n) max=n;
		}
		System.out.println(min+" "+max);
	}
}