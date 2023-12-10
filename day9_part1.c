#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>




int* split(char *line, int *nums_size) {
    *nums_size = 0;
    char* line_copy = strdup(line);

    char* token = strtok(line_copy, " ");
    int* nums = (int*)malloc(10000*sizeof(int));
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

int* get_sequence(int* nums, int size, int* sequence_size) {
    /*
    I originally tried to be clever and add 
    the nums to be like "if the line equals the sum of 0 that means
    all the nums are 0" but i just realised 

    something like 1 -1 1 -1 would be considered "all 0s" 💀
    I should check each num is 0. only realised this when i switched to 
    the python implementation and got bored of trying to fix the c one.

    */
    *sequence_size = 0;
    int* sequence = (int*)malloc(size*sizeof(int));

    for (int i = 1; i < size; i++) {
        sequence[i-1] = nums[i]-nums[i-1];
        *sequence_size += 1;
    }
    return sequence;
}

bool all_zeroes(int* nums, int size) {
    for (int i=0; i < size; i++) {
        if (nums[i] != 0) {
            return false;
        }
    }
    return true;
}

void print(int* nums, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d\n", nums[i]);
    }
}

int main() {
    FILE* file = fopen("test.txt", "r");

    size_t size = 120;
    char *line = NULL;
    ssize_t read;

    int nums_size;

    int last_nums_in_each_sequence[102400];

    int TOTAL = 0;

    while ((read = getline(&line, &size, file)) != -1) {
        int number_of_sequences = 0;
        int sequence_size = 0;

        int* sequence = split(line, &sequence_size);
        number_of_sequences+=1;

        while (!all_zeroes(sequence, sequence_size)) {
            last_nums_in_each_sequence[number_of_sequences] = sequence[sequence_size-1];
            sequence = get_sequence(sequence, sequence_size, &sequence_size);
            number_of_sequences += 1;
        }


        int line_total = 0;
        for (int i=0; i < number_of_sequences; i++) {
            line_total += last_nums_in_each_sequence[i];
        }
        TOTAL += line_total;

    }
    printf("%d", TOTAL);

    return 0;
}   

