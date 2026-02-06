import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc = 1; tc<=10; tc++) {
			br.readLine();
			String[] s = br.readLine().split("\\+");
			System.out.println("#"+tc+" "+ check(s,0));
			
		}
	}
	public static int check(String[] arr, int cnt) {
		
		//baseCase
		if(cnt==arr.length)
			return 0;
		return Integer.parseInt(arr[cnt])+check(arr,cnt+1);
	}
}