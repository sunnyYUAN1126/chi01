public class EmployeeTest{
	public static void main(String args[]){
		Employee a=new Employee("王小美");
		Employee b=new Employee("黃大銘");
		a.display();
		b.display();

		// 公司被別人併購
		System.out.println("--------------------------");
		System.out.println("\n公司被併購後....");
		a.setCompanyName("Apple");
		b.setPhoneNumber("02-9876-5432");
		Employee.setOfficeAddres("新北市板橋區");
		a.display();
		b.display();

		// 測試

	}
}