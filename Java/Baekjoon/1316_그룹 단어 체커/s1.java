import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int answer = N;
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            Character former = '?';
            int[] ascii = new int[26]; //영소문자 97~122
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                if (former != c) {
                    if (ascii[c - 'a'] == 1) {
                        answer -= 1;
                        break;
                    } else {
                        ascii[c - 'a'] = 1;
                    }
                }
                former = c;
            }
        }
        bw.write(answer + "");

        br.close();
        bw.flush();
        bw.close();
    }

}
