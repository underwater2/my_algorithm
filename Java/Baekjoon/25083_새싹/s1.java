import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write("         ,r'\"7" + "\n");
        bw.write("r`-_   ,'  ,/" + "\n");
        bw.write(" \\. \". L_r'" + "\n");
        bw.write("   `~\\/" + "\n");
        bw.write("      |" + "\n");
        bw.write("      |" + "\n");

        br.close();
        bw.flush();
        bw.close();
    }
}