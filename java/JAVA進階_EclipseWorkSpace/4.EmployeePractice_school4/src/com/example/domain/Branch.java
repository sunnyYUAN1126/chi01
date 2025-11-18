package com.example.domain;

public enum Branch {
	Taipei("NT$"), London("£"), Paris("€") ,Tokyo("¥");
	private final String currency;
	private Branch(String c) {
		currency=c;
	}
	
	public String getCurrency() {
		return currency;
	}

	

}
