#!/bin/perl
#Q2. PERL script to generate Random Strings

#opening the input file and reading
open( input , "<" , <input.txt> );

#storing the file input in a variable, here total input is stored as a single unit...
$input = <input>;
chomp $input;

#array to store the alphabet of the input data
@alphabet;

for( $i = 0 ; $i < length($input)-1 ; $i++ )
{
	$alphabet[$i] = substr($input, $i, $i+1-length($input));	#making substrings of each letter of the input string and storing it in an array 
}

#Reading the arguments --count and length
$count = $ARGV[0];
$length = $ARGV[1];

#creating an empty array to store our random string
@random_string;

#storing the no.of letters used in the input data, i.e, size of alphabet array 
$no_of_letters = @alphabet;

#Declaring variables used in random string generation 
$prev_index = 0;		#storing the previous random number, generated for index of the alphabet array, to check if it's going to be repeated
$i = 0;

#Running the while loop until reaching the required length of the random string
while( @random_string < $length )
{
		#1st random number generation for 'index' in the string of alphabet stored in the data file to be repeated.
		$index = int(rand($no_of_letters));
		if( "$alphabet[$prev_index]" ne "$alphabet[$index]" )		#checking if the same alphabet is used previously or not
		{
			#2nd random number generation for bounding the number of repetitions, i.e, 'frequency'.
			$freq = int(rand($count));
			if( $freq == 0 ) { $freq++; }			#frequency should not be zero...
			
			for( $j = 0 ; $j < $freq ; $j++ )
			{
				$random_string[$i] = $alphabet[$index];
				chomp $random_string[$i];
				$i++;
			}
		}
		$prev_index = $index;						#assigning prev index as current index for next checking
}
chomp @random_string;								#removing the newline character at the end of the string

#Printing the generated random string
for( $i = 0 ; $i < $length ; $i++ )
{
	print "$random_string[$i]";
}
print "\n";
