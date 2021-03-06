class StringQuestions:
    @staticmethod
    def hasRepeatCharacters(check_string, space_efficient=False):
        """
        Returns true if and only if the input string has repeat characters.

        :param space_efficient:
         If true, this method will run in polynomial time and take constant space.
         If false, this method will run in linear time and take linear space.
        :param check_string:
         The string to check for repeat characters
        :return:
         True if and only if check_string has duplicate characters
        """
        if space_efficient:
            return StringQuestions._spaceEfficientHasRepeatCharacters(check_string)

        seen_characters = {}
        for i in check_string:
            if seen_characters.get(i) is not None:
                return True
            seen_characters[i] = True
        return False

    @staticmethod
    def _spaceEfficientHasRepeatCharacters(check_string):
        """
        Returns true if and only if check_string contains duplicate characters.

        Runs in polynomial time, namely O(n^2)

        :param check_string:
         The string to check for duplicate characters
        :return:
         True if and only if check_string has duplicate characters
        """
        for i in range(len(check_string)):
            for j in range(len(check_string)):
                if check_string[i] == check_string[j] and i != j:
                    return True
        return False

    @staticmethod
    def checkPermutation(string1, string2):
        """
        Given two strings, returns true if and only if one string is a permutation
        of the other. Runs in linear time, takes up linear space.

        :param string1:
         The first string to compare
        :param string2:
         The second string to compare
        :return:
         True if and only if the first string is a permutation of the second string.
        """
        string1_content = {}
        # Hash the first string
        for i in string1:
            if string1_content.get(i) is None:
                string1_content[i] = 1
            else:
                string1_content[i] += 1

        # For each character in the section string, search for it
        for i in string2:
            if string1_content.get(i) is None:
                return False
            string1_content[i] -= 1

        # Make sure every character in the first string had a matching character in the second string
        for key, value in string1_content.items():
            if value != 0:
                return False
        return True

    @staticmethod
    def urlify(target, size):
        """
        Given an array of characters with spaces, expands those spaces into %20. Size is the length
        of the array, after this expansion. Runs in linear time, constant space consumption.

        :param target:
        The array to expand
        :param size:
        The size of the string in the array without any trailing spaces, after the expansion
        :return:
        The expanded version of the target array.
        """
        seen_index = size - 1
        copy_index = size - 1

        # Find the beginning of the string to expand
        for i in range(size):
            if target[size - 1 - i] != ' ':
                seen_index = size - 1 - i
                break

        expanded_space = "%20"
        # Replace the spaces in the string to explain with the appropriate spacer
        for i in range(seen_index + 1):
            if target[seen_index] != ' ':
                target[copy_index] = target[seen_index]
                copy_index -= 1
                seen_index -= 1
            else:
                seen_index -= 1
                for j in range(3):
                    target[copy_index - 2 + j] = expanded_space[j]
                copy_index -= 3

        return target
