package com.example.dao;

import java.io.*;
import java.text.*;
import java.util.*;

import com.example.model.Employee;

public class EmployeeDAOFileImpl implements EmployeeDAO {
	private SortedMap<Integer, Employee> employees=new TreeMap<>();

	private SimpleDateFormat df=new SimpleDateFormat("MMM d, yyyy", Locale.US);
	private String fileName;
	 
	public EmployeeDAOFileImpl(String fileName) {
		super();
		this.fileName = fileName;
	}
	
	public void syncData() throws DAOException{
		try (BufferedReader br=new BufferedReader(new FileReader(fileName))){
			employees.clear();
			while(br.ready()) {
				String line =br.readLine();
				if(line==null || line.length()==0)
					continue;
				String[] data =line.split("\\|");
				try {
					int id=Integer.parseInt(data[0]);
					String fName=data[1];
					String lName=data[2];
					Date bDate=df.parse(data[4]);
					float salary =Float.parseFloat(data[4]);
					Employee emp=new Employee(id,fName,lName,bDate,salary);
					employees.put(id, emp);
					
				}catch(NumberFormatException | ParseException ex) {
					System.err.println("資料轉換失敗: "+line);					
				}				
			}
		}catch(IOException ex){
			throw new DAOException("資料讀取失敗",ex);
		}
	}
	
	private void commit() throws DAOException{
		try(PrintWriter pw=new PrintWriter(new FileWriter(fileName))){
			Set<Integer>index=employees.keySet();
			for(Integer i:index) {
				Employee emp=employees.get(i);
				String line =String.format("%d|%s|%s|%s|%.2f",
						emp.getId(),emp.getFirstName(),emp.getLastName(),
						df.format(emp.getBirthDate()),emp.getSalary()
						);
				pw.println(line);
				
				
			}
			pw.flush();
		}catch(IOException ex){
			throw new DAOException("資料寫出失敗",ex);
		}
	}

	@Override
	public void close() {
		System.out.println("關閉資源...");
	}

	@Override
	public void add(Employee emp) throws DAOException {
		int id=emp.getId();	
		if(employees.containsKey(id))
			throw new DAOException("員工已經存在，新增失敗");
		employees.put(id, emp);
		commit();
	}

	@Override
	public void update(Employee emp) throws DAOException {
		int id=emp.getId();	
		if(employees.containsKey(id))
			throw new DAOException("員工不存在，更新失敗");
		employees.put(id, emp);
		commit();

	}

	@Override
	public void delete(int id) throws DAOException {
		if(!employees.containsKey(id))
			throw new DAOException("員工不存在，刪除失敗");
		employees.remove(id);
		commit();

	}

	@Override
	public Employee findById(int id) throws DAOException {
		syncData();
		Employee emp=employees.get(id);
		if(emp==null)
			throw new DAOException("員工不存在，查詢失敗");
		return emp;
	}

	@Override
	public Employee[] getAllEmployees() throws DAOException {
		syncData();
		return employees.values().toArray(new Employee[0]);
	}

}
