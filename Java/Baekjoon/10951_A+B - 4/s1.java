import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String line;

        while ((line = br.readLine()) != null) {
            bw.write((line.charAt(0) - '0') + (line.charAt(2) - '0') + "\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}