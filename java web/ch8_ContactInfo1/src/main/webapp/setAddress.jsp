<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>設定地址</title>
</head>
<body>
	<jsp:useBean id="addressBean" scope="session" class="domain.Address"/>
    <jsp:setProperty name="addressBean" property="*"/>  
        <h3>地址設定成功!</h3>
        <ul>
            <li><jsp:getProperty name="addressBean" property="address1"/></li>
            <li><jsp:getProperty name="addressBean" property="address2"/></li>
            <li><jsp:getProperty name="addressBean" property="city"/></li>
            <li><jsp:getProperty name="addressBean" property="country"/></li>
            <li><jsp:getProperty name="addressBean" property="postcode"/></li>
        </ul>

</body>
</html>