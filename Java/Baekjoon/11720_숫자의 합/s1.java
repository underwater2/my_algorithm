import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        //다양한 풀이 방법 참고) https://jumping-to-the-water.tistory.com/46

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        String nums = br.readLine();
        int answer = 0;
        for (int i = 0; i < n; i++) {
            answer += nums.charAt(i) - '0';
        }

        bw.write(answer + "");

        br.close();
        bw.flush();
        bw.close();
    }
}