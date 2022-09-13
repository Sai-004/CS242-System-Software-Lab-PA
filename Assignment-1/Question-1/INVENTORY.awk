#awk code for Q1

#Inventory Heading
BEGIN{print"-------------------------------INVENTORY REPORT---------------------------------------------"}

#Coloumn Headings
BEGIN{print"Part.No\t\tPrice\t\tQualityOnHand\tReorderPoint\tMininmumOrder\tOrderAmount"}

#Assigning variable names to the columns
{p_no=$1; price=$2; quality=$3; reord=$4; min_ord=$5; ord_am=($4+$5-$3) }

#condition to check for OrderAmount and printing the valid data
{ if( quality < reord ) print p_no"\t\t"price"\t\t"quality"\t\t"reord"\t\t"min_ord"\t\t"ord_am ;	#if QualityOnHand < ReorderPoint, calculate the OrderAmount
  else print p_no"\t\t"price"\t\t"quality"\t\t"reord"\t\t"min_ord"\t\t--"}				#else order amount is 0 (--)

#End statement
END{print"\t\t\t\tEND REPORT"}

#variables used: p_no == Part Number; reord == Reorder Point; min_ord == Minimum Order; ord_am == Order Amount
