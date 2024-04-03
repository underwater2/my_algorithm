import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;
import java.util.StringTokenizer;

class Node {
    int i;
    int j;

    public Node(int i, int j) {
        this.i = i;
        this.j = j;
    }

    public int getI() {
        return i;
    }

    public int getJ() {
        return j;
    }
}

public class Main {


    static int M;
    static int N;
    static int K;
    static int[][] arr;
    static int count;
    static ArrayList<Integer> area = new ArrayList<>();
    static Stack<Node> s = new Stack<>();
    static int[] di = {0, 1, 0, -1}; //우하좌상
    static int[] dj = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine(), " ");
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[M][N];

        int lx;
        int ly;
        int rx;
        int ry;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            lx = Integer.parseInt(st.nextToken());
            ly = Integer.parseInt(st.nextToken());
            rx = Integer.parseInt(st.nextToken());
            ry = Integer.parseInt(st.nextToken());
            for (int jj = rx-1; jj >= lx; jj--) {
                for (int ii = M-ry; ii < M-ly; ii++) {
                    arr[ii][jj] = 1;
                }
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 0) {
                    dfs(i, j);
                }
            }
        }

        bw.write(count + "\n");
        Collections.sort(area);
        for (int i = 0; i < area.size(); i++) {
            bw.write(area.get(i) + " ");
        }

        bw.flush();
        bw.close();
    }

    private static void dfs(int i, int j) {

        count += 1;
        int areaComp = 1;
        s.push(new Node(i, j));
        arr[i][j] = 1;

        while(!s.isEmpty()) {

            Node now = s.pop();

            for (int t = 0; t < 4; t++) {
                int ndi = now.getI() + di[t];
                int ndj = now.getJ() + dj[t];
                if (0 <= ndi && ndi < M && 0 <= ndj && ndj < N) {
                    if (arr[ndi][ndj] == 0) {
                        s.push(new Node(ndi, ndj));
                        arr[ndi][ndj] = 1;
                        areaComp += 1;
                    }
                }
            }
        }
        area.add(areaComp);
    }
}
