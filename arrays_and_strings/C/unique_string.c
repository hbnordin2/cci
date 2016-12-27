#include "utilities.h"

#define ASCII_SIZE 128

bool unique_characters(char*);

int main(int argc, char** argv) {
    if(argc != 2) {
        fprintf(stderr, "Usage: ./unique_characters <string>\n");
        exit(1);
    }
    unique_characters(argv[1]);
}

/**
 * @brief Prints and returns true if and only if every character in the input
 * string is unique
 *
 * @param toInspect
 *  The string to inspect
 *
 * @return True if and only if every character int he input is unique
 */
bool unique_characters(char* toInspect) {
    int seenCharacters[ASCII_SIZE];
    memset(seenCharacters, 0, sizeof(seenCharacters));
    for(int i=0; i<strlen(toInspect); i++) {
        int hashValue = toInspect[i] % ASCII_SIZE;
        if(seenCharacters[hashValue] > 0) {
            printf("False\n");
            fflush(stdout);
            return true;
        }
        seenCharacters[hashValue] += 1;
    }
    printf("True\n");
    fflush(stdout);
    return true;
}
