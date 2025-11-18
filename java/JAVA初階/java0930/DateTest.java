public class DateTest {
  public static void main(String args[]) {
	  
// DateOne
	  DateOne d1_1= new DateOne();
	  d1_1.year=2025;
	  d1_1.month=9;
	  d1_1.day=30;
	  System.out.println("------------ 公開 ---------");
	  System.out.println("預設建構子: ");
	  System.out.println("自訂屬性: "+d1_1.year+" / "+d1_1.month+" / "+d1_1.day);
	  
	  DateOne d1_2= new DateOne();
	  System.out.println("預設屬性: "+d1_2.year+" / "+d1_2.month+" / "+d1_2.day+"\n\n");
	  
	  // 公開 建構子 直接存取
	  System.out.println("有建構子&無參數建構子: ");
	  DateOneConstructor d1_3= new DateOneConstructor(2015,10,10);
	  System.out.println("自訂屬性: "+d1_3.year+" / "+d1_3.month+" / "+d1_3.day);
	  DateOneConstructor d1_4= new DateOneConstructor();
	  System.out.println("預設屬性: "+d1_4.year+" / "+d1_4.month+" / "+d1_4.day+"\n\n");


	

// DateTwo 會出現錯誤
	  //DateTwo d2_1= new DateTwo();
	  //d2_1.year=2025;
	  //d2_1.month=9;
	  //d2_1.day=30;
	  //System.out.println(d2_1.year+" / "+d2_1.month+" / "+d2_1.day);
	  
    
// DateThree
    System.out.println("----------- 封裝 private ----------");
	DateThree d3_1= new DateThree();
	d3_1.setYear(2020);
	d3_1.setMonthDay(5,20);
	System.out.println("自訂屬性: "+d3_1.getYear()+" / "+d3_1.getMonth()+" / "+d3_1.getDay()+"\n");
    
	
	System.out.println("錯誤判斷: ");
	DateThree d3_2= new DateThree();
	d3_2.setYear(1900);
	d3_2.setMonthDay(-40,100);
	System.out.println("預設屬性: "+d3_2.getYear()+" / "+d3_2.getMonth()+" / "+d3_2.getDay());
	
	//私有 建構子 建構子&方法存取
	DateThreeConstructor d3_3=new DateThreeConstructor(2015,1,1);
	
	System.out.println("建構子 類別外: "+d3_3.getYear()+" / "+d3_3.getMonth()+" / "+d3_3.getDay());
	d3_3.a();
  }// end main

} // end class


// DateOne-----------------------------
class DateOne{
	public int year=2000;
	public int month=1;
	public int day=1;
}
//  DateOneConstructor----------------------------
class DateOneConstructor{
	public int year=2000;
	public int month=1;
	public int day=1;
	
	public DateOneConstructor(int y,int m,int d){
		year=y;
		month=m;
		day=d;
	}
	public DateOneConstructor(){ }
	
}

class DateTwo{
	private int year=2000;
	private int month=1;
	private int day=1;
}


// DateThree-----------------------------------------------------------
class DateThree{
	private int year=2000;
	private int month=1;
	private int day=1;
	
// 值傳進去
// 設定私有的屬性，用公開的方法取值	
	public void setYear(int year){
		if (year>=2000)			
			this.year=year;
		else
			System.out.println("設定失敗!年度錯誤");
			
	}	
	public int getYear(){
		return year;
	}
	
	public void setMonthDay(int month,int day){
		if (month>0 && month<=12)
			this.month=month;
		else
			System.out.println("設定失敗!月份錯誤");
		
		if(day>0 && day<=31)
			this.day=day;
		else
			System.out.println("設定失敗!日期錯誤");
		
	}	
	public int getMonth(){
		return month;
	}
	
	

	public int getDay(){
		return day;
	}

}
// DateThreeConstructor------------------------------------------
class DateThreeConstructor{
	private int year=2000;
	private int month=1;
	private int day=1;
	
	public DateThreeConstructor(int y,int m,int d){
		year=y;
		month=m;
		day=d;
	}
		
	public int getYear(){
		return year;
	}
	
	public int getMonth(){
		return month;
	}

	public int getDay(){
		return day;
	}
	
	public void a(){
		System.out.println("類別內: "+year);
	}

}