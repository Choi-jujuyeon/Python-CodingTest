import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T =Integer.parseInt(br.readLine().trim());
        
        HashSet<String> set = new HashSet<>();
        for(int i = 0; i < T; i++) {
            set.add(br.readLine().trim());
        }
        ArrayList<String> list = new ArrayList<>(set);

        Collections.sort(list, (a, b) -> {
            if (a.length() != b.length()) return a.length() - b.length();
            return a.compareTo(b);
        });
        for(String w: list) {
        	sb.append(w).append("\n");
        }
        System.out.println(sb);   
    }
}