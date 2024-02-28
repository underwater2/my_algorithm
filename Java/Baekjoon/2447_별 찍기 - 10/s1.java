import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {

    private static Character[][] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        arr = new Character[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = ' ';
            }
        }

        recur(N, 0, 0);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                bw.write(arr[i][j]);
            }
            bw.write("\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }


    private static void recur(int n, int istart, int jstart) {
        if (n == 1) {
            arr[istart][jstart] = '*';
            return;
        }

        //1번째줄
        recur(n/3, istart, jstart + 0);
        recur(n/3, istart, jstart + (n/3));
        recur(n/3, istart, jstart + (2 * n/3));

        //2번째줄
        recur(n/3, istart + (n/3), jstart + 0);
        recur(n/3, istart + (n/3), jstart + (2 * n/3));

        //3번째줄
        recur(n/3, istart + (2 * n/3), jstart + 0);
        recur(n/3, istart + (2 * n/3), jstart + (n/3));
        recur(n/3, istart + (2 * n/3), jstart + (2 * n/3));
    }

    /*
        N = 1

        *


        N = 3

        N=1 이 3 2 3 -> 8개
        빈칸 1*1 1개

        ***
        * *
        ***


        N = 9

        N=3 이 3 2 3 -> 8개
        빈칸 3*3 1개

        (0~N/3-1) (N/3~(2N/3-1)) (2N/3~(N-1))
        0~2 3~5 6~8
        ********* 0~2
        * ** ** *
        *********
        ***   *** 3~5 (N/3~(2N/3-1))
        * *   * *
        ***   ***
        ********* 6~8
        * ** ** *
        *********



        N = 27
        N=9 이 3 2 3 -> 8개
        빈칸 9*9 1개

        ***************************
        * ** ** ** ** ** ** ** ** *
        ***************************
        ***   ******   ******   ***
        * *   * ** *   * ** *   * *
        ***   ******   ******   ***
        ***************************
        * ** ** ** ** ** ** ** ** *
        ***************************
        *********         *********
        * ** ** *         * ** ** *
        *********         *********
        ***   ***         ***   ***
        * *   * *         * *   * *
        ***   ***         ***   ***
        *********         *********
        * ** ** *         * ** ** *
        *********         *********
        ***************************
        * ** ** ** ** ** ** ** ** *
        ***************************
        ***   ******   ******   ***
        * *   * ** *   * ** *   * *
        ***   ******   ******   ***
        ***************************
        * ** ** ** ** ** ** ** ** *
        ***************************


     */

}
