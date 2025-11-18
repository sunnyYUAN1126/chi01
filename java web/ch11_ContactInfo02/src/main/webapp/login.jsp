<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>登入</title>
</head>
<body>
	<h1>登入畫面</h1>
        <form action="j_security_check" method="post">
            <p>
            	使用者姓名: <input type="text" name="j_username"/><br>
            	使用者密碼: <input type="text" name="j_password"/><br>
            </p>
            <input type="submit" value="登入"/>
            <input type="reset" value="清除"/>
        </form>

</body>
</html>