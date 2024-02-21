import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] nums = {a, b, c};
        Arrays.sort(nums);

        if (nums[0] == nums[1] && nums[1] == nums[2]) {
            bw.write(10000 + nums[0] * 1000 + "");
        } else if (nums[0] == nums[1] || nums[1] == nums[2]) {
            bw.write(1000 + nums[1] * 100 + "");
        } else {
            bw.write(nums[2] * 100 + "");
        }

        br.close();
        bw.close();
    }
}