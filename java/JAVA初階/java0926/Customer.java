public class Customer {

    public int customerID = 0; // Default ID for the customer
    public String name = "-name required-"; // default
    public String emailAddress = "-email required-"; // default  
	
	public void printt(){
	
	System.out.println("---------------------------------");
	System.out.println("customerID  : "+customerID);
	System.out.println("name        : "+name);
	System.out.println("emailAddress: "+emailAddress);
	System.out.println("---------------------------------");
	}

} // end of class
