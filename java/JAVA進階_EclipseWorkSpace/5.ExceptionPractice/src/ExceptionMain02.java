import java.io.*;

public class ExceptionMain02 {

	public static void main(String[] args) {
		try {
			System.out.println("Reading from file:" + args[0]);
		}catch(ArrayIndexOutOfBoundsException ero) {
			System.err.println("沒有輸入:  "+ero);
			System.exit(0);
			
		}
//		BufferedReader b=null;
		try (BufferedReader b=new BufferedReader(new FileReader(args[0]))){  //這寫法會自動關閉檔案(b.close)，先關閉資源在處理例外
//			b = new BufferedReader(new FileReader(args[0]));
			String s = null;
			while((s = b.readLine()) != null) {
				System.out.println(s);
			}
		}catch(FileNotFoundException e){
			System.err.println(args[0]+"檔案不存在");
		}catch(IOException e) {
			System.err.println(args[0]+"檔案讀取失敗"+e.getMessage());
		}

	
		
		
		
		
		

	}
}
