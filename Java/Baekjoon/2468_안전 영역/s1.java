import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
    private int x;
    private int y;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}

public class Main {

    private static int[][] visited;
    private static Queue<Node> q = new LinkedList<>();
    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, 1, 0, -1}; //우하좌상
    private static int N;
    private static int[][] soil;
    private static int ans;
    private static int max = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        soil = new int[N][N];
        visited = new int[N][N];

        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                soil[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int height = 0; height <= 100; height++) {
            ans = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (soil[i][j] > height && visited[i][j] == 0) {
                        visited[i][j] = 1;
                        bfs(i, j, height);
                    }
                }
            }
            max = Math.max(max, ans);
            visited = new int[N][N];
        }
        System.out.println(max);

    }

    private static void bfs(int i, int j, int height) {
        ans += 1;
        q.add(new Node(i, j));

        while (!q.isEmpty()) {
            Node now = q.poll();
            int x = now.getX();
            int y = now.getY();

            for (int t = 0; t < 4; t++) {
                int nx = x + dx[t];
                int ny = y + dy[t];
                if (nx >= 0 && nx < N && ny >= 0 && ny < N && visited[nx][ny] == 0 && soil[nx][ny] > height) {
                    q.add(new Node(nx, ny));
                    visited[nx][ny] = 1;
                }
            }
        }
    }
}
