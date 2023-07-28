public class tower_of_hanoi {
    public static void tower_of_hanois(int n, char source, char destination, char helper) {
        if (n == 1) {
            System.out.println("Move disk 1 from tower " + source + " to tower " + destination);
            return;
        }

        tower_of_hanois(n - 1, source, helper, destination);
        System.out.println("Move disk " + n + " from tower " + source + " to tower " + destination);
        tower_of_hanois(n - 1, helper, destination, source);
    }

    public static void main(String[] args) {
        int n = 3;
        tower_of_hanois(n, 'A', 'C', 'B');
    }

}