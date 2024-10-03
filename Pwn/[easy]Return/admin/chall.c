#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

void win(){
    puts("You sure did win");
    system("/bin/sh");
}

int main(){
    char buf[0x20];

    puts("Do whatever you want --__--");
    scanf("%s",buf);

    return 0;

}
