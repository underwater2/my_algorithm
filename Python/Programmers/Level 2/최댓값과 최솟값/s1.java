import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String[] words = s.split(" ");
        int[] nums = Arrays.stream(words).mapToInt(Integer::parseInt).toArray();
        int max = Arrays.stream(nums)
                .max()
                .getAsInt();
        int min = Arrays.stream(nums)
                .min()
                .getAsInt();
        String maxS = Integer.toString(max);
        String minS = Integer.toString(min);
        String answer = minS + " " + maxS;
        return answer;
    }
}