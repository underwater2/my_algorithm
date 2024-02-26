import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();
        String[] arr = {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            String alphabet = s.charAt(i) + "";
            for (int j = 0; j < arr.length; j++) {
                if (arr[j].contains(alphabet)) {
                    count += j + 3;
                    break;
                }
            }
        }
        bw.write(count + "");

        br.close();
        bw.flush();
        bw.close();
    }
}