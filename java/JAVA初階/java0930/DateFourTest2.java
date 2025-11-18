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
		setDate(y,m,d);
	}


//也可以用回傳布林值
//注意!! return 後就直接離開方法，不會執行下面接續的程式碼
	public boolean setDate(int y,int m,int d){
		if (y<1000 || y>10000){
			System.out.println("年錯誤");
			return false;
		}

		if(m<1 || m>12){
			System.out.println("月錯誤");
			return false;
		}

		if(d<1 && d>calcDaysInMonth(y,m)){
			System.out.println("日錯誤");
			return false;
		}
		
		this.year=y;
		this.month=m;
		this.day=d;
		
		return true;	
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