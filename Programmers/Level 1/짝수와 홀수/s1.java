class Solution {
    public String solution(int num) {
        num = Math.abs(num);
        if (num == 0) {
            return "Even";
        }

        if (num % 2 == 1) {
            return "Odd";
        } else {
            return "Even";
        }
    }
}