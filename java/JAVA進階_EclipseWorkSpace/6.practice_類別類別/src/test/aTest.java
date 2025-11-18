package test;

import father.*;
import son.*;

public class aTest {

	public static void main(String[] args) {

		animal a=new animal();
		a.animalAll();
		a.Same();
		System.out.println("----------");

//		
//		animal alittledog=new littledog();		
//		System.out.println("animal alittledog=new littledog();");
//		
//		System.out.println("----類別強制換----");
//		System.out.println("----bigdog----");
//		((bigdog)alittledog).bigdog1();
//		
//		System.out.println("\n"+"----dog----");
//		((dog)alittledog).bigdog1();
//		((dog)alittledog).dog1();
//		
//		System.out.println("----littledog----");
//		((littledog)alittledog).bigdog1();
//		((littledog)alittledog).dog1();;
//		((littledog)alittledog).littledog1();
//		
//		System.out.println("\n----類別繼承----");
//		alittledog.animalAll();
//		
//		System.out.println("\n----介面----");
//		animal abigdog=new bigdog(); 
//		animal adog=new dog();
//
//		((INanimal)abigdog).inabc();
//		((INanimal)adog).inabc();
//		((INanimal)alittledog).inabc();
//		
//		((bigdog)alittledog).inabc();
		
		System.out.println("----------");

		animal one=new dog();
		bigdog two=new littledog();
		
		one.Same();
		((dog)one).Samebigdog();

		
		System.out.println("----------");
		two.Same();
		two.Samebigdog();
		
		
		INanimal one000=new INanimal();
		one000.inabc();


		
		

	}

}
