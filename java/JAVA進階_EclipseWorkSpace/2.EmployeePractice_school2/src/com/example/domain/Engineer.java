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
	
	
	public String toString() {
		StringBuilder sb=new StringBuilder(super.toString());
		if(skillCount<=0)
			sb.append("\n沒有技能呦");
		else {
			for(int i=0;i<skillCount;i++) {
				sb.append("\n技能"+(i+1)+": "+skill[i]);
			}
		}
		return sb.toString();
	}
}
