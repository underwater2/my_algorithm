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

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        String a = st.nextToken();
        String b = st.nextToken();

        int reversedA = Integer.parseInt(new StringBuffer(a).reverse().toString());
        int reversedB = Integer.parseInt(new StringBuffer(b).reverse().toString());

        bw.write(reversedA > reversedB ? reversedA + "" : reversedB + "");

        br.close();
        bw.flush();
        bw.close();
    }
}