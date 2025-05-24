class Parallax:

    @classmethod
    def shift(cls, str1, str2) -> str:
        if len(str1) < 3 or len(str2) < 3:
            return str1

        start_inclusive = 0
        end_exclusive = 3
        final_str = str1
        pos = "start"

        while end_exclusive <= len(str1):
            substring = str1[start_inclusive:end_exclusive]
            if cls._is_decreasing(substring) and substring in str2:

                final_str = cls._add_substring(substring, final_str, pos)
                pos = "start" if pos == "end" else "end"

            start_inclusive += 1
            end_exclusive += 1

        return final_str

    @staticmethod
    def _is_decreasing(substr: str) -> bool:
        previous_ascii = 9999  # ascii wont go above this num
        for char in substr:
            current_ascii = ord(char)
            if current_ascii < previous_ascii:
                previous_ascii = current_ascii
            else:
                return False

        return True

    @staticmethod
    def _add_substring(substring, current_string, position) -> str:
        if position == "start":
            return substring + current_string
        if position == "end":
            return current_string + substring
        raise ValueError('Position must be either "start" or "end"')
