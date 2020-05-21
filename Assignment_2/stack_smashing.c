#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int virus(void) {
        return 1;
}
int overflow(void) {
        int arr[3];
        arr[0] = 12;
        arr[1] = 10;
        arr[2] = 18;
        arr[3] = 5;
        arr[4] = 0x00005555;
        arr[5] = 0x55555125;

        return 1;
}

int main() {
        int i;
        i = 14;
        overflow();
        
        return 0;
}
