import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

//        bw.write('z' - 'a' + ""); //25 -> 알파벳 26개
//        bw.write('a' + 0 + ""); //97
//        bw.write('z' + 0 + ""); //122

        String s = br.readLine();
        int[] arr = new int[26];
        for (int i = 0; i < 26; i++) {
            arr[i] = -1;
        }

        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 97;
            if (arr[idx] == -1) {
                arr[s.charAt(i) - 97] = i;
            }
        }

        for (int i = 0; i < 26; i++) {
            bw.write(arr[i] + " ");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}