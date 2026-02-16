import java.util.Arrays;
import java.util.Scanner;

class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
            sc.nextLine(); // nextInt() 뒤에 남아있는 엔터 처리**********


			String[] arrA = sc.nextLine().trim().split(" ");
			String[] arrB = sc.nextLine().trim().split(" ");

		
			int idx = 0;
			boolean ok =true;
			
			for (int i = 0; i < M; i++) {
				boolean check = false;
				for (int j = idx; j < N; j++) {
					if (arrB[i].equals(arrA[j])) {
						idx = j+1;
						check = true;
						break;
					}

				}
				if (!check) {
					ok=false;
					break;
				}
			}
			System.out.println("#" + tc + " " + (ok ? "YES" : "NO"));
		}

	}
}
