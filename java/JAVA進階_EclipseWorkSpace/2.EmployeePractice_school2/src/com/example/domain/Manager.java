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
	public String getStaffDetails() {
		StringBuilder sb=new StringBuilder();
		if(! employees.isEmpty()) {
			sb.append(this.getName()+"管理員工: ");
			for(Object obj : employees){
				 if(obj instanceof Employee){
					 Employee e = (Employee)obj;
					 sb.append( String.format("%s(%d)",e.getName(),e.getEmpid())   );
				 } 
			}
			sb.append("\n");
		}
		return sb.toString();
	}
	
	
	public String toString() {
		return super.toString()+
		       "\n部門: "+dept+"\n"+
		       this.getStaffDetails();
	}
	

}
