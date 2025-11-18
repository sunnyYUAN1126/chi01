public class MathTools{

	public static double getTriangle(int triangle_1,int triangle_2){
		return Math.sqrt(Math.pow(triangle_1, 2) + Math.pow(triangle_2, 2));
	}
	
	public static double getCelsius(int Fahrenheit){
		return Fahrenheit*(9.0/5)+32;
	}
	
	public static boolean isPrime(int num){
		for(int i=2;i<num;i++){
			if(num%i==0)
				return false;
		}
		return true;
	} 
	public static double getBMI(int we,int cm){
		return Math.round(  we/Math.pow((cm/100.0),2)  );
		// Math.round四捨五入
		
	}
}