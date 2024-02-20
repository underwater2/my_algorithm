import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int a = Integer.parseInt(br.readLine());
        String bStr = br.readLine();
        char[] b = bStr.toCharArray();

        //parameter type should be str, not char
        bw.write((a * (b[2] - '0')) + "\n");
        bw.write((a * (b[1] - '0')) + "\n");
        bw.write((a * (b[0] - '0')) + "\n");
        bw.write((a * Integer.parseInt(bStr)) + "\n");

        br.close();
        bw.close();
    }
}