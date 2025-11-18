<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>顯示地址</title>
</head>
<body>
	<jsp:useBean id="addressBean" scope="session" class="domain.Address" />
	<h3>
		我的地址:<br>
		<jsp:getProperty name="addressBean" property="address1" />,
		<jsp:getProperty name="addressBean" property="address2" />, <br>
		<jsp:getProperty name="addressBean" property="city" />.
		<jsp:getProperty name="addressBean" property="country" />, <br>
		<jsp:getProperty name="addressBean" property="postcode" />, <br>
	</h3>

</body>
</html>