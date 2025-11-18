package com.example;

import com.example.domain.Admin;
import com.example.domain.Director;
import com.example.domain.Employee;
import com.example.domain.Engineer;
import com.example.domain.Manager;

import com.example.domain.RegularStaff;

public class EmployeeTest {

	public static void main(String[] args) {
		Employee[] emps = new Employee[5];
	

		emps[0] = new Admin("Dav", "P913652874", 50000);
		emps[1] = new Admin("Amy", "B210987654", 50000);
		emps[2] = new Engineer("David", "C109876543", 60000);
		emps[3] = new Manager("Louis", "D124680135", 60000, "TW Sales");
		emps[4]= new Director("Nicole", "R202468135", 60000, "Global Sales", 1000000);

		for(int i=0; i<emps.length; i++)
			System.out.println(emps[i]);
		
		System.out.println("David 學會了Java, Android");
		if(emps[2] instanceof Engineer) {
			Engineer eng = (Engineer )emps[2];
			eng.addSkill("Java");
			eng.addSkill("Android");
		}
		
		System.out.println("部門分配.....");
		if(emps[3] instanceof Manager) {
			Manager m1 = (Manager)emps[3];
			m1.addEmployee(emps[0]);
			m1.addEmployee(emps[1]);
			m1.addEmployee(emps[2]);
		}
		
		((Manager)emps[4]).addEmployee(emps[3]);
		
		System.out.println("設定工作時數....\n");
		((Admin)emps[0]).setHours(150);
		((Admin)emps[1]).setHours(180);
		
		
		for(int i=0; i<emps.length; i++)
			System.out.println(emps[i]);
		
		System.out.println("===本月薪資&尾牙活動====");
		for(int i=0; i<emps.length; i++) {
			System.out.println(emps[i].getName()+": "+emps[i].getPay());



			if(emps[i] instanceof RegularStaff) {
				System.out.println("尾牙抽獎 :"+RegularStaff.getLuckDraw() );
				System.out.println("年終獎金 :"+((RegularStaff)emps[i]).getBonus()+"\n");				
			}else
				System.out.println("派遣沒有福利\n");			
		}
			
		
	}
}
