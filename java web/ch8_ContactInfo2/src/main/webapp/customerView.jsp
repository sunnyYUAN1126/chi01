<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Customer Info</title>
    </head>
    <body>
        <h3>客戶資訊</h3>
        <p>姓名: ${customer.name}</p>
        <p>辦公室地址:<br>
            ${customer.officeAddress.address1},<br>
            ${customer.officeAddress.address2},<br>
            ${customer.officeAddress.city},<br>
            ${customer.officeAddress.country},<br>
            ${customer.officeAddress.postcode}<br>            
        </p>
        <p>發票地址:<br>
            ${customer["billingAddress"].address1},<br>
            ${customer["billingAddress"].address2},<br>
            ${customer["billingAddress"].city},<br>
            ${customer["billingAddress"].country},<br>
            ${customer["billingAddress"].postcode}<br> 
            <!-- billingAddress對應 public Address getBillingAddress() -->           
        </p>
        <p>送貨地址:<br>
            ${customer.addresses[2].address1},<br>
            ${customer.addresses[2].address2},<br>
            ${customer.addresses[2].city},<br>
            ${customer["addresses"][2].country},<br>
            ${customer["addresses"][2].postcode}<br>            
        </p>
        
    </body>
</html>

