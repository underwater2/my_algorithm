import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        HashMap<Character, Integer> map = new HashMap<>();

        int max = 0;
        boolean dupli = false;
        char answer = '!';

        for (int i = 0; i < s.length(); i++) {
            char key = Character.toUpperCase(s.charAt(i));

            if (!map.containsKey(key)) {
                map.put(key, 1);
            } else {
                map.put(key, map.get(key) + 1);
            }

            Integer newValue = map.get(key);
            if (max == newValue) {
                dupli = true;
            }

            if (max < newValue) {
                max = newValue;
                dupli = false;
                answer = key;
            }

        }

        if (dupli) {
            System.out.println("?");
        } else {
            System.out.println(answer);
        }

    }
}
