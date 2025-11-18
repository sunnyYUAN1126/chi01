package web;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

import javax.servlet.ServletContext;
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;

import model.DVDItem;


@WebListener
public class InitializeLibrary implements ServletContextListener {

    
   

	
    public void contextDestroyed(ServletContextEvent sce)  { 
    	ServletContext context = sce.getServletContext();
        context.log("The Context will be destroyed!");
    }

    public void contextInitialized(ServletContextEvent sce)  { 
    	ServletContext context = sce.getServletContext();
    	
    	String[] genres=context.getInitParameter("genres-list").split(", ");
    	context.setAttribute("genreList", genres);
    	context.log("the genre list has been loaded");
    	    	
    	
    	//左邊libraryFile是Java 變數，用來存放取出的設定值（通常是檔案路徑）
        String libraryFile = context.getInitParameter("libraryFile"); //右邊"libraryFile"對應 web.xml 裡 <param-name>libraryFile</param-name>
        List<DVDItem> dvdList = new LinkedList<>();
        try(InputStream is = context.getResourceAsStream(libraryFile); //getResourceAsStream() 會打開該檔案並回傳 InputStream，之後讀檔
            BufferedReader br = new BufferedReader(new InputStreamReader(is))){
            String record;
            while((record=br.readLine())!=null){
                try{
                    String[] data = record.split("\\|");
                    DVDItem dvd =new DVDItem(data[0],data[1],data[2]);
                    dvdList.add(dvd);
                } catch(Exception e){
                    context.log("wrong data:"+record);
                }
            }
            context.setAttribute("DVDList", dvdList);
            context.log("The library file has been loaded!");
        } catch(Exception e){
            context.log("Processing library file exception: " + e);
        }  
    }
	
}
