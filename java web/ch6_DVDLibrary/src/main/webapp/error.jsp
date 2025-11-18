<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.util.*" %> 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<font color="red">
		修正:
		<ul>
			<%
			List<String> errors = (List<String>)request.getAttribute("errorMsgs");
            for(String error : errors) {
			%>
			<li>
				<%=error %>
			</li>
			<%
            }
			%>	
		</ul>
	</font>
	<a href="AddDVDForm">重新輸入</a>

</body>
</html>