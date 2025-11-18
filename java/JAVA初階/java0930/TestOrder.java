public class TestOrder {
	public static void main(String[ ] args) {
	Order myOrder = new Order( );
	Shirt myShirt = new Shirt();
	
	System.out.println("------myOrder------");	
	System.out.println("orderID     : "+myOrder.orderID);
	System.out.println("shirts[0]   : "+myOrder.shirts[0]);
	System.out.println("itemNo      : "+myOrder.itemNo);
	System.out.println("totalPrice  : "+myOrder.totalPrice);
	System.out.println();
	System.out.println("-------myShirt-----");
	System.out.println("shirtID     : "+myShirt.shirtID);
	System.out.println("colorCode   : "+myShirt.colorCode);
	System.out.println("price       : "+myShirt.price+"\n");
	
	System.out.println("------測試-----");
	myOrder.addShirt(myShirt);
	System.out.println("totalPrice  :"+myOrder.totalPrice);
	System.out.println("price       :"+myShirt.price+"\n");
	}
}
 
class Order {
	public int orderID = 1001;
	public Shirt[ ] shirts = new Shirt[5];
	public int itemNo = 0;
	public double totalPrice = 0.0;
	
	// 測試
	public void addShirt(Shirt s) {
		//這是新的物件s
		//s=new Shirt();
		//s.price=100;
		
		//這是Shirt s傳進來的，也就是s是myShirt
		s.price=200;
		
		shirts[itemNo++] = s;
		totalPrice += s.price;
		
		System.out.println("測試");
		System.out.println("shirtID     : "+s.shirtID);
		System.out.println("colorCode   : "+s.colorCode);
		System.out.println("price       : "+s.price+"\n");
		
	
		
		
	}
}
 
 
class Shirt {
	public int shirtID = 101;
	public char colorCode = 'R';
	public double price = 299.0;  
}