import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

//재귀호출
public class Main {

    public static Long a;
    public static Long b;
    public static Long c;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        a = Long.parseLong(st.nextToken());
        b = Long.parseLong(st.nextToken());
        c = Long.parseLong(st.nextToken());

        System.out.println(recur(b));
    }

    public static Long recur(Long exponent) {
        if (exponent == 1) {
            return a % c;
        }

        Long val = recur(exponent/2);

        //원래 지수가 홀수일 때
        if (exponent % 2 == 1) {
            return (val * val % c) * a % c;
        } else {
            return val * val % c;
        }
    }

}
