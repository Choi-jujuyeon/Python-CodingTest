import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution{
	static int[] arr;
	static int[] tmp;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		arr = new int[1000000];
		tmp = new int[1000000];
		
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		for(int i=0; i<1000000; i++) arr[i] = Integer.parseInt(st.nextToken());
		
		mergeSort(0,1000000-1);
		System.out.println(arr[500000]);
	}
	
	static void mergeSort(int left, int right) {
		if(left>= right) return;
		int mid = (left+right)/2;
		mergeSort(left, mid);
		mergeSort(mid+1,right);
		merge(left, mid, right);
		
	}
	static void merge(int left, int mid, int right) {
		int lp = left;
		int rp = mid +1;
		int start = left;
		
		while(lp <= mid && rp<=right) {
			if(arr[lp] <= arr[rp]) tmp[start++] = arr[lp++];
			else tmp[start++] = arr[rp++];
		}
		while(lp<=mid) tmp[start++] = arr[lp++];
		while(rp<=right) tmp[start++] = arr[rp++];
		
		for(int i=left; i<=right; i++) {
			arr[i] = tmp[i];
		}
		
	}
}