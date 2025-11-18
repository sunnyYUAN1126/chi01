public class MathToolsTest{
	public static void main(String args[]){
		// 直接呼叫類別方法，類別不用設定屬性直接把直傳進方法
		System.out.println(MathTools.getTriangle(3,4));
		
		System.out.println(MathTools.getCelsius(32));
		
		System.out.println(MathTools.isPrime(0));
		
		System.out.println(MathTools.getBMI(50,150));
	}
}