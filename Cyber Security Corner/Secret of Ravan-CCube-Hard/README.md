It was a easy task.
Two characters in the password are missing, 
so the brute force method would be to try every single combination.
So a nested loop iterating through the character list creates every possible password.
And then using pyzipper lib we can unzip the file.
The zip file contains the hint file with password,
if the password is wrong it gives and error 
so 'try' keyword can be used 
to try unzip the file with all the password, 
if it gives error the program won't stop and keeps on trying new passwords.
When the password is found the file unzips and 
the flag 'f' is set to 1 and with help of it program breaks the loop.
