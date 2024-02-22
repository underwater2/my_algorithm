import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int max = -1;
        int idx = 0;
        int now;
        for (int i = 0; i < 9; i++) {
            now = Integer.parseInt(br.readLine());
            if (max < now) {
                max = now;
                idx = i+1;
            }
        }

        bw.write(max + "\n" + idx);

        br.close();
        bw.flush();
        bw.close();
    }
}