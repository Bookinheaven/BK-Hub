class Time{
	private int hours;
	private int minutes;
	private int seconds;
	Time(){
		this.hours = 0;
		this.minutes = 0;
		this.seconds = 0;
	}
	Time(int hr, int min, int sec){
		this.hours = hr;
		this.minutes = min;
		this.seconds = sec;
	}
	public void display(){
		System.out.printf("%02d:%02d:%02d\n", this.hours, this.minutes, this.seconds);
	}
	public void add(Time time1,Time time2) {
		int totalsec = time1.seconds + time2.seconds + this.seconds;
		if (totalsec > 60) {
			this.minutes++;			
		}
		this.seconds = totalsec % 60;
		int totalmin =time1.minutes + time2.minutes + this.minutes;
		if (totalmin > 60) {
			this.hours++;			
		}
		this.minutes = totalmin % 60;
		this.hours = (time1.hours + time2.hours + this.hours ) % 12;
	}
}

public class F1 {
    public static void main(String[] args) {
    	Time time1 = new Time(11, 60, 59);
    	Time time2 = new Time(4, 60, 40);
    	Time time3 = new Time();
    	time1.display();
    	time2.display();
    	time3.add(time1, time2);
    	time3.display();
    }
}
