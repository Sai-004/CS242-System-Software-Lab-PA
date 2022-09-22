#Execution command for question-1: bash backup.scr filenames.txt backup_files/

#Execution command for question-2: perl Random_String_Generator.pl ARGV[0] ARGV[1]
																
							//while executing in terminal ARGV[0] and ARGV[1] are the arguments 'count' and 'length' respectively

-----------------------------------------------------   Question-1   -----------------------------------------------------------------------------------------
Input of list of files	: filenames.txt			
Backup Directory	: backup_files
Bash script		: backup.scr

Explanation:	#!/bin/bash is the shebang line which tells the system to execute the code using 'Bash Shell'.
		Filename and Backup_Dir are taken as arguments and are the list of files to be backed up 
		and the directory to stored the backup files respectively.
		The next few lines in the script are the validation check.
		We need to enter exactly 2 arguments in the execution command.
		In this Validation and Testing of Script part,the code checks for no.of arguments enetered,
								  if the file exists or not, 
								  if the directory exists or not or 
								  it's a file but not directory.
		After the validation check, if the entered arguments are exactly 2 and the file and directory exists, then the backing up of files part runs.
		while loop reads the file names from the input file 
		backup_filename=$file_name.bak -- this line adds the extension .bak for the backup files
		backup file is created in the backup_files directory using touch command
		cp command is used to copy the file contents to the backup files
		done < $1 -- this lines is the end of the while loop
				
Checking after affects: After executing the command, the given files will be backed up and to check the contents being copied or not,
			rename the backedup files with appropriate extension (.txt) and check its contents.

-----------------------------------------------------   Question-2   -----------------------------------------------------------------------------------------
Input file 	: input.txt
PERL code  	: Random_String_Generator.pl

Explanation	: #!/bin/perl is the line which tells the system to execute using PERL script.
		  open( input , "<" , <input.txt> );  --this line opens and reads the data from the input file.
		  Count and Length are passed as arguments in the execution command and are read in code by $ARGV[0] and $ARGV[1].
		  I stored the input data in the array @alphabet and generated the random string @random_string.
		  While loop runs until reaching the required length.
		  int(rand($count)) and int(rand($no_of_letters)) are the random number generating functions in the code.
		  The previously generated index of the letter lo be repeated is stored in a variable "$prev_index", 
		  	so as to make sure that next random letter should not be the same one.
		  If the random frequency generated equals to 0 then, I added 1 to it as we cannot make the count 0.
		  After generating the required random string, chomp command is used to make sure to remove the newline character at the end of the string
		  The random number is generated with the required conditions and printed at the end of the code.
