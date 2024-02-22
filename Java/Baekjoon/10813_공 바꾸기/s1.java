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
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] basket = new int[n];
        for (int a = 0; a < n; a++) {
            basket[a] = a+1;
        }

        int i, j, temp;
        for (int a = 0; a < m; a++) {
            st = new StringTokenizer(br.readLine(), " ");
            i = Integer.parseInt(st.nextToken()) - 1;
            j = Integer.parseInt(st.nextToken()) - 1;

            temp = basket[i];
            basket[i] = basket[j];
            basket[j] = temp;
        }

        for (int a = 0; a < n; a++) {
            bw.write(basket[a] + " ");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}