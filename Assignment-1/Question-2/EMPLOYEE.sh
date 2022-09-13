#! /bin/bash
#bash code for Q2

#input file name
file=EMPLOYEE.txt

#Employee payroll heading
echo -e "------------------------------------------    PAYROLL REGISTER     -------------------------------------------------------------"

#Column Headings
echo -e "Employee_No \t Department \t PayRate \t Exempt \t HoursWorked \t BasePay \t Overtime \t TotalPay"

#while loop for reading data
while read emp_no dep pr ex hw;
do
	#Checking for nonexempt employees and working hours greater than 40
	if [ "$ex" == "N" ] && (( "$hw" > 40 ))
	then
		bp=$( echo "scale=2; $pr*$hw" | bc )
		ot=$( echo "scale=2; ($hw-40)*$pr/2" | bc )
		tp=$( echo "$bp + $ot" | bc )

		echo -e "$emp_no \t\t $dep \t\t $pr \t\t $ex \t\t $hw \t\t $bp \t $ot \t\t $tp"			#printing the data

	else
		bp=$( echo "scale=2; $pr*$hw" | bc )
		echo -e "$emp_no \t\t $dep \t\t $pr \t\t $ex \t\t $hw \t\t $bp \t 0 \t\t $bp"		#printing the data
	fi
#end of while loop
done < $file	#reading data from input file

#variables used: emp_no == employee number; dep == department; pr == pay rate; ex == exempt; hw == hours worked; bp == base pay; ot == ovetime pay; tp == total pay
