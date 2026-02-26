import java.util.Arrays;
import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a= sc.nextInt();
		int b= sc.nextInt();
		int c= sc.nextInt();
		
		int[] arr = new int[10];
		String s = a*b*c +"";
		
		for(int i=0; i<s.length(); i++) {
			arr[s.charAt(i) - '0']+=1;
		}
		for(int i=0; i<arr.length; i++)
			System.out.println(arr[i]);
		
		
	}
}