import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String firstLine = sc.nextLine();
        int n = Integer.parseInt(firstLine);
        int mountains[][] = new int[n][n];

        for (int i = 0; i < n; i++) {
            String row = sc.nextLine();
            String ele[] = row.split(" ");
            for (int j = 0; j < n; j++) {
                mountains[i][j] = Integer.parseInt(ele[j]);
            }
        }
        Main sol = new Main();
        System.out.println(sol.findWallHeight(mountains));
    }

    public int findWallHeight(int[][] mountains) {
        int n = mountains.length;
        int maxIslands = 0, minHeight = 0;

        for (int h = 1; h <= 10; h++) {
            boolean[][] visited = new boolean[n][n];
            int islands = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (mountains[i][j] > h && !visited[i][j]) {
                        dfs(mountains, visited, i, j, h);
                        islands++;
                    }
                }
            }
            if (islands > maxIslands) {
                maxIslands = islands;
                minHeight = h;
            }
        }

        return minHeight;
    }

    private void dfs(int[][] mountains, boolean[][] visited, int i, int j, int mid) {
        int n = mountains.length;
        if (i < 0 || i >= n || j < 0 || j >= n || mountains[i][j] <= mid || visited[i][j]) {
            return;
        }
        visited[i][j] = true;
        dfs(mountains, visited, i-1, j, mid);
        dfs(mountains, visited, i+1, j, mid);
        dfs(mountains, visited, i, j-1, mid);
        dfs(mountains, visited, i, j+1, mid);
    }

}