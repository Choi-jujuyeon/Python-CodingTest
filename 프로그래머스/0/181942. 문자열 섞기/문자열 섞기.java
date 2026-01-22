class Solution {
    public String solution(String str1, String str2) {
        int n=str1.length();
        StringBuilder sb = new StringBuilder(n*2);
        
        for(int i=0; i<n; i++){
            sb.append(str1.charAt(i)).append(str2.charAt(i));
        }
        return sb.toString();
    }
}