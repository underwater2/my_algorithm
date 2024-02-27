import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

//재귀호출
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            System.out.println(recur(Integer.parseInt(br.readLine())));
        }
    }

    public static int recur(int num) {
        if (num == 1) {
            return 1;
        } else if (num == 2) {
            return 2;
        } else if (num == 3) {
            return 4;
        }

        return recur(num-1) + recur(num-2) + recur(num-3);
    }

}
