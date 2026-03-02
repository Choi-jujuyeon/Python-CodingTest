import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        long ans = 1; 
        for(int i=N; i>0; i--) {
        	ans*=i;
        }
        System.out.println(ans);
    }
    
}