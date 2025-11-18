public class TestStringBuffer {
    public static void main(String[] args) {
        StringBuffer sb1 = new StringBuffer("Hi");
        sb1.append(" Java!");
        System.out.println(sb1.toString( ));

        System.out.println(sb1);

        StringBuffer sb3 = new StringBuffer("Hi Java!");
        System.out.println(sb1.equals(sb3));
        System.out.println(sb1.toString().equals(sb3.toString()));
// ------------------------------------------------------------
 
        System.out.println("--------------------------");

        StringBuffer aa1 = new StringBuffer("Hi");
        aa1.insert(2," Java!");
        System.out.println(aa1.toString( ));

        StringBuffer aa3 = new StringBuffer("Hi Java!");
         System.out.println(aa3);
        System.out.println(aa1.equals(aa3));
        System.out.println(aa1.toString().equals(aa3.toString()));

    }
 }