class Solution {
    public int[] solution(String s) {
        int cnt = 0;
        int zero = 0;
        while (!s.equals("1")) {
            long one = s.chars().filter(ch -> ch == '1').count();
            zero += s.length() - one;
            s = Integer.toBinaryString((int) one);
            cnt += 1;
        }
        int[] answer = {cnt, zero};
        return answer;
    }
}