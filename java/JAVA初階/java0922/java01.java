// 2025/9/22
public class java01{
	public static void main(String args[]){
		java.util.Scanner sc=new java.util.Scanner(System.in);
		
		System.out.print("輸入a: ");
		int a=sc.nextInt();
		System.out.print("輸入b: ");
		int b=sc.nextInt();
		
		System.out.println("a+b= "+(a+b));
	}
}

class java02{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in,"cp950");
		System.out.print("輸入名子: ");
		String name=sc.nextLine();
		System.out.println("Hello! "+name);
	}
}

// 中文輸入"cp950" 是scanner api 
// cd ..\JAVA入門\1.WorkSpace
 

// 也可以這樣寫
class java03{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		System.out.print("請輸入消費金額: ");
		int a=sc.nextInt();
		int payment=0;
		// 先判斷金額
		if(a>=5000)
			payment=(int)(a*0.7);
		else if(a>=3000)
			payment=(int)(a*0.8);
		else if(a>=2000)
			payment=(int)(a*0.85);
		else if(a<0)
			payment=(int)(a*0.9);
		else
			System.out.println("請輸入正確金額");
		
		//一次統一輸出
		if (payment>0)
			System.out.println("折扣後為"+payment);
			
	}
}

// 也可以這樣寫: 直接設定區間
class java04{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		
		System.out.print("請輸入成績(判斷是否要補考): ");
		int score=sc.nextInt();
		
		if(score<=60 && score>=40)
			System.out.println("是");
		else
			System.out.println("否");

	}
}

// 巢狀 if-else
class java05{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		
		int num=sc.nextInt();
		if(num%2==0 || num%3==0){
			if(num%2==0 && num%3==0){
				System.out.println("是2與3的倍數");
			}
			else{
				if(num%3==0)
					System.out.println("是3的倍數");
				else
					System.out.println("是2的倍數");		
			}
		}			
		else{
			System.out.println("不是2與3的倍數");
		}
	}
}



class java06{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		
		System.out.print("請輸入要查詢的星期\n( 輸入值為 Mon/Tue/Wed/Thu/Fri/Sat/Sun )\n輸入: ");
		String week=sc.next();
		String weekClass;
		
		switch (week){
			case "Mon":
				weekClass="鋼琴課";
				break;
			case "Tue":
				weekClass="圍棋課";
				break;
			case "Wed":
				weekClass="英文課";
				break;
			case "Thu":
				weekClass="桌球課";
				break;
			case "Fri":
				weekClass="跆拳道";
				break;
			case "Sat":
				weekClass="電腦課";
				break;
			case "Sun":
				weekClass="作文課";
				break;	
			default:
				weekClass="輸入星期錯誤";
		}
		System.out.println(weekClass);
	}
}


class java07{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		System.out.print("請輸入字元(R/L/U/D): ");
		String a=sc.next();
		switch (a){
			case "r":
			case "R":
				System.out.println("向右走");
				break;
			case "l":
			case "L":
				System.out.println("向左走");
				break;
			case "u":
			case "U":
				System.out.println("向上走");
				break;
			case "d":
			case "D":
				System.out.println("向下走");
				break;
			default:
				System.out.println("無法辨識方向");
		}
		
	}
}



class java08{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		System.out.print("請輸入月份: ");
		int mon=sc.nextInt();
		switch (mon){
			case 1:
			case 3:
			case 5:
			case 7:
			case 8:
			case 10:
			case 12:
				System.out.println(mon+"月為31天");
				break;
			
			case 4:
			case 6:
			case 9:
			case 11:
				System.out.println(mon+"月為30天");
				break;
			
			case 2:
				
				System.out.println("輸入年份: ");
				int year=sc.nextInt();
				if((year%4==0 && year%100!=0) || (year%400==0))
					System.out.println(year+"年是潤年，"+mon+"月有29天");
				else
					System.out.println(year+"年是平年，"+mon+"月有28天");
				break;
			
			default:
				System.out.println("輸入錯誤");
		}
		
	}
}

// 1+...+n=總和
class java09{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		System.out.print("輸入最大值: ");
		int num=sc.nextInt();
		int sum=0;
		for (int i=1;i<=num;i++){
			sum=sum+i;
		}
		System.out.println("1+...+"+num+" = "+sum);
	}
}
// 費伯那西數列
class java010{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		System.out.print("輸入: ");
		int num=sc.nextInt();
		int count1=1;
		int count2=1;
		int temp=0;
		while(temp<=num){			
			count1=count2;
			count2=temp;
			temp=count1+count2; //count1+count2(count1)=temp(count2)	
			System.out.print(temp+"  ");	
		}
	}
}
// 1+0=1
// 0+1=1
// 1+1=2
// 2+1=3
// ....


// 九九乘法表
class java011{
	public static void main(String args[]){
		for(int i=1;i<10;i++){
			for(int j=1;j<10;j++){
				System.out.print(i+"*"+j+"="+(i*j)+"\t");
			}
			System.out.println();
		}	
	}
}

// 聖誕樹
class java012{
	public static void main(String args[]){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		System.out.print("輸入三角形層數: ");
		int level=sc.nextInt();
		
		for(int i=1;i<=level;i++){		
			for(int j=0;j<level-i;j++){				
				System.out.print(" ");
			}
			char c=(char)(64+i); // 強制轉型成字元
			for(int k=0;k<(2*i-1);k++){				
				System.out.print(c);
			}
			System.out.println();	
		}
			
	}
}




