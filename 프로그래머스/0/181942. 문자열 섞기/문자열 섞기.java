class Solution {
    public String solution(String str1, String str2) {
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<str1.length(); i++){
            char c1 = str1.charAt(i);
            char c2 = str2.charAt(i);
            sb.append(c1);
            sb.append(c2);
        }
        return sb.toString();
    }
}