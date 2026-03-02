import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        int ans = 1;
        for (int i = 0; i < N; i++) ans *= 2; 
        System.out.println(ans);
    }
}