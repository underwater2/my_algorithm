import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();
        char c = s.charAt(0);
        bw.write(c + 0 + ""); //65

//        //참고
//        int i = c + 1;
//        System.out.println(c + 1); //66 -> int 숫자 그대로 나온다.
//        bw.write(c + 1); //B -> int를 넣으면 해당하는 아스키 문자가 나온다.
//        bw.write(65); //A

        br.close();
        bw.flush();
        bw.close();
    }
}