#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(){

    int a[] = {127, 99, 117, 76, 6, 67, 104, 6, 2, 104, 93, 66, 2, 0, 104, 79, 7, 69, 104, 81, 7, 69, 104, 69, 4, 3, 91, 74};
    char buf[40];
    
    puts("Password please: ");
    
    if(read(0, buf, 39)-1 != 28){
        puts("Wrong");
        exit(1731);
    }

    for(int i = 0; i < 28; i++){
        if((buf[i] ^ 0x37) != a[i]){
            puts("Wrong");
            exit(1337);
        }
    }

    puts("Correct");

    return 0;
}

