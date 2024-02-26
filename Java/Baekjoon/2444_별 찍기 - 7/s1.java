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

        for (int i = 0; i < n; i++) {
            bw.write(" ".repeat(n-1-i) + "*".repeat(2 * (i+1) - 1) + "\n");
        }

        for (int i = n; i < (2 * n - 1); i++) {
            bw.write(" ".repeat(1+i-n) + "*".repeat(4*n - 2*i - 3) + "\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}