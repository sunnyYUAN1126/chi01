public class VacationScaleTest {
   
	public static void main (String args[]) {
	 
		VacationScale myVacationScale = new VacationScale();

		myVacationScale.yearsOfService = 1;
		myVacationScale.displayVacationDays();
	  
		myVacationScale.yearsOfService = 5;
		myVacationScale.displayVacationDays();
	  	
		myVacationScale.yearsOfService = 10;
		myVacationScale.displayVacationDays();
	} 
}
