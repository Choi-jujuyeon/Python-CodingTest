import java.io.*;
import java.util.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            // 친구 관계 저장할 그래프
            ArrayList<Integer>[] graph = new ArrayList[N + 1];
            for (int i = 1; i <= N; i++) {
                graph[i] = new ArrayList<>();
            }

            // 친구 관계 입력
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine().trim());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                graph[a].add(b);
                graph[b].add(a);
            }

            // BFS 준비
            boolean[] visited = new boolean[N + 1];
            int[] depth = new int[N + 1];

            Queue<Integer> q = new LinkedList<>();
            q.offer(1);         // 상원이부터 시작
            visited[1] = true;

            int count = 0;

            while (!q.isEmpty()) {
                int cur = q.poll();

                for (int next : graph[cur]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        depth[next] = depth[cur] + 1;

                        // 친구 또는 친구의 친구만 초대
                        if (depth[next] <= 2) {
                            count++;
                            q.offer(next);
                        }
                    }
                }
            }

            System.out.println("#" + tc + " " + count);
        }
    }
}