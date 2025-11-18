package com.example;

public class animal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		Ostrich o = new Ostrich(); //子
//		o.move();
//		o.hide();
		
		Bird b=new Bird(); //父
		b.move();
		Bird bo=new Ostrich(); //父=子
		bo.move();
//		bo.hide();不行
		((Ostrich) bo).hide(); //父子關係強制轉   (子)父.呼叫子方法
//		System.out.println( "強制轉型測驗----" );
//		((OstrichLittie)bo).cat();
		
		System.out.println(   (b instanceof Ostrich)   ); //父 instanceof 子
		
		
//		強制轉型測驗
		System.out.println( "----" );
		Bird c=new OstrichLittie();
		((OstrichLittie)c).cat();
		((Ostrich)c).hide();
	}
}
class Animaljj {
	public void move() {
		System.out.println("動");
	}
}

class Bird extends Animaljj {
	 public void move() {
		 System.out.println("飛");
	 }
}
class Ostrich extends Bird {
	 public void move() {
		 super.move();
		 System.out.println("跑");
	 }
	 public void hide() {
		 System.out.println("頭埋在土裡");
	 }
}


class OstrichLittie extends Ostrich {
	 public void move() {
		 System.out.println("跑");
	 }
	 public void cat() {
		 System.out.println("喵");		 
	 }
}