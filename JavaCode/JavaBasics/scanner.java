package JavaCode.JavaBasics;

import java.util.Scanner;

public class scanner {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String name = sc.nextLine();
            System.out.println(name);

            int number = sc.nextInt();
            System.out.println(number);

            float price = sc.nextFloat();
            System.out.println(price);
        }
    }

}
