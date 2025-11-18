package com.example;

import com.example.domain.*;
//com.example.domain資料夾
//Employee檔案/類別

public class EmployeeTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//----------------------------------------------------------------------
//		System.out.println("-----建立多個員工-----\n");
//		Employee a=new Employee("Anne","J123456789",40000.0);
//		a.displayInformation();
//		
//		Employee p=new Employee("Sunny","D963258741",45000.0);
//		p.displayInformation();

//----------------------------------------------------------------------	
//		System.out.println("\n---繼承練習 & Super練習 & 多型--------\n");	
//		System.out.println("\n---有員工學技能，加薪水~---");
//		Engineer em3=new Engineer("Tanna","J123456789",48000.0);
//		em3.addSkills("java");
//		em3.addSkills("c");
//		em3.raiseSalary(10000);
//		em3.displayInformation();
//		System.out.println("---------------");
//		System.out.println("其他員工:");
//		
//		
//		Employee em5=new Admin("Canna","J123456789",48000.0);
//		em5.displayInformation();
//		
//		Employee em4=new Manager("Panna","J123456789",50000.0,"cat_dept");
//		em4.displayInformation();
//		
//		Employee em6=new Director("Lanna","J123456789",50000.0,"cat_dept",10);
//		em6.displayInformation();
//----------------------------------------------------------------------			
		System.out.println("\n------多型進階--------\n");	
		Employee emp[]=new Employee[5];

		emp[0]=new Employee("Tanna","J123456789",48000.0);
		emp[1]=new Admin("Canna","J123456789",48000.0);
		emp[2]=new Engineer("Danna","J123456789",48000.0);
		emp[3]=new Manager("Panna","J123456789",50000.0,"cat_dept");
		emp[4]=new Director("Lanna","J123456789",50000.0,"cat_dept",10);
		
		

		
		if(emp[2] instanceof Engineer) {
			Engineer eng=(Engineer)emp[2];
			eng.addSkills("java");
			eng.addSkills("c");			
		}
		
		System.out.println("部門分配");
		if(emp[3] instanceof Manager) {
			Manager m=(Manager)emp[3];
			m.addEmployee(emp[0]);
			m.addEmployee(emp[1]);
			m.addEmployee(emp[2]);
		}
		
		((Manager)emp[4]).addEmployee(emp[3]);
		for(int i=0;i<emp.length;i++) {
			emp[i].displayInformation();
		}
		
	}
}
//src主目錄
//咖啡色包裹形狀的是資料夾
//com是公司名稱

