package com.example.domain;

public class Director extends Manager {
	private double budget;
	private int baseBonus=500000;
	

	public Director(String name, String ssn, double salary, String deptName, double budget,Branch branch) {
		super(name, ssn, salary, deptName,branch);
		this.budget = budget;
	}

	public double getBudget() {
		return budget;
	}

	@Override
	public String toString() {
		return super.toString() + 
			   "管理預算: "+this.branch.getCurrency()+formatter.format(budget) + "\n";
	}
	
	public double getPay() {
		return this.getSalary()+employees.size()*10000;
//		這裡測試THIS屬性、方法看看
	}
	public double getBonus() {
		return baseBonus* calcPerMultiplier();
	}
	
}
