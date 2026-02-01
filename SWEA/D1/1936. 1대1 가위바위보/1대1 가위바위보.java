import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a= sc.nextInt();
		int b= sc.nextInt();
		
		//A가 이기는 조건만
		if((a==1 && b==3) ||(a==2&&b==3) || (a==3 &&b==2))
			System.out.println("A");
		else
			System.out.println("B");		
	}
}
