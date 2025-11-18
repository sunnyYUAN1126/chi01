package com.example.dao;

import java.util.ArrayList;
import java.util.List;

import com.example.model.Employee;

public class EmployeeDAOMemoryImpl implements EmployeeDAO {
	private Employee[] employeeArray = new Employee[10];
	
	@Override
	public void add(Employee emp) throws DAOException {
		int id=emp.getId();
		try {
			if(employeeArray[emp.getId()]!=null)
				throw new DAOException("員工已經存在，新增失敗");
			employeeArray[emp.getId()] = emp;
		}catch(ArrayIndexOutOfBoundsException aooe){
			throw new DAOException("員工編號需小於10，新增失敗");
		}
		
	}

	@Override
	public void update(Employee emp) throws DAOException {
		int id=emp.getId();
		try {
			if(employeeArray[emp.getId()]!=null)
				throw new DAOException("員工已經存在，新增失敗");
			employeeArray[emp.getId()] = emp;
		}catch(ArrayIndexOutOfBoundsException aooe){
			throw new DAOException("員工編號需小於10，新增失敗");
		}
	}

	@Override
	public void delete(int id) throws DAOException {
		try {
			employeeArray[id] = null;
		}catch(ArrayIndexOutOfBoundsException aooe){
			throw new DAOException("員工編號需小於10，新增失敗");
		}
		
	}

	@Override
	public Employee findById(int id) throws DAOException{
		try {
			return employeeArray[id];
		}catch(ArrayIndexOutOfBoundsException aooe){
			throw new DAOException("員工編號需小於10，新增失敗");
		}
        
	}

	@Override
	public Employee[] getAllEmployees() {
		List<Employee> emps = new ArrayList<>();
        // Iterate through the memory array and find Employee objects
        for (Employee e : employeeArray) {
            if (e != null) {
                emps.add(e);
            }
        }
        return emps.toArray(new Employee[0]);
	}

	@Override
	public void close()  {
		System.out.println("關閉資源...");
		
	}

}
