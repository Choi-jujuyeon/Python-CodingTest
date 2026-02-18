import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N=sc.nextInt();
			int M = sc.nextInt();
			
			String s = sc.next();
			String[] arr =s.split("");
			
			String result="";
			
			for(int i=0; i<=N-M; i++) {
				
				boolean check=true;
				
                for(int k=0; k<M/2; k++) {
                    if(!arr[i+k].equals(arr[i+M-1-k])) {
                        check = false;
                        break;
                    }
                }
				if(check) {
					for(int r=i; r<i+M; r++) result+=arr[r];
					break;
				}
			}
            System.out.println("#"+tc+" "+(result.isEmpty() ? "NONE" : result));
			
		}
	}
}