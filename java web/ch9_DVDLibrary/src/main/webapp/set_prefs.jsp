<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page session='true'%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
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
               <c:if test='${not empty sessionScope.showTitle}'>checked</c:if> > 片名            
            <input type='checkbox' name='show' value='showYear' 
               <c:if test='${not empty sessionScope.showYear}'>checked</c:if> > 年份         
            <input type='checkbox' name='show' value='showGenre' 
               <c:if test='${not empty sessionScope.showGenre}'>checked</c:if> > 類型
            <br><br>
            <input type='submit' value='設定偏好'>
	
	
	</form>

</body>
</html>