package com.example.dao;

import com.example.model.Employee;

public interface EmployeeDAO {
	 public void add(Employee emp); //Employee emp=new Employee();-->Employee emp概念是宣告
	 public void update(Employee emp);
	 public void delete(int id);
	 public Employee findById(int id);
	 public Employee[] getAllEmployees();



}
