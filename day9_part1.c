#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>




int* split(char *line, int *nums_size) {
    *nums_size = 0;
    char* line_copy = strdup(line);

    char* token = strtok(line_copy, " ");
    int* nums = (int*)malloc(1000000000*sizeof(int));
    int i = 0;

    while (token != NULL) {
        nums[i] = atoi(token);
        token = strtok(NULL, " ");
        i++;
    }
    *nums_size = i;

    free(line_copy);

    return nums;
}

int* get_sequence(int* nums, int size, int *sequence_sum, int* sequence_size) {
    /*
    I originally tried to be clever and add 
    the nums to be like "if the line equals the sum of 0 that means
    all the nums are 0" but i just realised 

    something like 1 -1 1 -1 would be considered "all 0s" 💀
    I should check each num is 0. only realised this when i switched to 
    the python implementation and got bored of trying to fix the c one.

    */
    *sequence_sum = 0;
    *sequence_size = 0;
    int* sequence = (int*)malloc(size*sizeof(int));

    for (int i = 1; i < size; i++) {
        *sequence_sum += nums[i];
        sequence[i-1] = nums[i]-nums[i-1];
        *sequence_size += 1;
    }
    return sequence;
}

int main() {
    FILE* file = fopen("test.txt", "r");

    size_t size = 120;
    char *line = NULL;
    ssize_t read;

    int nums_size;

    int* prev_sequence = NULL;
    size_t prev_nums_size;
    size_t prev_sequence_sum = 0;
    size_t sequence_sum = 0;

    int last_nums_in_each_sequence[102400];

    int TOTAL = 0;

    while ((read = getline(&line, &size, file)) != -1) {
        int line_total = 0;
        int number_of_sequences = 0;
        int sequence_size = 0;
        int sequence_sum = 0;

        // 0   3   6   9  12  15
        int* sequence = split(line, &sequence_size);

        // the following sequences
        while (sequence_sum != 0) {
            sequence = get_sequence(sequence, sequence_size, &sequence_sum, &sequence_size);
            number_of_sequences++;
            last_nums_in_each_sequence[number_of_sequences] = sequence[sequence_size-1];
        }

        for (int i=number_of_sequences-1; i >= 0; i--) {
            line_total += last_nums_in_each_sequence[i];
        }
        TOTAL += line_total;

        free(sequence);

    }
    printf("%d", TOTAL);

    return 0;
}   

