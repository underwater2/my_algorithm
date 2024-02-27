import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        System.out.println((int) Math.pow(2, n) - 1);
        recur(n, 1, 2, 3);
        System.out.println(sb);
    }

    public static void recur(int n, int start, int mid, int end) {
        if (n == 1) {
            sb.append(start + " " + end + "\n");
            return;
        }

        recur(n-1, start, end, mid);
        sb.append(start + " " + end + "\n");
        recur(n-1, mid, start, end);
    }

    //N = 1
    //1 3

    //N = 2
    //1 2
    //1 3
    //2 3 <- 1

    //N = 3
    //1 3
    //1 2
    //3 2
    //1 3
    //2 1 <- 2
    //2 3
    //1 3 <- 1

    //N = 4
    //1 2
    //1 3
    //2 3
    //1 2
    //3 1
    //3 2
    //1 2
    //1 3
    //2 3 <- 3
    //2 1
    //3 1
    //2 3
    //1 2 <- 2
    //1 3
    //2 3 <- 1

}
