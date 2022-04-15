class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None
        if dividend == 0:
            return 0
        sign = (divisor < 0) ^ (dividend < 0)
        dvs = abs(divisor)
        dve = abs(dividend)
        
        res = 0
        digit = 0
        
        while dvs <= dve>>1:
            dvs <<=1
            digit += 1
        """print "dvs:", dvs, " digit:", digit"""
        
            
        while digit >= 0:
            if dve >= dvs:
                res += 1 << digit
                dve -= dvs
            dvs >>= 1
            digit -= 1
            """print "dvs:", dvs, " digit:", digit, "res:", res"""
        res = -res if sign else res
        return max(min(res, 2**31-1), -2**31)
