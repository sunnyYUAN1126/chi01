// https://www.oracle.com/java/technologies/downloads/?er=221886#jdk21-windows
// https://docs.oracle.com/javase/8/docs/api/ 
 
 // (public)公開的類別檔案名稱與類別名稱相同
 // main 主方法  字串陣列String args[]
 // 縮排
 // print印出+ln換行
 public class java01{
	 public static void main(String args[]){
		 System.out.println("hellow word!");
		 
		 System.out.println(args[0]+"你好");
	 }
 }
 
 // CMD指令
 // D: 切換D槽
 // cd+資料夾名稱  改變目錄
 // cd JAVA
 // dir 列出目錄
 // cls清除畫面
 // 編譯 javac java01.java 生出.class檔案
 // 執行 java java01  (執行.class檔案)
 
 // javac java01.java
 // java java01
 
 
// 練習1 
class java02{
	 public static void main(String args[]){
		 int a=2147483647;
		 int b=a+1;
		 System.out.println("a="+a);
		 System.out.println("b="+b);
		 
		 long b1=a+1;
		 long b2=(long)a+1;
		 System.out.println("int預設、沒轉換:"+b1);
		 System.out.println("有轉換"+b2);
	 }
 }
 
 
 
// 等於= 「指定」運算子
//0是正數
// byte 範圍-128 ~ 127 ，負數有128，正數有128(0是正數，因此範圍0~127有128個)。
// 資料是有範圍的
// 溢位
// 浮點數是近似值



//練習2
 class java03{
	 public static void main(String args[]){
		 long a= 23000000L;
		 long all=a*9876;	 
		 System.out.println("所有的所得稅額為 "+all+" 元。");
	 }
 }
 
 
 
 