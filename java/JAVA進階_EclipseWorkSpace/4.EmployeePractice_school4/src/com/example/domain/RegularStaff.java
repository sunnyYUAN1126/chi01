package com.example.domain;

import java.util.Random;

public interface RegularStaff {
	
	public String[] gifts=new String[] {"一萬禮券","八千禮券","六千禮券","四千禮券","兩千禮券"};
	
	public static String getLuckDraw() { //類別方法
		int idx=new Random().nextInt(gifts.length);
		return gifts[idx];
	}
	
	public default double calcPerMultiplier() {  //預設方法
//		int ram=new Random().nextInt(5);
//		return (ram+1)*0.5;
		return (int)(Math.random()*5+1)*0.5;
	};
	
	public double getBonus(); //抽象方法
	

}
