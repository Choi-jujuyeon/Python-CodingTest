import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution{
    static BufferedReader br;

    public static void main(String[] args)throws Exception{
        br=new BufferedReader(new InputStreamReader(System.in));
        int tc=Integer.parseInt(br.readLine().trim());
        for(int t=1;t<=tc;t++){
            int k=Integer.parseInt(br.readLine().trim());
            System.out.println("#"+t+" "+check(k));
        }
    }

    static int check(int k)throws Exception{
        Stack<Integer> st=new Stack<>();
        for(int i=0;i<k;i++){
            int num=Integer.parseInt(br.readLine().trim());
            if(num!=0)st.push(num);
            else if(!st.isEmpty())st.pop();
        }
        int sum=0;
        while(!st.isEmpty())sum+=st.pop();
        return sum;
    }
}
