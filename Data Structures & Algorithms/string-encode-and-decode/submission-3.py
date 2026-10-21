class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += f"{len(string)}#{string}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ix = 0
        decoded_str = []
        while ix < len(s):
            str_len = ""
            while s[ix] != '#':
                str_len += s[ix]
                ix += 1
            str_len = int(str_len)
            if str_len == 0:
                decoded_str.append("")
                ix += 1
            else:
                ix += 1
                decoded_str.append(
                    s[ix:ix+str_len]
                )
                ix += str_len
        return decoded_str