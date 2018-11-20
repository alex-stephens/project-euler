public class euler_1 {

    public static void main(String[] args) {
        int n = 1000;
        int[] x = new int[]{3, 5, 15};
        int ans = 0;

        ans += 3 * triangular((n - 1) / 3);
        ans += 5 * triangular((n - 1) / 5);
        ans -= 15 * triangular((n - 1) / 15);

        System.out.println(ans);
    }

    // Calculate the nth triangualr number
    private static int triangular(int n){
        return n * (n + 1) / 2;
    }
}
