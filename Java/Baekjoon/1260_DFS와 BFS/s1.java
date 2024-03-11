import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static Boolean[] visited;
    private static Boolean[][] edge;

    private static BufferedWriter bw;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        edge = new Boolean[N+1][N+1];
        for (int i = 0; i < N+1; i++) {
            Arrays.fill(edge[i], false);
        }

        int row = 0;
        int column = 0;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            row = Integer.parseInt(st.nextToken());
            column = Integer.parseInt(st.nextToken());
            edge[row][column] = true;
            edge[column][row] = true;
        }

        visited = new Boolean[N+1];
        Arrays.fill(visited, false);

        visited[V] = true;
        bw.write(V + " ");
        dfs(V);
        bw.write("\n");

        Arrays.fill(visited, false);
        bfs(V);

        br.close();
        bw.flush();
        bw.close();
    }

    private static void dfs(int v) throws IOException {
        for (int i = 1; i < N+1; i++) {
            if (edge[v][i] == true && visited[i] == false ) {
                bw.write(i + " ");
                visited[i] = true;
                dfs(i);
            }
        }
    }

    private static void bfs(int v) throws IOException {
        Queue<Integer> que = new LinkedList<>();
        que.add(v);
        visited[v] = true;

        while (!que.isEmpty()) {
            int now = que.poll();
            bw.write(now + " ");

            for (int i = 1; i < N+1; i++) {
                if (edge[now][i] == true && visited[i] == false) {
                    que.add(i);
                    visited[i] = true;
                }
            }
        }
    }

}
