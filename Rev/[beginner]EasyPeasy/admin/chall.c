#include <stdio.h>
#include <string.h>

int main(){
    
    int pp[] = {4991, 4963, 4981, 4940, 4989, 4930, 4866, 4864, 4968, 4931, 4871, 4871, 4968, 4866, 4870, 4954, 4935, 4955, 4868, 4968, 4870, 4864, 4968, 4870, 4866, 4938};

    char pssd[] = "SuperSecretPassword";
    char buf[60];
    
    printf("Please enter the password: ");

    scanf("%59s",buf);

    if(strcmp(buf,pssd) == 0){
        for(int i = 0; i < 26; i ++){
            printf("%c",pp[i] ^ 0x1337);
        }
    }else{
        puts("Look again");
    }

    return 0;
}

