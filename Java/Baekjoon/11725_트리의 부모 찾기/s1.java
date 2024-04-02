import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static ArrayList<Integer>[] edge;
    static int[] visited;
    static int[] parent;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        edge = new ArrayList[N+1];
        visited = new int[N+1];
        parent = new int[N+1];

        for (int i = 1; i < N+1; i++) {
            edge[i] = new ArrayList<>();
        }

        StringTokenizer st;
        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edge[a].add(b);
            edge[b].add(a);
        }

        bfs();
        for (int i = 2; i < N+1; i++) {
            System.out.println(parent[i]);
        }
    }

    private static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        visited[1] = 1;

        while(!q.isEmpty()) {
            Integer now = q.poll();

            for (Integer node : edge[now]) {
                if (visited[node] == 0) {
                    q.add(node);
                    visited[node] = 1;

                    parent[node] = now;
                }
            }
        }
    }
}
