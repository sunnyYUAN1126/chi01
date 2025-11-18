package com.example.domain;

import java.util.ArrayList;

public class Manager extends Employee implements RegularStaff{
	private String deptName;
	protected ArrayList employees;
	private int baseBonus=100000;

	public Manager(String name, String ssn, double salary, String deptName,Branch branch) {
		super(name, ssn, salary,branch);
		this.deptName = deptName;	
		this.employees = new ArrayList();
	}

	public String getDeptName() {
		return deptName;
	}
	
	public boolean addEmployee(Employee emp) {
		if(employees.contains(emp))
			return false;
		else {
			employees.add(emp);
			return true;
		}
	}
	
	public boolean removeEmployee(Employee emp) {
		if(employees.contains(emp)) {
			employees.remove(emp);
			return true;
		}
		return false;
	}
	
	public String getStaffDetails() {
		StringBuilder sb = new StringBuilder();
		if(employees.size()>0) {
			sb.append(getName()+"管理員工:");
			for(Object obj: employees) {
				if(obj instanceof Employee) {
					Employee e = (Employee)obj;
					sb.append(String.format(" %s(%d)", e.getName(),e.getEmpId()));
				}
			}
			sb.append("\n");			
		}
		return sb.toString();
	}

	@Override
	public String toString() {
		return super.toString() + 
			   "管理部門: "+deptName + "\n" +
			   getStaffDetails();
	}
	
	public double getPay() {
		return this.getSalary()+employees.size()*2000;
	}

	@Override
	public double getBonus() {
		// TODO Auto-generated method stub
		return baseBonus* calcPerMultiplier();
	}
	
}
