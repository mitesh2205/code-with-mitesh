public class container_with_most_water {
    public static void most_water(int height[]) {
        int area = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            area = Math.max(area, Math.min(height[left], height[right]) * Math.abs(right - left));
            if (height[left] < height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        System.out.println(area);
    }

    public static void main(String[] args) {
        int height[] = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
        most_water(height);
    }
}
