#Execution command for question-1: awk -f INVENTORY.awk INVENTORY.txt

#Execution command for question-2: ./EMPLOYEE.sh



-----------------------------------------------------   Question-1   -----------------------------------------------------------------------------------------
Input file : INVENTORY.txt
AWK code   : INVENTORY.awk (code file)
Explanation: 	BEGIN: awk will execute the actions if this command once, before reading the input file.
		END  : similar to BEGIN, awk will execute the actions of END before the code exits.
		I have assigned the variable names to the columns in the input data.
		Condition for calculating the order amount is written using the if-else commands.
			(if QualityOnHand < ReorderPoint then OrderAmount=ReorderPoint+MinimumOrder-QualityOnHand; else order amount is null)



-----------------------------------------------------   Question-2   -----------------------------------------------------------------------------------------
Input file : EMPLOYEE.txt
Bash code  : EMPLOYEE.sh (code file)
Explanation:	#! /bin/bash is the shebang line which tells the system to execute the code using 'Bash Shell'.
		'file=EMPLOYEE.txt' & 'done < $file' show that the input data is taken from the EMPLOYEE.txt file.
		I have taken the input from columns of input file as emp_no, dep, pr, ex, hw.
		I used the while loop in read mode to read all the lines of the input file.
		$ is required for using the value of the variable and when assigning values to variables.
		There should be no space between the variable name and '=' sign, else code gives an error.
		bc is bash calculator which is used for returning the decimal results (float values). And 'scale' is for rounding off the decimalplaces.
		At the end of 'if' command 'fi' is written to end the 'if' command.
		Finally I have changed the file to executable mode using 'chmod +x EMPLOYEE.sh' command so that we can execute it in the bash shell.

CalculationPart: BasePay is calculated as Payrate*HoursWorked.
		 Overtime pay is calculated only for non exempt employees who worked more than 40 hrs and is 0.5 times the payrate for those extra hours.
		 
		 Hence for these employees who have OvertimePay, 
		 		Total pay = (Payrate*HoursWorked)+[(HoursWorked-40)*Payrate*0.5]
		 For remaining employees, 
		 		Total pay = Base Pay                    				/*As OvertimePay = 0 (null)*/	
