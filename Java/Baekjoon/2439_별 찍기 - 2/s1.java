import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder(" ".repeat(n-1) + "*");

        for (int i = 0; i < n-1; i++) {
            bw.write(sb + "\n");
            sb.setCharAt(n-i-2, '*');
        }
        bw.write(sb + "");

        br.close();
        bw.flush();
        bw.close();
    }
}