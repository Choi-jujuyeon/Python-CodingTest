import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // String result = (n%2==0)?"is even": "is odd" ;
        // System.out.printf(n+" "+result);
        System.out.printf(n + " is "+ ((n%2==0)? "even":"odd"));
    }
}