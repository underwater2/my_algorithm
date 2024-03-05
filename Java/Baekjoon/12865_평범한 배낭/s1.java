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
        int K = Integer.parseInt(st.nextToken());
        int[][] dp = new int[K+1][N+1];

        //dp[W][K] = max(물건가치 + dp[W-물건무게][K-1], dp[W][K-1])
        int W;
        int V;
        for (int j = 1; j < N+1; j++) {

            st = new StringTokenizer(br.readLine(), " ");
            W = Integer.parseInt(st.nextToken());
            V = Integer.parseInt(st.nextToken());

            for (int i = 1; i < K+1; i++) {
                if (i < W) {
                    dp[i][j] = dp[i][j-1];
                } else {
                    dp[i][j] = Math.max(V + dp[i-W][j-1], dp[i][j-1]);
                }
            }

        }
        bw.write(dp[K][N] + "");

        // 2차원 배열 출력
//        for(int[] array : dp) {
//            for(int k : array) {
//                System.out.print(k + " ");
//            }
//            System.out.println();
//        }

        br.close();
        bw.flush();
        bw.close();
    }

}
