public class _16_Enum {
        public enum day {
            MONDAY(10),
            TUESDAY,
            WEEKEND;
            day(int value) {
                System.out.println(value);
            }
            day() {
            }
            public String dayofWeekend = "SUNDAY";
        } 
    public static void main(String[] args) {
        System.out.println(day.valueOf("MONDAY").ordinal());
        System.out.println(day.WEEKEND.dayofWeekend);
    }    
}
