import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int tc = 1; tc <= 10; tc++) {

            int N = sc.nextInt();                 // 암호문 길이
            List<Integer> list = new LinkedList<>();

            for (int i = 0; i < N; i++) {
                list.add(sc.nextInt());
            }

            int cmdCnt = sc.nextInt();            // 명령어 개수
            for (int i = 0; i < cmdCnt; i++) {

                sc.next();                        // "I"
                int pos = sc.nextInt();           // 삽입 위치 x
                int cnt = sc.nextInt();           // 삽입할 숫자 개수 y

                for (int j = 0; j < cnt; j++) {
                    list.add(pos++, sc.nextInt());
                }
            }

            System.out.print("#" + tc);
            for (int i = 0; i < 10; i++) {
                System.out.print(" " + list.get(i));
            }
            System.out.println();
        }
    }
}
