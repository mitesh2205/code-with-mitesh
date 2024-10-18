import java.util.PriorityQueue;

public class HospitalQueue {
    public static void main(String[] args) {
        PriorityQueue<Patient> pq = new PriorityQueue<>();
        pq.add(new Patient("Adsf", 3, "Critical"));
        pq.add(new Patient("Bob", 5, "Moderate"));
        pq.add(new Patient("Cathy", 1, "Critical"));
        pq.add(new Patient("David", 7, "Low"));
        pq.add(new Patient("Eva", 2, "Moderate"));

        System.out.println("Patients in the queue as per severity: ");
        while (!pq.isEmpty()) {
            Patient nextPatient = pq.poll();
            System.out.println("Name: " + nextPatient.getName() + " Severity: " + nextPatient.getSeverity());
        }
    }
}

class Patient implements Comparable<Patient> {
    String name;
    int rank;
    String severity;

    public Patient(String name, int rank, String severity) {
        this.name = name;
        this.rank = rank;
        this.severity = severity;
    }

    @Override
    public int compareTo(Patient o) {
        return this.rank - o.rank;
    }

    public String getName() {
        return this.name;
    }

    public int getRank() {
        return this.rank;
    }

    public String getSeverity() {
        return this.severity;
    }
}
