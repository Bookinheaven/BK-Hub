public class _2_Threading {
    private static void mainThreadCheck(){
        Thread mainThread = Thread.currentThread();
        mainThread.setName("This is Main");
        mainThread.setPriority(2);
        ThreadGroup tg = mainThread.getThreadGroup();
        String name = mainThread.getName();
        int priority = mainThread.getPriority();
        System.out.printf("Name: %s\nThreadGroup : %s\nPriority : %d\n",name, tg.getName(), priority);
        try {
            mainThread.sleep(1000);
        } catch (InterruptedException e){
            System.out.println("Interrupted Exception" + e);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
    public static void main(String[] args) {
        mainThreadCheck();
        Thread t1 = new T1();
        t1.start();
        System.out.println(t1.isAlive());
        try {
            t1.join();            
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        // Thread t2 = new Thread(new R1());
        // t2.start();
        R1 x = new R1();
    }
}
class R1 implements Runnable {
    Thread l;
    R1(){
        Thread l = new Thread(this);
        l.start();
    }
    @Override
    public void run() {
        System.out.println("Runnable");
    }
}
class T1 extends Thread {
    @Override
    public void run() {
        System.out.println("Child started");
        for(int i=1;i<=5;i++) {
            System.out.println("Child:"+i);
            try {
            Thread.sleep(2000);
            } catch (InterruptedException e) {
            e.printStackTrace();
            }
        }
        System.out.println("Child completed");
    }    
}
