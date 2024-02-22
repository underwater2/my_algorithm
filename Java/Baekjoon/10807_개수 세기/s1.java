import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        Integer[] nums = new Integer[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int v = Integer.parseInt(br.readLine());

        //int 배열과 같은 Primitive 타입의 배열의 경우, Arrays.asList(배열)을 써서는 List로 변환할 수 없다.
        //-> Interger[]로 변경하면 잘된다.
        //참고) https://hianna.tistory.com/551
        bw.write(Collections.frequency(Arrays.asList(nums), v) + "");

        br.close();
        bw.flush();
        bw.close();
    }
}