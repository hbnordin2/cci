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
