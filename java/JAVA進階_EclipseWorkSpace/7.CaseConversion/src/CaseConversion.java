import java.io.*;

public class CaseConversion {

	public static void main(String[] args) {
		boolean toUpper=false;
		if(args.length==0) {
			System.err.println("程式用法: java CaseConversion -U/L");
			System.exit(0);
		}else if(args[0].equalsIgnoreCase("-U")) {
			toUpper=true;
		}else if(args[0].equalsIgnoreCase("-L")) {
			toUpper=false;
		}else {
			System.err.println("程式用法: java CaseConversion -U/L");
			System.err.println("程式結束");
			System.exit(0);
		}
//		try( FileReader fr=new FileReader("source.txt"); 
//			 FileWriter fw=new FileWriter("result.txt")){
//			char[] input=new char[32];
//			int count=0;
//			while((count=fr.read(input))>0) {
//				String line =new String(input,0,count);
//				String output="";
//				if(toUpper)
//					output=line.toUpperCase();
//				else
//					output=line.toLowerCase();
//				fw.write(output);
//			}
//			fw.flush();
//			System.out.println("輸出成功");
//		}catch(IOException ex) {
//			ex.printStackTrace();
//		}
		
		
		try( BufferedReader fr=new BufferedReader(new FileReader("source.txt")); 
			 PrintWriter fw=new PrintWriter (new FileWriter("result.txt"))    ){
				while(fr.ready()) {
					String input=fr.readLine();
					String output=(toUpper)?input.toUpperCase():input.toLowerCase();
					fw.println(output);
				}
				fw.flush();
				System.out.println("輸出成功");
			}catch(IOException ex) {
				ex.printStackTrace();
			}
		
	}

}
