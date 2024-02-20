class Solution {
    public String solution(String s) {
        String[] arr = s.split("");

        int flag = 0;
        for(int i = 0; i < arr.length; i++) {
            if (arr[i].equals(" ")) {
                flag = 0;
            } else if (flag == 1) {
                arr[i] = arr[i].toLowerCase();
            } else {
                arr[i] = arr[i].toUpperCase();
                flag = 1;
            }
        }
        return String.join("", arr);
    }
}