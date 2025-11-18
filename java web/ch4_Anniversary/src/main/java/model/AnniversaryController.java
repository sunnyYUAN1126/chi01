package model;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class AnniversaryController
 */
@WebServlet("/AnniversaryController")
public class AnniversaryController extends HttpServlet {
	//private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String yearStr = request.getParameter("year");
		int year =0;
		try {
			year =Integer.parseInt(yearStr);
		}catch(NumberFormatException ex){
			ex.printStackTrace();   
		}
		AnniversaryModel aModel = new AnniversaryModel();
        aModel.setYear(year);
        
        RequestDispatcher rd = request.getRequestDispatcher("anniversaryView.jsp");
        request.setAttribute("model_go", aModel);
        rd.forward(request, response);
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
		//doPost都會呼叫doGet
	}
	


}
