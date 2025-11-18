package com.example;

import com.example.domain.*;
//com.example.domain資料夾
//Employee檔案/類別

public class EmployeeTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("\n------多型進階--------\n");	
		Employee emp[]=new Employee[5];

		emp[0]=new Employee("Tanna","J123456789",40000.0);
		emp[1]=new Admin("Canna","J123456789",40000.0);
		emp[2]=new Engineer("Danna","J123456789",40000.0);
		emp[3]=new Manager("Panna","J123456789",50000.0,"cat_dept");
		emp[4]=new Director("Lanna","J123456789",60000.0,"cat_dept",10);
		
		for(int i=0;i<emp.length;i++) 
			System.out.println(emp[i]);
		

		System.out.println("-----有人學技能------");
		System.out.println(emp[2] instanceof Engineer);
		if(emp[2] instanceof Engineer) {
			Engineer eng=(Engineer)emp[2]; //宣告一個Engineer型態的eng
			eng.addSkills("java");
			eng.addSkills("c");	
			((Engineer)emp[2]).addSkills("http");
			((Engineer)emp[2]).addSkills("css");
			((Engineer)emp[2]).addSkills("javaScript");
		}
		emp[2].raiseSalary(10000);
		
		System.out.println("-----部門分配-------");
		if(emp[3] instanceof Manager) {
			Manager m=(Manager)emp[3];
			m.addEmployee(emp[0]);
			m.addEmployee(emp[1]);
			m.addEmployee(emp[2]);
		}
		
		((Manager)emp[4]).addEmployee(emp[3]);
//		emp[4].addEmployee(emp[3]);不可以這樣做，因為Employee emp是父。雖然是Director子給他，但是要用Manager子，但是Employee emp是父
		for(int i=0;i<emp.length;i++) 
			System.out.println(emp[i]);
		
		
	}
}
//src主目錄
//咖啡色包裹形狀的是資料夾
//com是公司名稱

