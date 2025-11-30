import math

class AnalyzeNumber:

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def find_prime_number(self, n: list) -> list:
        return [x for x in n if self.is_prime(x)]
 
    def is_perfect(self, n: int) -> bool:
        divisors = [i for i in range(1, n) if n % i == 0]

        return sum(divisors) == n
    
    def find_perfect_number(self, n: list) -> list:
        return [x for x in n if self.is_perfect(x)]
    
    def is_armstrong(self, n: int) -> bool:
        digits = str(n)
        power = len(digits)
        total = sum(int(d)**power for d in digits)
        
        return total == n and n >= 10
    
    def find_armstrong_number(self, n: list) -> list:
        return [x for x in n if self.is_armstrong(x)]
    
    def analyze_num_range(self, n: list) -> dict:
        rs = {}
        pr = 0
        pf = 0
        am = 0
        for i in n:
            if self.is_prime(i):
                #print(f"Number {i} is Prime")
                pr += 1
            
            if self.is_perfect(i):
                #print(f"Number {i} is Perfect")
                pf += 1

            if self.is_armstrong(i):
                #print(f"Number {i} is Armstrong")
                am += 1

        print(f"Total Prime = {pr}, Perfect = {pf}, Armstrong = {am}")

        rs = {"Prime": pr, "list_prime": self.find_prime_number(n),
              "Perfect": pf, "list_perfect": self.find_perfect_number(n),
              "Armstrong": am, "list_armstrong": self.find_armstrong_number(n)}

        return rs

#an = AnalyzeNumber()

#ls = list(range(1, 1000))
#rs = an.analyze_num_range(ls)
#print(rs)
#print(an.find_armstrong_number(ls))
#print(an.find_perfect_number(ls))
#print(an.find_prime_number(ls))
#print(an.format_analysis())