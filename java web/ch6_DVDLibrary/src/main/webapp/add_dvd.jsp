<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
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
			 <% 
				 String[] genres = (String[])request.getAttribute("genreList");
	             for(String genre : genres) {
			 %>
			 	<option value="<%=genre%>"><%=genre%></option>
			 <%  }  %>
             </select>
         
         或其他種類: <input type="text" name="otherGenre">
         <br><br>
         
         <input type='submit' value='儲存'/>
	</form>
</body>
</html>