public class Person{
	private StringBuilder name;
	private StringBuilder phoneNumber;
	
	public Person(String name,String phoneNumber){
		this.name=new StringBuilder(name);
		this.phoneNumber=new StringBuilder(phoneNumber);
	}
	
	public void addLastName(String lastname){
		name.append(" ");
		name.append(lastname);
		
		//01-3456789
		//01-3456-89
		phoneNumber.insert(2, "-");
		phoneNumber.insert(7, "-");
	}
	
	public void displayInfo(){
		int lastnamePOS=name.indexOf(" ");
		
		System.out.println("姓      : "+name.substring(lastnamePOS+1));
		System.out.println("名      : "+name.substring(0,lastnamePOS));
		System.out.println("姓名    : "+name.toString());
		System.out.println("姓名長度: "+name.length());
		System.out.println("姓名容量: "+name.capacity());
		System.out.println("電話    : "+phoneNumber.toString());
		System.out.println("電話長度: "+phoneNumber.length());
		System.out.println("電話容量: "+phoneNumber.capacity());
		
	}

	
	public static void main(String args[]){
		Person a=new Person("sunny","0245632145");
		a.addLastName("Gonzalezz");
		a.displayInfo();
		
	}
	
}