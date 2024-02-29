import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.EmptyStackException;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Stack<Character> former = new Stack<>();
        Stack<Character> latter = new Stack<>();

        String s = br.readLine();
        for (int i = 0; i < s.length(); i++) {
            former.push(s.charAt(i));
        }

        int M = Integer.parseInt(br.readLine());

        String order;
        Character a;
        for (int i = 0; i < M; i++) {
            order = br.readLine();
            a = order.charAt(0);
            try {
                if (a == 'L') {
                    latter.push(former.pop());
                } else if (a == 'D') {
                    former.push(latter.pop());
                } else if (a == 'B') {
                    former.pop();
                } else if (a == 'P') {
                    former.push(order.charAt(2));
                }
            } catch (EmptyStackException e) {}
        }

        StringBuilder sb = new StringBuilder();
        while (!former.empty()) {
            sb.append(former.pop());
        }
        sb.reverse();

        while (!latter.empty()) {
            sb.append(latter.pop());
        }
        bw.write(sb.toString());

        br.close();
        bw.flush();
        bw.close();
    }

}
