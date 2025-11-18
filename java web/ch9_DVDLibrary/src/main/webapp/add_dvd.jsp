<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>新增DVD</title>
</head>
<body>
	<form action="Add_DVD" method="POST">  <!--這一行在呼叫@WebServlet("/Add_DVD")這個檔案-->
		片名:<input type="text" name="title"><br><br>
		年分:<input type="text" name="year"><br><br>
		
		類型:<select name="genre">
			 <c:forEach var='genre' items='${genreList}'>
		            	<option value='${genre}'>${genre}</option>
		            </c:forEach>
             </select>
         
         或其他種類: <input type="text" name="otherGenre">
         <br><br>
         
         <input type='submit' value='儲存'/>
	</form>
</body>
</html>