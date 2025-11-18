package com.example;

public class Cat extends Animal implements Pet {

	private String name="野貓";
	public Cat() {
		super(4);
	}
	
	public Cat(String name) {
		super(4);
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public void eat() {
		if(name!=null && name.length()!=0 || !name.equals("野貓"))
			System.out.println(name+"最喜歡吃魚");
		else
			System.out.println("貓最喜歡吃魚");			
	}

	@Override
	public void play() {
		// TODO Auto-generated method stub
		System.out.println("跟"+this.name+"貓玩逗貓棒、吃肉泥");
	}

}
