<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>輸入地址</title>
</head>
<body>
	<h2>輸入地址</h2>
	<form action="setAddress.jsp">
		地址一:<input type="text" name="address1"><br>
		<br> 地址二:<input type="text" name="address2"><br>
		<br> 城市:<input type="text" name="city"><br>
		<br> 國家:<input type="text" name="country"><br>
		<br> 郵遞區號:<input type="text" name="postcode"><br>
		<br> <input type="submit" value="送出">
	</form>
	<a href="showAddress.jsp">查詢</a>

</body>
</html>