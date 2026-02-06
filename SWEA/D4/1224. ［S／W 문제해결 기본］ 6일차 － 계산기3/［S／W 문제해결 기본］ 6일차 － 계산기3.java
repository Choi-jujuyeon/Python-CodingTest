import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Solution {

    // 연산자 우선순위
    static int priority(char op){
        if(op=='*') return 2;
        if(op=='+') return 1;
        return 0;
    }

    // 스택 맨 위 연산 하나 계산
    static void calc(Deque<Integer> numStack, Deque<Character> opStack){
        int b=numStack.pop();
        int a=numStack.pop();
        char op=opStack.pop();

        if(op=='+') numStack.push(a+b);
        else numStack.push(a*b);
    }

    // 계산 함수
    static int solve(String exp){
        Deque<Integer> numStack=new ArrayDeque<>();
        Deque<Character> opStack=new ArrayDeque<>();

        for(int i=0;i<exp.length();i++){
            char ch=exp.charAt(i);

            if(ch>='0'&&ch<='9'){
                numStack.push(ch-'0');
            }
            else if(ch=='('){
                opStack.push(ch);
            }
            else if(ch==')'){
                while(opStack.peek()!='('){
                    calc(numStack,opStack);
                }
                opStack.pop(); // '(' 제거
            }
            else{ // + 또는 *
                while(!opStack.isEmpty()&&opStack.peek()!='('
                        &&priority(opStack.peek())>=priority(ch)){
                    calc(numStack,opStack);
                }
                opStack.push(ch);
            }
        }

        while(!opStack.isEmpty()){
            calc(numStack,opStack);
        }

        return numStack.pop();
    }

    public static void main(String[] args)throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        for(int tc=1;tc<=10;tc++){
            br.readLine();           // 길이 버림
            String exp=br.readLine();
            System.out.println("#"+tc+" "+solve(exp));
        }
    }
}
