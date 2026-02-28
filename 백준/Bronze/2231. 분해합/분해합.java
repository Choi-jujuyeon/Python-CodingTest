import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
	
	//자릿수 체크ㄱㄱ
	static long check(int x) {
		int sum=0;
		while(x>0) {
			sum+=x%10;
			x/=10;
		}
		return sum;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine().trim());
		int min =0;
		for(int i=1; i<N; i++) {
			if(i+check(i) == N) {
				min=i;
				break;
			}
		}
		System.out.println(min);
	}
}