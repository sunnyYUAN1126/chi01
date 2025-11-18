package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


@WebServlet(name = "SetPrefsServlet", urlPatterns = {"/Set_Prefs"})
public class SetPrefsServlet extends HttpServlet {
	
	protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession();
        String[] shows = request.getParameterValues("show");
        if(shows==null) {
            shows = new String[]{"showTitle", "showYear", "showGenre"};
        }
        
        //這裡把預設值清空(=null)
        session.removeAttribute("showTitle");
        session.removeAttribute("showYear");
        session.removeAttribute("showGenre");
        
        //被勾選的框框加上true，如果其中一個沒有被勾選，上面會出現把值清空，但這裡不會出現被加上true
        for(int i=0; i<shows.length; i++){
            session.setAttribute(shows[i], "true");
        }
        
        RequestDispatcher rd = request.getRequestDispatcher(response.encodeURL("index.jsp"));
        rd.forward(request, response);
    }
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		processRequest(request, response);
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		processRequest(request, response);
	}

}
