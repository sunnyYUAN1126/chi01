<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@page session='true'%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>


<body>
	<c:if test= '${empty sessionScope}' >
            <c:set var = "showTitle"  value = "true" scope = "session"/>
            <c:set var = "showYear"  value = "true" scope = "session"/>
            <c:set var = "showGenre"  value = "true" scope = "session"/>
        </c:if>
        <h3>DVD Library 中有${DVDList.size()}片DVD</h3>
        <table>
            <tr>
            <tr>
            <c:if test='${not empty sessionScope.showTitle}'>
                <th>片名</th>
            </c:if>
            <c:if test='${not empty sessionScope.showYear}'>
                <th>年份</th>
            </c:if>
            <c:if test='${not empty sessionScope.showGenre}'>
                <th>類型</th>
            </c:if>
            </tr>
            <c:forEach var='dvd' items='${DVDList}'>
            <tr>
            <c:if test='${not empty sessionScope.showTitle}'>          
                <td>${dvd.title}</td>
            </c:if>
            <c:if test='${not empty sessionScope.showYear}' >
                <td>${dvd.year}</td>            
            </c:if>
            <c:if test='${not empty sessionScope.showGenre}'>
                <td>${dvd.genre}</td>            
            </c:if>
            </tr>            
        	</c:forEach>
        </table>
</body>
</html>