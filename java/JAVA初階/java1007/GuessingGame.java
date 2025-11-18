public class GuessingGame{
	public static void main(String args[]){
		if ( (args.length==0) || (args[0].equalsIgnoreCase("help"))   )
			System.out.println(" 程式用法: java Guessing [1-5 數字] ");
		else if(! (args[0].matches("\\d+")) )
			//matches: 傳回值為boolean，驗證此字串是否符合給定的正則表達式。
			System.out.println(" 猜測內容須為數字 ");
		else{
			int guessing= Integer.parseInt(args[0]);
			if(guessing>0 && guessing<6){
				int random=(int)((Math.random()*5)+1);	
				if(random==guessing)
					System.out.println(" 恭喜猜對! ");	
				else
					System.out.println(" 猜錯!答案為"+random);
			}else 
				System.out.println(" 請猜測數字1~5之間 ");
		}
		
		
		
		

	}
}