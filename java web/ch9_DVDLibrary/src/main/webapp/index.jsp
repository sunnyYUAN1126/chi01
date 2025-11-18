<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page session='true' %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>DVD資料庫</title>
</head>
<body>
	<h2>DVD資料庫</h2>
	<ul>
		<li>
			<a href='<c:url value="list_library.jsp"/>'>顯示所有ＤＶＤ</a>
		</li>
		<li>
			<a href="add_dvd.jsp">新增DVD喔</a>
		</li>
		<li>
			<a href='<c:url value="set_prefs.jsp"/>'>設定顯示偏好</a>
		</li>
	</ul>

</body>
</html>