public class CustomerTest {
   
	public static void main (String args[]) {
		Customer  c=new Customer ();
		c.setCustomerInfo(1,"王大明","新北市萬華區","02-6354-1236");
		c.display();
		
		Customer  d=new Customer ();
		d.setCustomerInfo(2,"陳小美","台中市龍井區","04-6583-1658","ddd@gmail.com");
		d.display();
	} 
}


class Customer {
	public int customerID =0;
	public String name ="-name required-";
	public String address ="-address required-";
	public String phoneNumber ="-phone required-";
	public String eMail ="-email optional-";
		
	public void setCustomerInfo(int Id, String nm, String addr, String phNum) {
		customerID =Id;
		name =nm;
		address =addr;
		phoneNumber =phNum;
	}
    public void setCustomerInfo(int Id,String nm,String addr, String phNum,String email){
		customerID =Id;
		name =nm;
		address =addr;
		phoneNumber =phNum;
		eMail =email;
	} 
	public void display(){
		System.out.println("----------------------");
		System.out.println("客戶編號: "+customerID);
		System.out.println("客戶姓名: "+name);
		System.out.println("客戶地址: "+address);
		System.out.println("客戶電話: "+phoneNumber);
		if(eMail != "-email optional-")
			System.out.println("客戶電郵: "+eMail);
		
		//三元運算 email
		//String eMail_Result = (eMail== "-email optional-") ? "沒有email" : eMail;
		//System.out.println("客戶電郵: "+eMail_Result);

		System.out.println("----------------------");
	}
}