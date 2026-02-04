import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 1; tc <= 10; tc++) {
            br.readLine();                 
            String word = br.readLine();   
            String text = br.readLine();   

            int tLen = text.length();
            int wLen = word.length();

            int ans = 0;

            for (int j = 0; j <= tLen - wLen; j++) {
                int k = 0;
                while (k < wLen && text.charAt(j + k) == word.charAt(k)) {
                    k++;
                }
                if (k == wLen) ans++;
            }

            System.out.println("#" + tc + " " + ans);
        }
    }
}
