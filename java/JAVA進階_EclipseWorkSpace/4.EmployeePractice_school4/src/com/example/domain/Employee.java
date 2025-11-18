package com.example.domain;

import java.text.NumberFormat;
import java.util.Locale;
import java.util.Objects;

public abstract class Employee {
	public static int nextId = 101;
	private int empId;
	private String name = "John";
	private String ssn = "A123456789";
	private double salary = 26400;	
	protected Branch branch;
	protected NumberFormat formatter = NumberFormat.getInstance();
	
	public abstract double getPay(); //抽象類別的抽象方法
	
	
	
	
	public Employee(String name, String ssn, double salary,Branch branch) {
		this.empId = nextId++;
		if(name!=null && name.length()!=0)
			this.name = name;
		if(ssn!=null && ssn.length()!=0)
			this.ssn = ssn;
		if(salary>26400)
			this.salary = salary;
		this.branch=branch;
	}
	public Branch getBranch() {
		return branch;
	}

	public int getEmpId() {
		return empId;
	}

	public String getName() {
		return name;
	}


	public void setName(String name) {
		if(name!=null && name.length()!=0)
			this.name = name;
		else
			System.out.println("參數為空值改名失敗!");
	}

	public String getSsn() {
		return ssn;
	}

	public double getSalary() {
		return salary;
	}


	public void raiseSalary(double increase) {
		if(increase>0)
			this.salary += increase;
		else
			System.out.println("參數錯誤加薪失敗!");
	}
	
	@Override
	public int hashCode() {
		return Objects.hash(empId, ssn);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Employee other = (Employee) obj;
		return empId == other.empId && Objects.equals(ssn, other.ssn);
	}

	@Override
	public String toString() {
		return "======員工資料======"+"\n"+
			   "編號: "+this.empId+"\n"+
			   "姓名: "+this.name+"\n"+
			   "SSN: "+this.ssn+"\n"+
			   "薪水: "+this.branch.getCurrency()+formatter.format(salary)+"元"+"\n";
	}
	
}
