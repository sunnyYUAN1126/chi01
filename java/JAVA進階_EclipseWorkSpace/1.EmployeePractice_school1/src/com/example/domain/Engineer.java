package com.example.domain;

public class Engineer extends Employee {
	private String skill[];
	private int skillCount;

	public Engineer(String name, String ssn, double salary) {
		super(name, ssn, salary);
		skill=new String[5];
		skillCount=0;	
	}
	
	
	public void addSkills(String sk) {
		if(skillCount<5) 
			skill[skillCount++]=sk;
		else
			System.out.println("技能超出範圍，最多5個");
	}
	
	
	public void displayInformation() {
		super.displayInformation();
		if(skillCount<=0)
			System.out.println("沒有技能呦");
		else {
			for(int i=0;i<skillCount;i++) {
				System.out.println("技能"+(i+1)+": "+skill[i]);
			}
		}
	}
}
