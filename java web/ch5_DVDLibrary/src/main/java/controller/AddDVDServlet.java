package controller;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.DVDItem;

/**
 * Servlet implementation class AddDVDServlet
 */
@WebServlet("/Add_DVD")
public class AddDVDServlet extends HttpServlet {


	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String title = request.getParameter("title");
        String year = request.getParameter("year");
        String genre = request.getParameter("otherGenre"); //otherGenre(自訂欄位)的值給genre
        if(genre==null || genre.trim().length()==0){
            genre = request.getParameter("genre");
        }
        //如果 otherGenre（自訂欄位）是空的（null 或只是空白），那就改用使用者從下拉選單 genre 選的值。
        
        List<String> errorMsgs = new ArrayList<>(); 
        //宣告一個 List 介面型別的變數，但實際用 ArrayList 這個類別來建立它的物件，而且這個 List 裡面只能放字串 (String)。
        if(title==null||title.trim().length()==0)
            errorMsgs.add("請輸入DVD片名");
        if(year==null||year.trim().length()==0)
            errorMsgs.add("請輸入DVD發行年度");
        else if(!year.trim().matches("\\d\\d\\d\\d"))
            errorMsgs.add("請輸入有效DVD發行年度");
        
        if(!errorMsgs.isEmpty()){ //errorMsgs是空的代表成功
            RequestDispatcher rd = request.getRequestDispatcher("error.jsp");
            request.setAttribute("errorMsgs", errorMsgs);
            rd.forward(request, response);
        }else {
            DVDItem dvd = new DVDItem(title, year, genre);
            RequestDispatcher rd = request.getRequestDispatcher("success.jsp");
            request.setAttribute("dvdItem", dvd);
            rd.forward(request, response);
        }
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		doGet(request, response);
	}

}
