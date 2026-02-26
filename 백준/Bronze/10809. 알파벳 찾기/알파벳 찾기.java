import java.util.Arrays;
import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        int[] pos = new int[26];
        Arrays.fill(pos, -1);

        for(int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if(pos[idx] == -1) pos[idx] = i;
        }

        for(int i = 0; i < 26; i++) {
            System.out.print(pos[i] + " ");
        }
    }
}