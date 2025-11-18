public class CustomerTest {
	public static void main(String arg[]){ //這個main主方法是區域變數
		Customer cust1=new Customer();
		cust1.customerID=1;
		cust1.name="Petter";
		cust1.emailAddress="ppp@gmail.com";
		cust1.printt();
		
		Customer cust2=new Customer();
		cust2.customerID=2;
		cust2.name="Ammy";
		cust2.emailAddress="aaa@gmail.com";	
		cust2.printt();
		
		cust2=cust1;
		System.out.println("--------- cust2 = cust1 ---------");
		cust1.printt();
		cust2.printt();
		
		
		
	
	}

} // end of class
