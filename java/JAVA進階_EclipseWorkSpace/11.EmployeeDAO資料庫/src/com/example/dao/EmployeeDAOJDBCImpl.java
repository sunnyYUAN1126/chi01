package com.example.dao;

import java.sql.*;
import java.util.ArrayList;

import com.example.model.Employee;

public class EmployeeDAOJDBCImpl implements EmployeeDAO {
	private Connection conn;

	

	public EmployeeDAOJDBCImpl() {
		String url = "jdbc:mysql://localhost:3306/EmployeeDB";
        String username = "root";
        String password = "123123";
        try {
        	conn=DriverManager.getConnection(url,username,password);     	
        }catch(SQLException ex) {
        	System.out.println("資料庫連線建立失敗: "+ex);
        	System.exit(0);
        }
	}

	@Override
	public void add(Employee emp) throws DAOException {
		String sql="insert into employee values(?,?,?,?,?)";
		try(PreparedStatement pstmt=conn.prepareStatement(sql)){
			pstmt.setInt(1, emp.getId());
			pstmt.setString(2, emp.getFirstName());
			pstmt.setString(3, emp.getLastName());
			pstmt.setDate(4, new java.sql.Date(emp.getBirthDate().getTime()));
			pstmt.setFloat(5, emp.getSalary());
			
			if(pstmt.executeUpdate()!=1)
				throw new DAOException("新增員工失敗!");
//			IGNORE 的意思是：忽略錯誤繼續執行
//			所以加入IGNORE，，「if會執行」並且不執行例外
//			如果沒有加入IGNORE，if會不執行並且「直接執行例外」
		}catch(SQLException ex) {
			throw new DAOException("資料庫新增發生錯誤: "+ex);
		}

	}

	@Override
	public void update(Employee emp) throws DAOException {
		String sql="update employee set firstname=?,lastname=?,birthdate=?,salary=? where ID=?";
		try(PreparedStatement pstmt=conn.prepareStatement(sql)){
			pstmt.setInt(1, emp.getId());
			pstmt.setString(2, emp.getFirstName());
			pstmt.setString(3, emp.getLastName());
			pstmt.setDate(4, new java.sql.Date(emp.getBirthDate().getTime()));
			pstmt.setFloat(5, emp.getSalary());
			
			if(pstmt.executeUpdate()!=1)
				throw new DAOException("更新員工失敗!");
		}catch(SQLException ex) {
			throw new DAOException("資料庫新增發生錯誤: "+ex);
		}

	}

	@Override
	public void delete(int id) throws DAOException {
		String sql="delete from employee where ID=?";
		try(PreparedStatement pstmt=conn.prepareStatement(sql)){
			pstmt.setInt(1, id);
			if(pstmt.executeUpdate()!=1)
				throw new DAOException("刪除員工失敗!");
		}catch(SQLException ex) {
			throw new DAOException("資料庫新增發生錯誤: "+ex);
		}

	}

	@Override
	public Employee findById(int id) throws DAOException {
		String query ="select * from employee where ID=?";
		Employee emp=null;
		try(PreparedStatement pstmt=conn.prepareStatement(query)){
			pstmt.setInt(1, id);
			ResultSet rs=pstmt.executeQuery();
			if(rs.next())
				emp=new Employee(rs.getInt("ID"),rs.getString("FIRSTNAME"),rs.getString("LASTNAME"),rs.getDate("BIRTHDATE"),rs.getFloat("SALARY"));
			return emp;
		}catch(SQLException ex) {
			throw new DAOException("資料庫新增發生錯誤: "+ex);
		}
	}

	@Override
	public Employee[] getAllEmployees() throws DAOException {
		String query ="select * from employee";
		ArrayList<Employee> emps=new ArrayList<>();
		try(Statement stmt=conn.createStatement()){
			ResultSet rs=stmt.executeQuery(query);
			while(rs.next())
				emps.add(new Employee(rs.getInt("ID"),rs.getString("FIRSTNAME"),rs.getString("LASTNAME"),rs.getDate("BIRTHDATE"),rs.getFloat("SALARY")));
			return emps.toArray(new Employee[0]);
		}catch(SQLException ex) {
			throw new DAOException("資料庫新增發生錯誤: "+ex);
		}
		
	}
	
	@Override
	public void close() throws Exception {
		conn.close();
	}

}
