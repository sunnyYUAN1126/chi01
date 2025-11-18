<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>客戶資訊</title>
</head>
<body>
	<h3>${user},你好!</h3>
	<h3>客戶資訊</h3>
	<c:choose>
		<c:when test="${not empty customer}">
			<p>姓名: ${customer.name}</p>
			<c:if test="${not empty customer.officeAddress}">
				<p>
					辦公室地址:<br> ${customer.officeAddress.address1},<br>
					${customer.officeAddress.address2},<br>
					${customer.officeAddress.city},<br>
					${customer.officeAddress.country},<br>
					${customer.officeAddress.postcode}<br>
				</p>
			</c:if>
			<c:if test="${not empty customer.billingAddress}">
				<p>
					發票地址:<br> ${customer["billingAddress"].address1},<br>
					${customer["billingAddress"].address2},<br>
					${customer["billingAddress"].city},<br>
					${customer["billingAddress"].country},<br>
					${customer["billingAddress"].postcode}<br>
					<!-- billingAddress對應 public Address getBillingAddress() -->
				</p>
			</c:if>
			<c:if test="${not empty customer.addresses[2]}">
				<p>
					送貨地址:<br> ${customer.addresses[2].address1},<br>
					${customer.addresses[2].address2},<br>
					${customer.addresses[2].city},<br>
					${customer["addresses"][2].country},<br>
					${customer["addresses"][2].postcode}<br>
				</p>
			</c:if>
		</c:when>
		<c:otherwise>
			<h3>查詢的客戶不存在</h3>
		</c:otherwise>
	</c:choose>
</body>
</html>

