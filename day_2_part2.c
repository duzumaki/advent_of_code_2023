#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int CUBED_SUM = 0;

int main() {
    FILE *file = fopen("test.txt", "r");
    int token_count;

    int number;
    char buffer[128];

    int cubed_sum = 0;


    while (fscanf(file, "%s %d:", buffer, &number) == 2) {
        int game_no = number;

        int red = 0;
        int green = 0;
        int blue = 0;

        while (fscanf(file, "%d %s", &number, buffer) == 2) {
            // check the first character only so you don't need to 
            // bother parsing the rest of the string. e.g "blue,", "red;", etc
            if (buffer[0] == 'r' && number > red) {
                red = number;
            } 
            else if (buffer[0] == 'g' && number > green) {
                green = number;
            }
            else if(buffer[0] == 'b' && number > blue) {
                blue = number;
            }
        }

        int product = red * green * blue;
        cubed_sum += product;
    }

    fclose(file);
    printf("%d", cubed_sum);
    return 0;
}


