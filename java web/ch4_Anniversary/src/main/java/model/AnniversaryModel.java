package model;

import java.util.*;

public class AnniversaryModel {
	private int year;
	private Map<Integer , String> annualMap;
	public AnniversaryModel() {
		annualMap=new HashMap<>();
		annualMap.put(1, "紙");
		annualMap.put(2, "棉花");
		annualMap.put(3, "皮革");
		annualMap.put(4, "絲綢");
		annualMap.put(5, "木頭");
		annualMap.put(6, "鐵");
		annualMap.put(7, "羊毛");
		annualMap.put(8, "青銅");
		annualMap.put(9, "陶器");
		annualMap.put(10, "錫");
		annualMap.put(11, "鋼");
		annualMap.put(12, "麻");
		annualMap.put(13, "花邊");
		annualMap.put(14, "象牙");
		annualMap.put(15, "水晶");
		annualMap.put(20, "瓷器");
		annualMap.put(25, "銀");
		annualMap.put(30, "珍珠");
		annualMap.put(35, "珊瑚");
		annualMap.put(40, "紅寶石");
		annualMap.put(45, "藍寶石");
		annualMap.put(50, "金");
		annualMap.put(55, "翡翠");
		annualMap.put(60, "鑽石");
		
	}
	public int getYear() {
		return year;
	}
	public void setYear(int year) {
		this.year = year;
	}
	
	public String getMaterial() {
		String result="";
		if(annualMap.containsKey(year)){
            result = annualMap.get(year);
        } 
		return result;
	}
	
	

}
