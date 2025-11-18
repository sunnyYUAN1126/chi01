package domain;

import java.util.Collection;
import java.util.HashMap;

public class Customer {
	 private String name;
	 private Address [] addresses;
	 public static final int HEAD_OFFICE = 0;
	 public static final int BILLING = 1;
	 public static final int DELIVERY = 2;
	 
	 public Customer(String name, Address office, Address billing, Address delivery ){
	        this.name = name;
	        this.addresses = new Address[3];
	        addresses[HEAD_OFFICE] = office;
	        addresses[BILLING] = billing;
	        addresses[DELIVERY] = delivery;
	    }
	//測試資料
    private static final HashMap<Integer, Customer> customers = new HashMap<Integer, Customer>();
    static {
        customers.put(1, new Customer("賴清德", 
                        new Address("凱達格蘭大道1號", "總統府廣場", "台北", "台灣", "100"), 
                        new Address("重慶南路一段122號", "總統府", "台北", "台灣", "100"),
                        new Address("重慶南路二段100號", "總統官邸", "台北", "台灣", "100")));
        customers.put(2, new Customer("蔣萬安", 
                        new Address("市府路1號", "台北市政府", "台北", "台灣", "110"), 
                        null,
                        new Address("徐州路46號", "台北市長官邸", "台北", "台灣", "100")));
    }
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Address[] getAddresses() {
		return addresses;
	}
	public void setAddresses(Address[] addresses) {
		this.addresses = addresses;
	}
    
	
	public Address getOfficeAddress() {
        return addresses[HEAD_OFFICE];
    }

    public Address getBillingAddress() {
        return addresses[BILLING];
    }

    public Address getDeliveryAddress() {
        return addresses[DELIVERY];
    }
    
    public static Customer getCustomer(int id) {
        return customers.get(id);
    }
    
    public static Collection<Customer> getCustomers() {
        return customers.values();
    }


}
