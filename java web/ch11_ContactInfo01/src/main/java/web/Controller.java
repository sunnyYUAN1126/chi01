package web;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import domain.Customer;

@WebServlet("/SelectCustomer")
public class Controller extends HttpServlet {
	protected void processRequest(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int custid = Integer.parseInt(request.getParameter("custid"));
		RequestDispatcher rd=null;
		if(custid==0) {
			request.setAttribute("customers", Customer.getCustomers());
			rd = request.getRequestDispatcher("customerList.jsp");
		}else {
			request.setAttribute("customer", Customer.getCustomer(custid));
			rd = request.getRequestDispatcher("customerView.jsp");
		}
		rd.forward(request, response);
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		processRequest(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		processRequest(request, response);
	}

}
