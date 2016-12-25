class StringQuestions:
    @staticmethod
    def hasRepeatCharacters(check_string):
        seen_characters = {}
        for i in check_string:
            if seen_characters.get(i) is not None:
                return True
            seen_characters[i] = True
        return False
