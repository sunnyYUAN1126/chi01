import java.io.BufferedReader;
import java.io.*;

public class ExceptionMain01 {

	public static void main(String[] args) {
		try {
			System.out.println("Reading from file:" + args[0]);
		}catch(ArrayIndexOutOfBoundsException ero) {
			System.err.println("沒有輸入:  "+ero);
			System.exit(0); //結束目前正在執行的 Java 程式
			
		}
		BufferedReader b=null;	
		try {
			b = new BufferedReader(new FileReader(args[0]));
			String s = null;
			while((s = b.readLine()) != null) {
				System.out.println(s);
			}
		}catch(FileNotFoundException e){
			System.err.println("檔案不存在");
		}catch(IOException e) {
			System.err.println("檔案讀取失敗");
		}finally{
			if(b!=null) {
				try {
					b.close(); //關閉檔案或資源，先處理例外再關閉資源
				}catch(IOException e) {
					System.err.println("檔案關閉發生錯誤: "+e);
				}
			}
			
			
		}
	
		
		
		
		
		

	}
}
