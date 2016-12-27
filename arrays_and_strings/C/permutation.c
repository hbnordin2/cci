#include "utilities.h"

void argument_check(int, char**);
bool check_permutation(char*, char*);

int main(int argc, char** argv) {
    argument_check(argc, argv);
    check_permutation(argv[1], argv[2]);
}

void argument_check(int argc, char** argv) {
    if(argc != 3) {
        fprintf(stderr, "Usage: argument_check <string1> <string2>\n");
        exit(1);
    }
}

/**
 * @brief Prints and returns true if the two input strings are permutations
 * of one another.
 *
 * @param word1
 *      The first input word to compare against the second
 *
 * @param word2
 *      The second input word to compare against the first
 *
 * @return True if and only if the two input words are permutations of one 
 * another
 */
bool check_permutation(char* word1, char* word2) {
    int seenValues[128];
    memset(seenValues, 0, sizeof(seenValues));

    for(int i=0; i<strlen(word1); i++) {
        int hashValue = word1[i] % 128;
        seenValues[hashValue] += 1;
    }

    for(int i=0; i<strlen(word2); i++) {
        int hashValue = word2[i] % 128;
        seenValues[hashValue] -= 1;
    }

    for(int i=0; i<128; i++) {
        if(seenValues[i] != 0) {
            printf("False\n");
            fflush(stdout);
            return false;
        }
    }
    printf("True\n");
    fflush(stdout);
    return true;
}
