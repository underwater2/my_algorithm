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

        int[] pieces = {1, 1, 2, 2, 2, 8};

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < 6; i++) {
            int now = Integer.parseInt(st.nextToken());
            bw.write((pieces[i] - now) + " ");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}