<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
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
			<a href='<%=response.encodeURL("list_library.jsp")%>'>顯示DVD喔</a>
		</li>
		<li>
			<a href="AddDVDForm">新增DVD喔</a>
		</li>
		<li>
			<a href='<%=response.encodeURL("set_prefs.jsp")%>'>設定顯示偏好</a>
		</li>
	</ul>

</body>
</html>