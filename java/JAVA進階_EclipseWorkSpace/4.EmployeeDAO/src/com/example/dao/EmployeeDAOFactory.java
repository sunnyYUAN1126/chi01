package com.example.dao;

public class EmployeeDAOFactory {
	public EmployeeDAO createEmployeeDAO( ) { //方法 回傳型別（這個方法會回傳一個 EmployeeDAO 的東西）
		 return new EmployeeDAOMemoryImpl() ; //呼叫建構子，建立一個物件
	}

}

//類似
//public int fun() {
//	return a;
//}
