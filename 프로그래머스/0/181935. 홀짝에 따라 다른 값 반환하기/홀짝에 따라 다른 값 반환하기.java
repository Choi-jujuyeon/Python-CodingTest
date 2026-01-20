class Solution {
    public int solution(int n) {
        int sum=0;
        //홀수라면 n이하의 홀수인 모든 양의 정수 합
        if(n%2==0){
            for(int i=2; i<=n; i+=2){
                sum+=i*i;
            }
        }else{
            for(int i=1; i<=n; i+=2){
                sum+=i;
            }
        }
        return sum;
        
        //짝수라면 n이하의 짝수 중 정수의 제곱 합
    }
}