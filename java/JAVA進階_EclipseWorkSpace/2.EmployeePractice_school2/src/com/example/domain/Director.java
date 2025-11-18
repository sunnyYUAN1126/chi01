package com.example.domain;

public class Director extends Manager {
	private double budget;

	public Director(String name, String ssn, double salary, String dept,double budget) {
		super(name, ssn, salary, dept);
		this.budget=budget;
	}

	public double getBudget() {
		return budget;
	}
	public String toString() {
		
		return super.toString()+
			   "預算: "+nf.format(budget);
	}



}
