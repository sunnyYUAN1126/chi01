import java.util.Scanner;
public class CheckPalindrome{
	public static void main(String args[]){
		
		Scanner sc = new Scanner(System.in,"CP950");  //"CP950"設定繁體中文
		System.out.print("輸入回文: ");
		String s = sc.next();
		
	
		
		String all=s.toLowerCase();
		// all.charAt()也可以
		// 判斷 all.charAt(i)==all.charAt(all.length()) 注意!這裡string字串是方法
		String arr[]=all.split("");
				
		if(arr.length%2!=0){
			all=s.concat("是字串是基數且不是回文");
		}
		else{
			for(int i=0;i<arr.length;i++){
				if(arr[i].equals(arr[((arr.length-1)-i)])){
					all=s.concat("是回文");
					continue;
				}else{
					all=s.concat("不是回文");
					break;
				}
			}		
		}	
		System.out.printf("%s",all);		
	}
}