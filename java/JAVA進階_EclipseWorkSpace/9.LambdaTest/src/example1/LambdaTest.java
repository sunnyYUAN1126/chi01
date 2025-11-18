package example1;

public class LambdaTest {

    public static void main(String[] args) {
        String[] strList01 = {"tomorrow", "toto", "to", "timbukto", "the", "hello", "heat"};

        AnalyzerTool stringTool = new AnalyzerTool();
        String searchStr = "to";

        System.out.println("Searching for: " + searchStr);

        System.out.println("==Contains==");
//        寫法一
//        stringTool.showResult(strList01, searchStr, new ContainsAnalyzer());
//        寫法二
//        stringTool.showResult(strList01, searchStr, new StringAnalyzer() {
//        	public boolean analyze(String target, String searchStr){
//        		return target.contains(searchStr);
//        	}
//        });
//        寫法三
        stringTool.showResult(strList01, searchStr, (t,s)->t.contains(s)); //(t,s)->t.contains(s)這一段就是 analyze方法
        System.out.println("==Starts With==");
        stringTool.showResult(strList01, searchStr, (t,s)->t.startsWith(s));

        System.out.println("==Equals==");
        stringTool.showResult(strList01, searchStr, (t,s)->t.equalsIgnoreCase(s));

        System.out.println("==Ends With==");
        stringTool.showResult(strList01, searchStr, (t,s)->t.endsWith(s));

        System.out.println("==Less than 5==");
        stringTool.showResult(strList01, searchStr, (t,s)->t.contains(s)&&t.length()<5);

        System.out.println("==Greater than 5==");
        stringTool.showResult(strList01, searchStr, (t,s)->t.contains(s)&&t.length()>5);
    }
    
}
