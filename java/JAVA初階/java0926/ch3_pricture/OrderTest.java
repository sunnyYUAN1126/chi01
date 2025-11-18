
public class OrderTest{
	public static void main(String args[]){
		Order o1=new Order();
		Shirt s1=new Shirt();		
		s1.shirtID=1;
		s1.description="11111";
		s1.colorCode='A';
		s1.price=14.99;
		s1.quantityInStock=1;
		o1.addShirt(s1);

		

		Shirt s2=new Shirt();
		s2.shirtID=2;
		s2.description="22222";
		s2.colorCode='C';
		s2.price=23.55;
		s2.quantityInStock=10;	
		o1.addShirt(s2);

		
		

		Shirt s3=new Shirt();
		s3.shirtID=3;
		s3.description="3333";
		s3.colorCode='B';
		s3.price=49.99;
		s3.quantityInStock=6;	
		o1.addShirt(s3);

		
		o1. displayOrderInfo();
		
		
		
		
		


		
		
	}
}
