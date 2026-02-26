import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String ans="";
		if( n>=90) 
			ans="A";
		else if(n >=80) 
			ans="B";
		else if(n>=70) 
			ans="C";
		else if(n>=60) 
			ans="D";
		else 
			ans="F";
		System.out.println(ans);
	}
}