public class VacationScale {
	public int yearsOfService;
	public int vacationDays[]=new int[]{10,15,15,15,20,20,25};
	
	public void displayVacationDays(){
		//int vacationDays[]=new int[]{10,15,15,15,20,20,25};
		//int vacationDays[]={10,15,15,15,20,20,25};
		
		if(yearsOfService>6){
			System.out.println(yearsOfService+" years: vacation have "+vacationDays[6]);
		}
		else{
			System.out.println(yearsOfService+" years: vacation have "+vacationDays[yearsOfService]);
		}
			
		

	}
}
