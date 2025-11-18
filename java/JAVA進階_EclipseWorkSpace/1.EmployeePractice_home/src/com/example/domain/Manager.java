package com.example.domain;

public class Manager extends Employee {
	private String dept;
	public Manager(String name,String ssn,double salary, String dept) {
		super(name,ssn,salary);
		this.dept=dept;
	}
	public String getDeptName() {
		return dept;
	}
	

}
