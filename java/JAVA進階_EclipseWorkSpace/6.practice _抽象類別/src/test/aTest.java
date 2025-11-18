package test;

import father.*;
import son.*;

public class aTest {

	public static void main(String[] args) {


		System.out.println("----------");
		animal lid=new dog();
		lid.AaaOne();

		System.out.println("----------");
		bigdog cc=new littledog();
		cc.AaaOne();
		((dog)cc).BigTwo();
		((littledog)cc).BigTwo();
		

		
		System.out.println("----------");
		

	}

}
