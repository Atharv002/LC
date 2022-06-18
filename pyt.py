#Question 38: Count and Say
class Solution(object):
    def countAndSay(self, n):
        if n==1:
            return "1"
        else:
            str1 = self.countAndSay(n-1)
            str2=""
            count=1
            for i in range(0,len(str1)):
                if i!=len(str1)-1:
                    if str1[i+1]==str1[i]:
                        count+=1
                    else:
                        str2+=str(count)
                        str2+=str(str1[i])
                        count=1
                else:
                    str2+=str(count)
                    str2+=str(str1[i])
            return str2



#Question 28: Implement strStr()
class Solution(object):
    def strStr(self,haystack,needle):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                j=0
                k=i
                countr=0
                while j<len(needle):
                    if haystack[k]==needle[j]:
                        countr+=1
                    else:
                        break
                    k+=1
                    j+=1
                if countr==len(needle):
                    return i
        return -1


