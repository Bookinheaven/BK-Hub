class Airport {
    private int availableRunways;
    public Airport(int numRunways) {
        this.availableRunways = numRunways;
    }
    public synchronized void requestRunwayForTakeoff(String airplane) throws InterruptedException {
        System.out.println(airplane + " is requesting permission for takeoff.");
        while (availableRunways == 0) {
            System.out.println(airplane + " is waiting for a runway to be available for takeoff.");
            wait();
        }
        availableRunways--; 
        System.out.println(airplane + " is taking off. Runways available: " + availableRunways);
        Thread.sleep(2000);
        System.out.println(airplane + " has taken off.");
        releaseRunway();
    }
    public synchronized void requestRunwayForLanding(String airplane) throws InterruptedException {
        System.out.println(airplane + " is requesting permission for landing.");
        while (availableRunways == 0) {
            System.out.println(airplane + " is waiting for a runway to be available for landing.");
            wait();
        }
        availableRunways--;  
        System.out.println(airplane + " is landing. Runways available: " + availableRunways);
        Thread.sleep(2000);
        System.out.println(airplane + " has landed.");
        releaseRunway();
    }
    private synchronized void releaseRunway() {
        availableRunways++;
        System.out.println("Runway released. Runways available: " + availableRunways);
        notifyAll();
    }
}

class Airplane extends Thread {
    private final Airport airport;
    private final String airplaneName;
    private final boolean isTakeoff;

    public Airplane(Airport airport, String airplaneName, boolean isTakeoff) {
        this.airport = airport;
        this.airplaneName = airplaneName;
        this.isTakeoff = isTakeoff;
    }
    @Override
    public void run() {
        try {
            if (isTakeoff) {
                airport.requestRunwayForTakeoff(airplaneName);
            } else {
                airport.requestRunwayForLanding(airplaneName);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
public class _5_AirportSimulation {
    public static void main(String[] args) {
        System.out.println("Tanvik URK23CS1261");
        Airport airport = new Airport(2); 
        Airplane airplane1 = new Airplane(airport, "Airplane 1", true);
        Airplane airplane2 = new Airplane(airport, "Airplane 2", false);
        Airplane airplane3 = new Airplane(airport, "Airplane 3", true);
        Airplane airplane4 = new Airplane(airport, "Airplane 4", false);
        airplane1.start();
        airplane2.start();
        airplane3.start();
        airplane4.start();
    }
}
