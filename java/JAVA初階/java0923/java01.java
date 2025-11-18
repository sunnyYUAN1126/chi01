// 2025/9/23


public class java01{
	public static void main(String args[]){
		java.util.Scanner sc=new java.util.Scanner(System.in);

		
	}
}
//質數 迴圈 解答
class PrimeNumber {
	public static void main(String[] args){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		System.out.print("輸入質數:");
		int num = sc.nextInt();
		boolean isPrime = true;
		for(int i=2; i<num; i++){
			if(num%i==0){
				isPrime = false;
				break;
			}
		}
		System.out.println(num+(isPrime?"質數":"非質數"));
	}
}


class PrimeNum2{
	public static void main(String[] args){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		System.out.print("輸入整數:");
		int num=sc.nextInt();
		
		checkPrime:{
			for(int i=2; i<num; i++){
				if(num%i==0){	
					System.out.println(num+"不是質數");
					break checkPrime;
				}
			}			
		System.out.println(num+"是質數");
		}
	}
}

//練習
class java02{
	public static void main(String args[]){
		java.util.Scanner sc=new java.util.Scanner(System.in,"cp950");
		

		
		while(true){
			System.out.print("輸入學號: ");
			String name=sc.next();

			System.out.print("輸入筆試成績: ");
			int a=sc.nextInt();
			
			if(a>70){
				System.out.print("輸入路考成績: ");
				int b=sc.nextInt();
				if(b>70){
					System.out.println(name+"恭喜取得駕照");
					break;
				}
				else{
					System.out.println(name+"路考要重考");
					continue;		
				}
			}
			else{
				System.out.println(name+"不能路考");
				continue;
			}
		}				
	}
}
// 解答
class DriverLicense{
	public static void main(String[] args){	
		java.util.Scanner sc = new java.util.Scanner(System.in);		
		while(true){				
			System.out.print("學號(輸入-1離開):");
			int id = sc.nextInt();
			if(id==-1)
				break;	
			System.out.print("輸入筆試成績:");
			int exam1 = sc.nextInt();
			if(exam1<85)
				continue;
			System.out.print("輸入考場成績:");
			int exam2 = sc.nextInt();
			if(exam2<70)
				continue;
			System.out.print("輸入路考成績:");
			int exam3 = sc.nextInt();
			if(exam3<70)
				continue;
			System.out.println(id+"號取得駕照");
		}
	}	
}