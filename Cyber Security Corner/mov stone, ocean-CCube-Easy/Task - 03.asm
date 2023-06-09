SYS_EXIT  equ 1
SYS_READ  equ 3
SYS_WRITE equ 4
STDIN     equ 0
STDOUT    equ 1

segment .data 

   m1 db "How many stones required per kilometer:", 0xA,0xD 
   l1 equ $- m1 

   m2 db "How many kilometers to build:", 0xA,0xD 
   l2 equ $- m2 

   m3 db "The amoutnof stones required: "
   l3 equ $- m3

segment .bss

   num1 resb 2 
   num2 resb 2 
   res resb 1  

section	.text
   global _start   
	
_start:            
   mov eax, SYS_WRITE         
   mov ebx, STDOUT         
   mov ecx, m1         
   mov edx, l1 
   int 0x80                

   mov eax, SYS_READ 
   mov ebx, STDIN  
   mov ecx, num1 
   mov edx, 2
   int 0x80            

   mov eax, SYS_WRITE        
   mov ebx, STDOUT         
   mov ecx, m2          
   mov edx, l2         
   int 0x80

   mov eax, SYS_READ  
   mov ebx, STDIN  
   mov ecx, num2 
   mov edx, 2
   int 0x80        

   mov eax, SYS_WRITE         
   mov ebx, STDOUT         
   mov ecx, m3          
   mov edx, l3         
   int 0x80

   
   mov eax, [num1]
   sub eax, '0'
	
   mov ebx, [num2]
   sub ebx, '0'

   
   imul eax, ebx
   
   add eax, '0'

   mov [res], eax

   mov eax, SYS_WRITE        
   mov ebx, STDOUT
   mov ecx, res         
   mov edx, 1        
   int 0x80

exit:    
   
   mov eax, SYS_EXIT   
   xor ebx, ebx 
   int 0x80