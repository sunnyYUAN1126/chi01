package web;

import java.io.IOException;
import javax.servlet.DispatcherType;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;


@WebFilter(filterName="SecurityFilter",
		   urlPatterns = { "/SelectCustomer" },
		   dispatcherTypes = {DispatcherType.REQUEST })
public class SecurityFilter extends HttpFilter implements Filter {
   private FilterConfig config;
   
   public void init(FilterConfig fConfig) throws ServletException {
		this.config=fConfig;
	}
	
	public void destroy() {
		this.config=null;
	}


	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		boolean needLogin = true;
		// 檢查 request 物件是否是 HttpServletRequest 類型
		if (request instanceof HttpServletRequest) {
		    
		    // 將 request 轉型成 HttpServletRequest，取得 session 物件
		    HttpSession session = ((HttpServletRequest) request).getSession();
		    
		    // 如果 session 有東西（使用者的工作階段有效）
		    if (session != null) {
		        
		        // 從 session 中取出名為 "user" 的屬性（通常是登入的使用者帳號）
		        String user = (String) session.getAttribute("user");
		        
		        // 如果 user 不是 null，且不是空白字串（代表使用者已登入）
		        if (user != null && user.trim().length() != 0) {
		            
		            // 將 needLogin 設為 false，代表不需要再登入
		            needLogin = false;
		        }
		    }
		}
		
        if(needLogin){
            RequestDispatcher rd = request.getRequestDispatcher("login.jsp");
            rd.forward(request, response);
        } else {
        	chain.doFilter(request, response);
        }
        	
	}


	

}
