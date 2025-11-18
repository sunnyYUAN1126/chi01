package com.example.domain;

import java.util.ArrayList;

public class Manager extends Employee {
	private String dept;
	private ArrayList employees= new ArrayList();
	
	
	
	
	public Manager(String name,String ssn,double salary, String dept) {
		super(name,ssn,salary);
		this.dept=dept;
	}
	public String getDeptName() {
		return dept;
	}
	
	
	
	
	
	public boolean addEmployee(Employee e) {
		if(employees.contains(e))
			return false;
		else {
			employees.add(e);
			return true;
		}	
	}
	public boolean removeEmployee(Employee e) {
		if(employees.contains(e)) {
			employees.remove(e);
			return true;
		}
		else {
			return false;
		}	
	}
	public void printStaffDetails() {
		if(! employees.isEmpty()) {
			System.out.print(this.getName()+"管理員工: ");
			for(Object obj : employees){
				 if(obj instanceof Employee){
					 Employee e = (Employee)obj;
					 System.out.printf("%s(%d)",e.getName(),e.getEmpid());
				 }
				 
			}
			System.out.println();
		}
	}
	
	
	public void displayInformation() {
		super.displayInformation();
		System.out.println("部門: "+dept);
		this.printStaffDetails();
	}
	

}
