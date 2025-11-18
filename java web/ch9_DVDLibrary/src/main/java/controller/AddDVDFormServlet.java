package controller;

import java.io.IOException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(name = "AddDVDFormServlet", urlPatterns = {"/AddDVDForm"}, initParams = {
    @WebInitParam(name = "genre-list", value = "Animation, Action, Sci-Fi")})
public class AddDVDFormServlet extends HttpServlet {
    private String[] genres;

    @Override
    public void init() throws ServletException {
        String genreStr = this.getInitParameter("genre-list");
        genres = genreStr.split(", ");        
    }     
    
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        RequestDispatcher rd = request.getRequestDispatcher("/add_dvd.jsp");
        request.setAttribute("genreList", genres);
        rd.forward(request, response);
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

}
