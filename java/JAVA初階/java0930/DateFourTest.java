public class DateaFourTest {
    public static void main(String args[]) {
		DataFour f=new DataFour(2000,2,29);
		System.out.println(  f.getDate()  +"\n");
		
		DataFour f1=new DataFour(2010,20,20);
		System.out.println(  f1.getDate()  +"\n");
		
		DataFour f2=new DataFour();
		System.out.println(  f2.getDate()  +"\n");
	  
  }
}
class DataFour{
	private int year;
	private int month;
	private int day;
	
	public DataFour(){}	
	public DataFour(int y,int m,int d){
		this.setDate(y,m,d);
	}

	public void setDate(int y,int m,int d){
		if (y>=1000 && y<=10000)
			year=y;
		else
			System.out.println("年錯誤: "+y);
		if(m>0 && m<=12)
			month=m;
		else
			System.out.println("月錯誤: "+m);
		if(d>=0 && d<=calcDaysInMonth(y,m))
			day=d;
		else
			System.out.println("日錯誤: "+d);
		
		
// 也可以這樣寫		
//		if (y>=1000 && y<=10000){
//			if(m>0 && m<=12){
//				if(d>=0 && d<=calcDaysInMonth(y,m)){
//					year=y;
//					month=m;
//					day=d;
//				}else{
//					System.out.println("日錯誤");
//				}
//			}else{
//				System.out.println("月錯誤");
//			}	
//		}else{
//			System.out.println("年錯誤");
//		}		
	}

	
	private int calcDaysInMonth(int y, int m){
		int day=0;
		switch (m){
			case 1:
			case 3:
			case 5:
			case 7:
			case 8:
			case 10:
			case 12:
				day=31;
				break;
			case 4:
			case 6:
			case 9:
			case 11:
				day=30;
				break;
			case 2:
				day=((y%4==0 && y%4!=0) || (y%400==0))?29:28;
			
		}
		return day;	
	}
	
	
	public String getDate(){
        if(day==0||month==0||year==0)
            return "日期未設定好!";
        return year+"/"+month+"/"+day;
    }
}