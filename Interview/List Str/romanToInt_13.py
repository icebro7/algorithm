class Solution:
    def romanToInt(self, s: str) -> int:
        L = len(s)
        S = 0

        def romannumber(i: str):
            match i:
                case "I":
                    return 1
                case "IV":
                    return 4
                case "V":
                    return 5
                case "IX":
                    return 9
                case "X":
                    return 10
                case "XL":
                    return 40
                case "L":
                    return 50
                case "XC":
                    return 90
                case "C":
                    return 100
                case "CD":
                    return 400
                case "D":
                    return 500
                case "CM":
                    return 900
                case "M":
                    return 1000

        i = 0
        while i < L:
            z = romannumber(s[i])
            if i < L - 1 and romannumber(s[i]) < romannumber(s[i + 1]):
                res = s[i] + s[i + 1]
                S += romannumber(res)
                i += 2
            else:
                S += romannumber(s[i])
                i += 1

        return S


if __name__ == '__main__':
    s = "MCMXCIV"
    print(Solution().romanToInt(s))
