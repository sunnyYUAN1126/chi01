<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.util.*" %>
<%@page import="model.DVDItem" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>


<body>
	<h1>所有DVD</h1>
	<h3>方法一:</h3>
	${DVDList }
	
	<br><br><br><br><br>
	
	<h3>方法二:</h3>
	<%
		List<DVDItem> dvdList=(List<DVDItem>)application.getAttribute("DVDList");
	%>
	<h3>DVD資料庫有 <%=dvdList.size()%> 片DVD</h3>
	<table style="border:1px solid black;">
		<tr>
		   <th style="border:1px solid black;">片名</th>
           <th style="border:1px solid black;">年份</th>
           <th style="border:1px solid black;">類型</th>		
		</tr>
		<% for(DVDItem i:dvdList){ %>
		<tr>
			<td><%=i.getTitle()%></td>
            <td><%=i.getYear()%></td>
            <td><%=i.getGenre()%></td>
		</tr>
		<% } %>
	</table>
</body>
</html>