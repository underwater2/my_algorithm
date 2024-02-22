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

        int[] baskets = new int[n];
        for (int i = 0; i < n; i++) {
            baskets[i] = i+1;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int front = start;
            int back  = end;
            int temp;
            for (int j = 0; j < (end - start + 1)/2; j++) {
                temp = baskets[front-1];
                baskets[front-1] = baskets[back-1];
                baskets[back-1] = temp;
                front += 1;
                back -= 1;
            }
        }

        for (int i = 0; i < baskets.length; i++) {
            bw.write(baskets[i] + " ");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}