import java.io.*;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int ans=1;
        for(int i=N; i>N-K; i--) ans*=i; 
        for(int i=K; K>=1; K--) ans/=K;
        
        System.out.println(ans);
    }
}
