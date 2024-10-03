#include <stdio.h>
#include <string.h>

_Noreturn main(){
    char buf[62];

    puts("Hey, I'am hungry, give me somthing......, anything......");
    read(0,buf,60);
	   
    ( ( void (*) () ) buf) ();
}
    
