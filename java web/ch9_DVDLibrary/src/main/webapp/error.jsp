<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.util.*" %> 
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
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
			<c:forEach var='error' items='${errorMsgs}'>
            	<li>${error}</li>
        	</c:forEach>	
		</ul>
	</font>
	<a href="AddDVDForm">重新輸入</a>

</body>
</html>