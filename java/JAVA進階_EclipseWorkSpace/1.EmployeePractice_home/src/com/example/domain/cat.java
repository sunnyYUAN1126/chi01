package com.example.domain;

public class cat {
	private int apple=20;
	private int banan=30;
	public cat(int apple, int banan) {
		this.apple = apple;
		this.banan = banan;
//		super();不能放
		
	}	
//	public cat() {
//		super();可以放
//	}	
	
	
	public void dis() {
		System.out.println(apple);
		System.out.println(banan);
	}
}
