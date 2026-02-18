import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			sc.nextLine();
			String[] arr = sc.nextLine().split(" ");
			
			int start = (N + 1) / 2;
            System.out.print("#" + tc + " ");
            
            for(int i=0; i<start; i++) {
            	System.out.print(arr[i] +" ");
            	
            	if(start+i<N)
            		System.out.print(arr[start+i]+" ");
            }
            System.out.println();
		}
	}
}