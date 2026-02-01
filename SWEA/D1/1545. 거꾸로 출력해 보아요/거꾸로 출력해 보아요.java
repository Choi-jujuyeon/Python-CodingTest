import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for (int test_case = 0; test_case <= T; test_case++) {
            System.out.print(T - test_case + " ");
        }
	}
}