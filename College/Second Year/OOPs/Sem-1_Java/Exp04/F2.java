class Distance{
	private int feets;
	private int inches;
	Distance(){
		this.feets = 0;
		this.inches = 0;

	}
	Distance(int ft, int inc){
		this.feets = ft;
		this.inches = inc;
	}
	public void display(){
		System.out.printf("%d Feets %d Inches\n", this.feets, this.inches);
	}
	public int[] add(Distance distance1,Distance distance2) {
		int total = distance1.inches + distance2.inches + this.inches;
		if (total / 12 > 0) {
			this.feets+= total / 12;			
		}
			this.feets = distance1.feets + distance2.feets + this.feets;
		return new int[]{this.feets, this.inches};
	}
}
public class F2 {
    public static void main(String[] args) {
		System.out.println("Tanvik Sri Ram .R => URK23CS1261");
    	Distance distance1 = new Distance(11, 60);
    	distance1.display();
    	Distance distance2 = new Distance(4, 60);
    	distance2.display();
    	Distance distance3 = new Distance();
    	int[] out= distance3.add(distance1, distance2);
    	System.out.printf("Resultant : %d Feets %d Inches", out[0], out[1]);
    }    
}
