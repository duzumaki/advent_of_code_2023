#include <stdio.h>

int main() {
    FILE *file = fopen("test.txt", "r");

    int number;

    char buffer[128];

    int game_no;
    char buffer2[128];


        while (fscanf(file, "%s %d: %d %s", buffer2, &game_no, &number, buffer) == 2) {
            printf("%s\n", buffer);
        }


    fclose(file);
    return 0;
}
