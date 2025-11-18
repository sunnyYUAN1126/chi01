 // 練習
 public class java01{
	 public static void main(String args[]){
		 final double PI=3.14159;
		 int r1=10,r2=25,r3=50; // 可以這樣一次寫
		 double a=r1*r1*PI;
		 double b=r2*r2*PI;
		 double c=r3*r3*PI;
		 System.out.println("半徑10: "+a);
		 System.out.println("半徑25: "+b);
		 System.out.println("半徑50: "+c);
		 // 浮點數是近似值
	 }
 }
 
 //同型態運算不會出錯
 //不同型態運算會出錯
 //資料轉型
 //小轉大 不會出錯 自動轉型
 //大轉小 會出錯
 
 // 練習
 class java02{
	 public static void main(String args[]){
		 int year=3, month=12, yearDay=365, hour=24, min=60, sec=60, ms=1000;
		 System.out.println(year+" 年等於");
		 System.out.println(year*month+" 個月");
		 System.out.println(year*yearDay+" 天");
		 System.out.println(year*yearDay*hour+" 小時");
		 System.out.println(year*yearDay*hour*min+" 分鐘");
		 System.out.println(year*yearDay*hour*min*sec+" 秒");
		 System.out.println((long)(year*yearDay*hour*min*sec*ms)+" 豪秒鐘");
	 }
 }
 
 class java03{
	 public static void main(String args[]){
		 int a=0,b=0;
		 b=a++ + ++a;
		 System.out.println(a);
		 System.out.println(b);

	
	 }
 }
 
 
 // (int)(n*z) -->n*z運算完後轉int
 // (int)n*z   -->(int)n轉換後*z
 
 // 由左到右
 // 1+2+"a"  -->3a
 // "a"+1+2  -->a12
 
 // 10/0 出錯
 // 10.0/0.0 不會出錯，因為浮點數是近似值
 
 
 //i++ 執行一次後加1
 //++i 先加1一次後執行
 
 //a=0,b=0
 //b=a++ + ++a 答案為2
 // 因為a++、++a算是在執行了
 //a++ 0-->1
 //++a 1+1-->2
 
 class java04{
	 public static void main(String args[]){
		 int c1=0, c2=54, c3=98;
		 double f1=9/5*c1+32;
		 double f2=(double)9/5*c2+32;
		 double f3=9*c3/5+32;
		 System.out.println(f1);
		 System.out.println(f2);
		 System.out.println(f3);
		 
		 System.out.println("差異:");
		 System.out.println("9/5: "+9/5);
		 System.out.println("9.0/5: "+9.0/5);
		 System.out.println("(double)9/5: "+(double)9/5);
		 // 如果要有小數，要加.0 例如9.0。或是傳換成double
		 // 10/3   整數3 
         // 10.0/3 浮點數3.33 
	 }
 }
 
 //「整數除以整數」會是整數
 //「浮點數除以整數會」是浮點數
 
 
 
 
 // 「&」與「捷徑&&」的差異
 // 當左式已經足以判斷整個運算的結果時,右式就不必做了
  class java05{
	 public static void main(String args[]){
		 int a=0,b=0;
		 if((a++>0) & (b++>0)){
			 
		 }
		 System.out.println("(a++>0) & (b++>0)  a: "+a);
		 System.out.println("(a++>0) & (b++>0)  b: "+b);
		 
		 
		 a=0;
		 b=0;
		 if((a++>0) && (b++>0)){
			 
		 }
		 System.out.println("(a++>0) && (b++>0)  a: "+a);
		 System.out.println("(a++>0) && (b++>0)  b: "+b);
	
	 }
 }

  class java06{
	 public static void main(String args[]){

		 System.out.println("======= & =======");
		 System.out.println("true & true   : "+ (true & true));
		 System.out.println("true & false  : "+ (true & false));
		 System.out.println("false & false : "+ (false & false));
		 
		 System.out.println("======= | =======");
		 System.out.println("true | true   : "+ (true | true));
		 System.out.println("true | false  : "+ (true | false));
		 System.out.println("false | false : "+ (false | false));

		 System.out.println("======= ^ =======");
		 System.out.println("true ^ true   : "+ (true ^ true));
		 System.out.println("true ^ false  : "+ (true ^ false));
		 System.out.println("false ^ false : "+ (false ^ false));
		 
	
	 }
 }
 
 //位元邏輯運算
 class java07{
	 public static void main(String args[]){
		 System.out.println(13 & 12);
		 System.out.println(13 | 12);
		 System.out.println(13 ^ 12);
		 System.out.println(~13);
		 // 13-->1101
		 // 12-->1100
		 // & -->1100是12
		 // | -->1101是13
		 // ^ -->0001是1
		 // ~13 -->要加1-->是-14
		 // ~是not的意思
		 System.out.println("--------------------------");
		 
		 System.out.println("253 & 134 : "+ (253 & 134));
		 System.out.println("253 | 134 : "+ (253 | 134));
		 System.out.println("253 ^ 134 : "+ (253 ^ 134));
		 System.out.println(" ~253 : "+(~253));
         System.out.println(" ~134 : "+ (~134));		 
		 
	 }
 }
 
 // 位移運算
 //二元次方曙
  class java08{
	 public static void main(String args[]){
         long i=1L;
		 System.out.println(i<<32); //2的32次方
		 System.out.println(i<<38);
		 System.out.println(i<<49);
		 
		 System.out.println("--------------------------");
		 System.out.println(i<<0); // 1 × 2^0 = 1
		 System.out.println(i<<1);
		 System.out.println(i<<2);
		 System.out.println(i<<3);	 
	 }
 }

 // 三元運算子
 // x=(布林運算式)? "正確" : "錯誤" ;
 class java09{
	 public static void main(String args[]){
		 int a=55;
		 String answer= (a%2==0)?"true Yes~偶數":"false No!奇數";
		 System.out.println(a+" 是 "+answer);
	 }
 }

 
 
 