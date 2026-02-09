import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());

		for(int i=1; i<T+1; i++) {
			
			br.readLine();
			String[] arr = br.readLine().split(" ");

			int n = arr.length;
			int mid = (n + 1) / 2;

			int left= 0;
			int right= mid;

			StringBuilder sb = new StringBuilder();

			while (left<mid || right < n) {
			    if (left<mid) sb.append(arr[left++]).append(' ');
			    if (right<n) sb.append(arr[right++]).append(' ');
			}

			sb.setLength(sb.length() - 1);
			System.out.println("#"+i+" "+sb);

		}
		
	}
}
