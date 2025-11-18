package com.example;

import com.example.domain.*;
//com.example.domain資料夾
//Employee檔案/類別

public class EmployeeTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//----------------------------------------------------------------------
		System.out.println("-----建立多個員工-----\n");
		Employee a=new Employee("Anne","J123456789",40000.0);
		a.displayInformation();
		
		Employee p=new Employee("Sunny","D963258741",45000.0);
		p.displayInformation();
		
		System.out.println("\n-----修改員工資料-----");
		a.setName("");
		System.out.println(" 好吧!修改姓名為Bnna");
		a.setName("Bnna");
		a.raiseSalary(-1000);
		System.out.println(" 好吧!加薪水1000");
		a.raiseSalary(1000);
		System.out.println("\n ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓");
		System.out.println("員工編號 "+a.getEmpid()+" 修改完成!");
		a.displayInformation();
//----------------------------------------------------------------------	
		System.out.println("\n---繼承練習-------------\n");
		Engineer em3=new Engineer("Tanna","J123456789",48000.0);
		em3.displayInformation();
		
		Manager em4=new Manager("Panna","J123456789",50000.0,"cat_dept");
		em4.displayInformation();
		System.out.println("部門 : "+em4.getDeptName());
		
		Admin em5=new Admin("Canna","J123456789",48000.0);
		em5.displayInformation();
		
		Director em6=new Director("Lanna","J123456789",50000.0,"cat_dept",10);
		em6.displayInformation();
		System.out.println(em6.getName()+" 的部門是 "+em6.getDeptName());
		System.out.println("預算 : "+em6.getBudget());
		
		
		
		
		
	}

}
//src主目錄
//咖啡色包裹形狀的是資料夾
//com是公司名稱

