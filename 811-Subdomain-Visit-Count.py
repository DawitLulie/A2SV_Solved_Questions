from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = Counter()
        for domain in cpdomains:
            arr = domain.split()
            num = int(arr[0])
            cur =  ""
            i = len(domain) - 1

            while domain[i] != " ":
                if domain[i] == ".":
                    dic[cur] += num
                cur = domain[i] + cur
                i -= 1
            dic[cur] += num

        result = []
        for key, val in dic.items():
            result.append(str(val) + " " + key)

        return result




        