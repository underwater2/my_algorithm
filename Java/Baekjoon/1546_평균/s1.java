import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[] scores = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
        }

        int maxScore = Arrays.stream(scores).max().getAsInt();

        //double로 지정해야 소수점 뒷자리가 잘리지 않는다. int로 하면 정수 부분만 들어간다.
        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += scores[i] / (double) maxScore * 100;
        }
        bw.write(sum / n + "");

        br.close();
        bw.flush();
        bw.close();
    }
}