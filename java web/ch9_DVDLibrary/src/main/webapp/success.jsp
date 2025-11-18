<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.util.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>DVD加入成功</title>
</head>
<body>
	<h1>新增dvd成功</h1>
	您新增一部DVD:<br><br>
	片名:${dvdItem.title }<br><br>
	發行年分:${dvdItem.year }<br><br>
	類型:${dvdItem.genre }<br><br>
	
	<a href="index.jsp">回首頁</a>

</body>
</html>