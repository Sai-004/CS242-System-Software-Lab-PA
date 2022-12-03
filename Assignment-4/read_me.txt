#Execution command for question-1: python3 Denominations_Assign04_q1.py 

#Execution command for question-2: pdflatex Latex_Assign04_q2_pg1.tex
				   pdflatex Latex_Assign04_q2_pg2.tex


-----------------------------------------------------   Question-1   ---------------------------------------------------------------------------------------------------
Python Code: 	python3 Denominations_Assign04_q1.py (code file)

INPUT	   :	Enter the required amount (int type) whose denominations are to be found.

Explanation: 	Minimum no.of denominations are found by the two functions minDenominations, minDenominations_25.
		for loop in the function runs for all types of coins and the while checks for the condition that the amount exceeds the currency or not.
		If the condition satifies, then no.of coins of that type and the total no.of coins will be incremented. (ans[i],coins)
		Function return a pair of values coins (total no.of coins) and ans list (list of no.of coins of each type).
		In the minDenominations_25 function, 25 coin type is removed and calculated.
		This method of using 2 functions is followed as the type of coins have a change in their difference in 25,20 where else other are atleast doubled.
		As the difference is not doubled, normal calculation gives error as the count for the 25 will be consider but counting 20 gives the least denominatins.
		Function is called after taking the input of the required amount.
		Minimum of the no.of coins found from the two functions is taken as the minimum denominations and the no.of coins of each type are printed		

-----------------------------------------------------   Question-2   --------------------------------------------------------------------------------------------------
Latex Code : 	pdflatex Latex_Assign04_q2_pg1.tex (code file for part-1 of Q2)
		pdflatex Latex_Assign04_q2_pg2.tex (code file for part-2 of Q2)
		 	
Explanation:	\documentclass{article} --> denotes that the pdf created from the latex file will have an article type layout.
		\usepackage{amsmath,amssymb,color} --> these are the packages used in the latex code written.
		\today --> gives todays date.
		\begin{document}
				--> complete code for the contents of the file are to be written within this begin{document} and end{document} section.
		\end{document}
		\section --> this command divides the text into sections.
		\LaTeX --> converts the latex into a different (required) format.
		\begin{align}  --> used for writing mathematical equations which require a different font and symbols and also gives the numbering for the equation.
		different types of begin-end sections are used in the code file which have their own use and this is reflecting the output pdf file after ecxecution.
		
