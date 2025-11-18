public class RectangleTest {   
	public static void main (String args[]) {
		//寬、高
		Rectangle a=new Rectangle(3,4);
		a.draw();
		
		
		Rectangle a1=new Rectangle(2);
		a1.draw();

		
		Rectangle a2=new Rectangle();
		a2.draw();


		Rectangle a3=new Rectangle(-1,-5);
		a3.draw();
	} 
}

class Rectangle {   
	public int width=5;
	public int height=3;
	
	public Rectangle(int width,int height){
		this.width=width;
		this.height=height;	
	}
	public Rectangle(int width){
		this(width,width);	
	}
	public Rectangle(){
		
	}

	
	public int getArea(){
		return width*height;	
	}
	
	public void draw(){
		if(getArea()>0&& (width>0 && height>0) ){
			if(width==height){
				System.out.println(width+" * "+height+"為正方形");	
			}else{
			System.out.println(width+" * "+height+"為矩形");	
			}
			
			System.out.println(width+" * "+height+" 的面積: "+getArea());	
			for(int i=0;i<height;i++){
				for(int j=0;j<width;j++){
					System.out.print("* ");
				}
				System.out.println();
			}
		}else{
			System.out.println("width: "+width+" 、 height: "+height+" ==>輸入錯誤");	
		}
		
		
		System.out.println();
	}
}
