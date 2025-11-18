<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page session='true'%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>設定顯示偏好</title>
</head>
<body>
	<h2>設定顯示偏好</h2>
	<form action='<%=response.encodeUrl("Set_Prefs")%>' method="GET">
		顯示欄位:
		<!-- name='show'會記錄"showTitle", "showYear", "showGenre"，被勾選會成一個陣列 -->
		<input type='checkbox' name='show' value='showTitle' 
            <% if(session.getAttribute("showTitle")!=null){ out.print("checked");}%> > 片名            
            <input type='checkbox' name='show' value='showYear' 
            <% if(session.getAttribute("showYear")!=null){ out.print("checked");}%> > 年份         
            <input type='checkbox' name='show' value='showGenre' 
            <% if(session.getAttribute("showGenre")!=null){ out.print("checked");}%> > 類型
            <br><br>
            <input type='submit' value='設定偏好'>
	
	
	</form>

</body>
</html>