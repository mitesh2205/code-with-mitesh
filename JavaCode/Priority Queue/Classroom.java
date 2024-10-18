
package JavaCode.Priority%20Queue;

import java.util.PriorityQueue;


    
    static class Student implements Comparable<Student> {
        String name;
    int rank;

    public Student(String name, int rank){
        this.name = name;
        this.rank = rank;
    }

    @Override
    public int compareTo(Student o) {
        return  o.rank - this.rank;
    }
    }
    public class Classroom {
    public static void main(String[] args) {
        PriorityQueue<Student> pq = new PriorityQueue<>();
        pq.add(new Student("A", 1));
        pq.add(new Student("B", 2));
        pq.add(new Student("C", 3));
        pq.add(new Student("D", 4));
        pq.add(new Student("E", 5));
        pq.add(new Student("F", 6));
        pq.add(new Student("G", 7));
        pq.add(new Student("H", 8));
        pq.add(new Student("I", 9));
        pq.add(new Student("J", 10));
        pq.add(new Student("K", 11));
        pq.add(new Student("L", 12));
        pq.add(new Student("M", 13));
        pq.add(new Student("N", 14));
        pq.add(new Student("O", 15));
        pq.add(new Student("P", 16));
        pq.add(new Student("Q", 17));
        pq.add(new Student("R", 18));
        pq.add(new Student("S", 19));
        pq.add(new Student("T", 20));
        pq.add(new Student("U", 21));
        pq.add(new Student("V", 22));
        pq.add(new Student("W", 23));
        pq.add(new Student("X", 24));
        pq.add(new Student("Y", 25));
        pq.add(new Student("Z", 26));

        while (!pq.isEmpty()){
            System.out.println(pq.poll().name);
        }
    }
}
