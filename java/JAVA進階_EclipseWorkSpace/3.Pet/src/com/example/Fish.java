package com.example;

public class Fish extends Animal implements Pet{

	public Fish() {
		super(0);
	}
	
	@Override
	public void eat() {
		System.out.println("大魚吃小魚");
	}

	@Override
	public void walk() {
		System.out.println("魚沒有腳,只會游泳");
	}

	@Override
	public void play() {
		// TODO Auto-generated method stub
		System.out.println("靜靜的欣賞魚");
	}

	
}
