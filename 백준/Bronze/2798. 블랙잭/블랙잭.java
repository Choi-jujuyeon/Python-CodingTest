import java.util.Scanner;

class Main{
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int totalSum = sc.nextInt();
		int[] arr = new int[N];
		for(int i=0; i<N; i++) 
			arr[i] = sc.nextInt();
		
		int max = Integer.MIN_VALUE;
		// 이중에서 3개를 뽑아서 21을 넘지 않는 최대의 수를 구해라!
		for(int i=0; i<N; i++) {
			for(int j=i+1; j<N; j++){
				for(int k=j+1; k<N; k++) {
					int a = arr[i]+arr[j]+arr[k];
					if(max<a && totalSum>=a) max = a;
				}
			}
		}
		
		
		System.out.println(max);
	}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
}