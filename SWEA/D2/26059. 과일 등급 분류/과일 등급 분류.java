import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N =sc.nextInt();
			int lo = sc.nextInt();
			int hi = sc.nextInt();
			
			int[] arr = new int[N];
			for(int i=0; i<N; i++) arr[i] = sc.nextInt();
			
			Arrays.sort(arr);
			
			//k1 k2 어디에 둘지 + 같은 무게 쪼개면 안돼
			//몇 개로 나눠야 할지 모를때는 ArrayList를 사용해라
			ArrayList<Integer> arr2 = new ArrayList<>();
			for(int i=0; i<N-1; i++) {
				if(arr[i]!=arr[i+1])
					arr2.add(i+1); 
			}
//			System.out.println(arr2); //여기서 2개만 택하면 됌
			
			int min = Integer.MAX_VALUE;
			for(int i=0; i<arr2.size(); i++) {
				int cut1 = arr2.get(i);
				
				for(int j=i+1; j<arr2.size(); j++) {
					int cut2 = arr2.get(j);
					
					//객수만 체크
					int low = cut1;
					int mid = cut2-cut1;
					int high = N-cut2;
							
					if(low>=lo && mid>=lo && high>=lo &&low<=hi && mid<=hi && high<=hi) {
						int maxG = Math.max(low, Math.max(mid, high));
						int minG = Math.min(low, Math.min(mid, high));
						
						if(min> maxG-minG) min = maxG-minG;
					}
						
				}
			}
			System.out.println("#"+tc+" "+(min==Integer.MAX_VALUE? -1: min));

		}
	}
}