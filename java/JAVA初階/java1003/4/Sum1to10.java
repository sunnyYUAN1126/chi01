public class Sum1to10 {
    public static void main(String[] args) {
        String op = "1";
        int sum1 = 1;
        for (int i=2; i<=10; i++){
            op += "+"+i;
            sum1 += i;
        }
        System.out.println(op + " = " + sum1);
        var sb = new StringBuilder("1");
        var sum2 = 1;
        for (int j=2; j<=10; j++){
            sb.append("+"+j);
            sum2 += j;
        }
        System.out.println(sb.append(" = ").append(sum1));
    }
 }