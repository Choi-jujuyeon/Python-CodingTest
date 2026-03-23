import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] tmp = new int[6];
		for(int i=0; i<6; i++) 
			tmp[i] = sc.nextInt();
		int T = sc.nextInt();
		int P = sc.nextInt();
		
		int shirt = 0;
		int ans =0;
		
		for(int i=0; i<6; i++) {
			shirt += (tmp[i] + T -1) /T;
			ans +=tmp[i];
		}
		
		int bundlePens = 0;
		int Pen =0;
		
		bundlePens = ans/P;
		Pen = ans%P;
		
		System.out.println(shirt);
		System.out.println(bundlePens + " "+Pen);
		
		
	}
}