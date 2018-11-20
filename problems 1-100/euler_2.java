public class euler_2 {

    public static void main(String[] args) {
        int[] fib = new int[]{1, 2};
        int i = 0;
        int ans = 2;
        int max = 4000000;

        while (fib[0] < max && fib[1] < max){
            fib[i] = fib[0] + fib[1];
            if (fib[i] % 2 == 0){
                ans += fib[i];
            }
            i ^= 1;
            System.out.println(i);
        }

        System.out.println(ans);
    }
}
