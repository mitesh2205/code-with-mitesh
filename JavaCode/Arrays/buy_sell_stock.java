public class buy_sell_stock {

    public static void max_profit(int prices[]) {
        int i = 0;
        int j = 1;
        int max_profit = 0;

        while (j < prices.length) {
            if (prices[i] < prices[j]) {
                max_profit = Math.max(max_profit, prices[j] - prices[i]);
            } else {
                i = j;
            }
            j += 1;
        }
        System.out.println(max_profit);

    }

    public static void main(String[] args) {
        int prices[] = { 7, 1, 5, 3, 6, 4 };
        max_profit(prices);
    }

}