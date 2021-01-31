#1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


#7. Reverse Integer
class Solution:
    def reverse(self, x: 'int') -> 'int':
        maxint = 2147483649
        minint = -2147483648
        ans = int(str(abs(x))[::-1])
        return ans * (abs(x)//x) if minint < ans < maxint and ans else 0
    
#9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = int(str(abs(x))[::-1])
        return True if ans==x else False
####################################
class Solution:
    def isPalindrome(self, x):
        return False if x < 0 else x == int(str(x)[::-1])

#13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = { 'I':1, 'V':5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for i in range(len(s)-1):
            if(mappings[s[i]]<mappings[s[i+1]]):
                total -= mappings[s[i]]
            else:
                total += mappings[s[i]]
            
        return(total+mappings[s[-1]])
####################################
class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = { 'I':1, 'V':5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for i in range(len(s)-1):
             if((s[i]=='I' and s[i+1]=='V') or (s[i]=='I' and s[i+1]=='X')):
                 total-=1
             elif((s[i]=='X' and s[i+1]=='L') or (s[i]=='X' and s[i+1]=='C')):
                 total-=10
             elif((s[i]=='C' and s[i+1]=='D') or (s[i]=='C' and s[i+1]=='M')):
                 total-=100
            else:
                total += mappings[s[i]]
            
        return(total+mappings[s[-1]])
    
#14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        for i in range(min(map(len, strs))):
            ch = strs[0][i]
            if all(s[i] == ch for s in strs):
                prefix += ch
            else:
                break
        return prefix


#20. Valid Parentheses
class Solution:
    def isValid(self, s):
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []
############################################
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 if l2 is None else l2
        else:
            sm, lg = sorted((l1, l2), key=lambda l: l.val)
            sm.next = self.mergeTwoLists(sm.next, lg)
            return sm
#####################################
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        for idx in range(len(nums)-1,0,-1): ---In the for loop, the index will change if you delete an element. So it should be traversed from back to front----
            if nums[idx] == nums[idx-1]:
                del nums[idx]
        return len(nums)
#########################################
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = 1 ---Might not be correct for other senarios---
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ +=1
        return len_

27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                del nums[i]
        return  len(nums)

28. Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1 
###################################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1

35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i==target:
                return nums.index(i)
        nums.insert(0,target)
        return sorted(nums).index(target)
#####################################
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        copy_nums = nums
        try:
            return nums.index(target)
        except:
            copy_nums.append(target)
            return sorted(copy_nums).index(target)
   
38. Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            s, curr_digit, count = "", result[0], 1
            for digit in result[1:]:
                if digit == curr_digit:
                    count += 1
                else:
                    s += str(count) + curr_digit
                    curr_digit, count = digit, 1
            result = s + str(count) + curr_digit
        return result
        
53. Maximum Subarray        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=max(nums[i-1]+nums[i],nums[i])
        return max(nums)
#####################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        allmax = nums[0]
        curmax = nums[0]
        for i in nums[1:]:
            if curmax + i > i:
                curmax = curmax + i
            else:
                curmax = i
            if curmax > allmax:
                allmax = curmax
                
        return allmax  
        

58. Length of Last Word        
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
##########################################
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
		return 0 if len(s.split())==0 else len(s.split()[-1])

66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:     
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            digits[i] = 0        
        return [1] + digits
################################################
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            i=-1
            while -i <= len(digits) and (digits[i] == 9):
                digits[i] = 0
                i -= 1
            if i+1 == -len(digits):
                digits = [1] + digits
            else:
                digits[i] += 1
        return digits

67. Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = int(a,2) + int(b,2) # strings both in binary. converted to decimal and added
        return bin(ans)[2:] # converted result back to binary '0bxxxx' and sliced for format

--- Note: bin of any number returns binary---
--- for ex: - bin(2) = '0b10'---

69. Sqrt(x)
from numpy import sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
#################################
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** (1/2))

70. Climbing Stairs
class Solution:
def climbStairs(self, n: int) -> int:
    no_steps = [1]  * (n+1)
    no_steps[1] = 1    
    for i in range(2,n+1):
        no_steps[i] = no_steps[i-1] + no_steps[i-2]       
    return no_steps[n]
################################
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        c1, c2, c3 = 0, 1, 2
        while n > 2:
            c1, c2 = c2, c3
            c3 = c1 + c2
            n -= 1
        return c3
###########################
class Solution:
    def climbStairs(self, n):
        a,b = 1,0
        for _ in range(n):
            a,b = a+b,a
        return a

83. Remove Duplicates from Sorted List
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur=head
        while cur:
            while cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            cur=cur.next
        return head

88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()
############################
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums2)):
            nums1.pop() # To remove the trailing zeros
        nums1.extend(nums2)
        nums1.sort()

