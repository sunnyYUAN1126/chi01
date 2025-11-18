package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet(
		name = "AddDVDForm", 
		urlPatterns = { "/AddDVDForm" }, 
		initParams = { 
				@WebInitParam(name = "genres-list", value = "Animation, Action, Cat, Dog")
		})
public class AddDVDFormServlet extends HttpServlet {
	private String[] genres;
	

	
	@Override
	public void init() throws ServletException {
		String genreStr=this.getInitParameter("genres-list");
		genres=genreStr.split(", ");
	}
	protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        RequestDispatcher rd = request.getRequestDispatcher("/add_dvd.jsp");
        request.setAttribute("genreList", genres);
        rd.forward(request, response);
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		processRequest(request, response);
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		processRequest(request, response);
	}

}
