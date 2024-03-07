//시간 줄이려고 코드를 추가해봤는데 오히려 12ms 더걸리고 메모리도 증가...

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] m = new int[N+1];
        int[] c = new int[N+1];

        StringTokenizer sti = new StringTokenizer(br.readLine(), " ");
        StringTokenizer stj = new StringTokenizer(br.readLine(), " ");
        int height = 1;
        for (int i = 1; i < N+1; i++) {
            m[i] = Integer.parseInt(sti.nextToken());
            c[i] = Integer.parseInt(stj.nextToken());
            height += c[i];
        }

        int[][] dp = new int[height][N+1];

        for (int j = 1; j < N+1; j++) {
            for (int i = 0; i < height; i++){
                if (i >= c[j]) {
                    dp[i][j] = Math.max(m[j] + dp[i-c[j]][j-1], dp[i][j-1]);
                } else {
                    dp[i][j] = dp[i][j-1];
                }

                if (dp[i][j] >= M) {
                    break;
                }
            }
        }

//        for(int[] array : dp) {
//            for(int k : array) {
//                System.out.print(k + " ");
//            }
//            System.out.println();
//        }

        for (int i = 0; i < height; i++) {
            if (dp[i][N] >= M) {
                bw.write(i + "");
                break;
            }
        }

        br.close();
        bw.flush();
        bw.close();
    }

}
