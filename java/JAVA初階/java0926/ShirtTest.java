public class ShirtTest{
	public static void main(String args[]){
		Shirt a=new Shirt();
		a.shirtID=1;
		a.colorCode='R';
		a.description="meow meow";
		//a.price=1000;
		//a.qu=5;
		
		System.out.println("-----------------------");
		System.out.println("ID          : "+a.shirtID);
		System.out.println("color       : "+a.colorCode);
		System.out.println("description : "+a.description);
		System.out.println("price       :"+a.price);
		System.out.println("qu          : "+a.qu);
		System.out.println(a);
		
		
		Shirt b=new Shirt();
		b.shirtID=2;
		b.colorCode='y';
		b.description="dog";
		b.price=1;
		b.qu=1;
		System.out.println("-----------------------");
		System.out.println("ID          : "+b.shirtID);
		System.out.println("color       : "+b.colorCode);
		System.out.println("description : "+b.description);
		System.out.println("price       : "+b.price);
		System.out.println("qu          : "+b.qu);
		System.out.println(b);
		




	}
}