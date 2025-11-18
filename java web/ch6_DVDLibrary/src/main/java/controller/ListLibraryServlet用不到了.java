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


@WebServlet(name = "List_Library", urlPatterns = { "/List_Library" })
public class ListLibraryServlet用不到了 extends HttpServlet {
	
	    
    private List<DVDItem> createDvdList(){
        List<DVDItem> dvds = new ArrayList<DVDItem>();
        dvds.add(new DVDItem("Spiderman", "2000", "Action"));
        dvds.add(new DVDItem("Forzen", "2014", "Animation"));
        dvds.add(new DVDItem("TransFormer4", "2014", "Action"));
        return dvds;
    }
    
    protected void processRequest(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<DVDItem> dvdList = this.createDvdList();
        
        RequestDispatcher rd = request.getRequestDispatcher("list_library.jsp");
        request.setAttribute("DVDList", dvdList);
        rd.forward(request, response);        
    }

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {		
		processRequest(request, response);
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {	
		processRequest(request, response);
	}

}
