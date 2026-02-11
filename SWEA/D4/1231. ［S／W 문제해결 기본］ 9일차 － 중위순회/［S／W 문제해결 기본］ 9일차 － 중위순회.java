import java.util.Scanner;

class Solution {
	static int N;
	static char[] tree;
	static StringBuilder sb;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		for (int tc = 1; tc <= 10; tc++) {
			N = sc.nextInt();
			tree = new char[N + 1];

			for (int i = 0; i < N; i++) {
				int idx = sc.nextInt();
				String a = sc.next();
				sc.nextLine();
				tree[idx] = a.charAt(0);
			}
			sb = new StringBuilder();
			inorder(1);

			System.out.println("#" + tc + " " + sb.toString());
		}
	}

	static void inorder(int v) {
		if (v > N) return;

		// 중위 == 왼중오
		inorder(v * 2);
		sb.append(tree[v]);
		inorder(v * 2 + 1);
	}
}
