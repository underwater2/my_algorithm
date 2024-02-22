import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //만약 입력 문자열의 맨 앞이나 맨 뒤에 공백이 있다면, StringTokenizer는 이 공백을 무시하고 토큰을 추출한다.
        StringTokenizer st = new StringTokenizer(br.readLine());
        int count = 0;
        while (st.hasMoreTokens()) {
            st.nextToken();
            count += 1;
        }
        bw.write(count + "");

        br.close();
        bw.flush();
        bw.close();
    }
}