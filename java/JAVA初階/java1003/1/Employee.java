public class Employee{
	

	// 類別屬性
	private static int counter=100;
	private static String companyName="Oracle";
	private static String phoneNumber="123-456-789";
	private static String officeAddres="台北市南港區";
	// 實體屬性
	private String name;
	private int emID;
	
	
	// 建構子&實體屬性
	public Employee(String name){
		this.name=name;
		emID=++counter;
	}
	
	// 修改類別屬性
	public static void setCompanyName(String companyName){	
		Employee.companyName=companyName;
	}
	public static void setPhoneNumber(String phoneNumber){	
		Employee.phoneNumber=phoneNumber;
	}
	public static void setOfficeAddres(String officeAddres){	
		Employee.officeAddres=officeAddres;
	}
	public void display(){
		System.out.println("-------------------");
		System.out.println("公司    : "+companyName);
		System.out.println("公司電話: "+phoneNumber);
		System.out.println("公司地址: "+officeAddres);

		System.out.println("員工編號: "+emID);
		System.out.println("員工姓名: "+name);
		

	}
	
}