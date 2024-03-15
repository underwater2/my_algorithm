import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
    private int x;
    private int y;
    private int z;

    public Node(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }

    public int getZ() {
        return this.z;
    }
}

public class Main {

    private static int[][][] visited;
    private static Queue<Node> q = new LinkedList<>();
    private static int[] dx = {1, -1, 0, 0, 0, 0};
    private static int[] dy = {0, 0, 0, 0, 1, -1};
    private static int[] dz = {0, 0, -1, 1, 0 ,0}; //위, 아래, 왼, 오른, 앞, 뒤
    private static int M;
    private static int N;
    private static int H;
    private static int[][][] tomato;
    private static int ans;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        tomato = new int[H][N][M];
        visited = new int[H][N][M];

        for (int h = 0; h < H; h++) {
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                for (int j = 0; j < M; j++) {
                    int status = Integer.parseInt(st.nextToken());
                    tomato[h][i][j] = status;
                    if (status == 1) {
                        q.add(new Node(h, i, j));
                        visited[h][i][j] = 1;
                    }
                }
            }
        }

        bfs();

        //3차원 배열 출력
//        for (int h = 0; h < tomato.length; h++) {
//            for (int i = 0; i < tomato[0].length; i++) {
//                for (int j = 0; j < tomato[0][0].length; j++) {
//                    System.out.print(tomato[h][i][j] + " ");
//                }
//                System.out.println();
//            }
//            System.out.println();
//        }


        int max = 0;
        for (int h = 0; h < tomato.length; h++) {
            for (int i = 0; i < tomato[0].length; i++) {
                for (int j = 0; j < tomato[0][0].length; j++) {
                    if (ans != -1) {
                        if (tomato[h][i][j] == 0) {
                            ans = -1;
                        }
                        max = Math.max(tomato[h][i][j], max);
                    }
                }
            }
        }

        System.out.println(ans == -1 ? -1 : max-1);
    }

    private static void bfs() {

        while(!q.isEmpty()) {
            Node now = q.poll();

            for (int t = 0; t < 6; t++) {
                int ndx = now.getX() + dx[t];
                int ndy = now.getY() + dy[t];
                int ndz = now.getZ() + dz[t];

                if (ndx >= 0 && ndx < H && ndy >= 0 && ndy < N && ndz >= 0 && ndz < M) {
                    if (tomato[ndx][ndy][ndz] > -1 && visited[ndx][ndy][ndz] == 0) {
                        q.add(new Node(ndx, ndy, ndz));
                        tomato[ndx][ndy][ndz] = tomato[now.getX()][now.getY()][now.getZ()] + 1;
                        visited[ndx][ndy][ndz] = 1;
                    }
                }
            }
        }

    }

}
