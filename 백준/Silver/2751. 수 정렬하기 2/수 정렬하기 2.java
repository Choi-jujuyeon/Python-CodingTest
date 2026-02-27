import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main{
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine().trim());
		
		int[] arr = new int[T];
		for(int i=0; i<T; i++) {
			arr[i] = Integer.parseInt(br.readLine().trim());
		}
		
		Arrays.sort(arr);
		for(int i=0; i<T; i++) {
			sb.append(arr[i]).append('\n');
		}
		System.out.println(sb);
	}
}