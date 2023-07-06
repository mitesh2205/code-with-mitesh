import java.util.HashMap;
import java.util.Map;

public class player_of_year {
    public static int playerOfYear(int N, int M, int[][] data) {
        Map<Integer, Integer> leaderboard = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            leaderboard.put(i, 0);
        }

        for (int j = 0; j < M; j++) {
            int maxScore = Integer.MIN_VALUE;
            for (int i = 0; i < N; i++) {
                maxScore = Math.max(maxScore, data[i][j]);
            }
            for (int i = 0; i < N; i++) {
                if (data[i][j] == maxScore) {
                    leaderboard.put(i + 1, leaderboard.get(i + 1) + 1);
                }
            }
        }

        int maxCount = Integer.MIN_VALUE;
        int playerOfYear = -1;
        for (Map.Entry<Integer, Integer> entry : leaderboard.entrySet()) {
            int player = entry.getKey();
            int count = entry.getValue();
            if (count > maxCount) {
                maxCount = count;
                playerOfYear = player;
            }
        }

        return playerOfYear;
    }

    public static void main(String[] args) {
        int N = 5;
        int M = 3;
        int[][] data = { { 5, 9, 5 }, { 8, 9, 3 }, { 11, 9, 9 }, { 6, 11, 2 }, { 2, 2, 5 } };
        System.out.println(playerOfYear(N, M, data));

        N = 2;
        M = 3;
        data = new int[][] { { 4, 2, 10 }, { 5, 8, 9 } };
        System.out.println(playerOfYear(N, M, data));

        N = 3;
        M = 4;
        data = new int[][] { { 1, 3, 4, 5 }, { 7, 2, 3, 4 }, { 1, 3, 2, 1 } };
        System.out.println(playerOfYear(N, M, data));
    }
}
