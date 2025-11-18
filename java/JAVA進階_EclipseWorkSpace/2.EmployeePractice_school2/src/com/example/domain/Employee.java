package com.example.domain;

import java.text.NumberFormat;
import java.util.Objects;

public class Employee {
	private static int nextId=101;
	private int empId;
	private String name="www";
	private String ssn="F000000001";
	private double salary=30000;
	protected NumberFormat nf = java.text.NumberFormat.getCurrencyInstance();
	
	public Employee(String name,String ssn,double salary) {
		if (name.trim().length()!=0)
			this.name=name;
		else
			System.out.println(" 姓名預設 ");
		
		if (ssn.trim().length()!=0)
			this.ssn=ssn;
		else
			System.out.println(" 身分證預設 ");
		
		if (salary>=30000)
			this.salary=salary;
		else
			System.out.println(" 薪水預設 ");

		empId=nextId++;
	}
	public String toString() {
		return "-----員工資訊-----"+
				"\n編號   : "+empId+
				"\n姓名   : "+name+
				"\n身分證 : "+ssn+
				"\n薪水   : "+nf.format(salary);
	}
	
	
	public int getEmpid() {
		return empId;
	}
	public String getName() {
		return name;
	}
	public String getSsn() {
		return ssn;
	}
	public double getSalary() {
		return salary;
	}
	
	
	public void setName(String name) {
		if (name.trim().length()!=0)
			this.name=name;
		else
			System.out.println(" 姓名不可以為空!!! ");
	}

	public void raiseSalary(double increase) {
		if(increase>0)
			this.salary=salary+increase;
		else
			System.out.println(" 必須加薪水!!! ");
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
	
	
	

}
