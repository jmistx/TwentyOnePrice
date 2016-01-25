import math

def spread(n, k, i):
    return (n // k) + (1 if i < (n % k) else 0)
    
def check(n, k):
    buckets = [ spread(n,k,i) for i in range(k)] 
    print ( buckets )
    buckets_sum = sum(buckets)
    print ( buckets_sum == n)
    if buckets_sum != n:
        raise Exception(n)
    return buckets_sum
    
def total_check():
    for j in range(100):
        buckets_sum = check (j, 10)
        

def spread_with_limit(n, k, buckets, conditions):
    # n > 0
    # k > 0
    # len(buckets> == k
    # len(conditions) == k
    total = n
    current = 0
    increments_per_pass = 0
    while total > 0:
        if current == k:
            if increments_per_pass == 0:
                raise Exception("can't achieve conditions")
            current = 0
            increments_per_pass = 0
        if conditions[current] <= buckets[current]:
            current += 1
            continue
        buckets[current] += 1
        total -= 1
        current += 1
        increments_per_pass += 1
        
def caluclate_prices(p1, p21, n=21):
    if p21 < p1 + n - 1:
        raise Exception('С такими ограничениями будет товар стоимостью 0')
    if p1 * 21 < p21:
        raise Exception('С такими ограничениями стоимость последующих товаров будет выше первого')
    prices = [p1] + [1] * (n - 1)
    total_amount = p21 - p1 - (n - 1)
    weights = [ 0,
                0.110917031,
                0.095196507,
                0.08209607,
                0.071615721,
                0.063755459,
                0.05720525,
                0.051965066,
                0.048034935,
                0.045414848,
                0.04279476,
                0.040174673,
                0.037554586,
                0.036244542,
                0.034934498,
                0.033624455,
                0.03231442,
                0.031004367,
                0.029694324,
                0.028384280,
                0.027074236,
                ]
                
    increase = [0] * n
    
    for i in range(len(prices)):
        increase[i] = int(math.floor(weights[i] * total_amount))
        prices[i] += increase[i]
    
    total_amount -= sum(increase)
    return prices
        
#input_buckets = [0]
#spread_with_limit(1, 1, input_buckets, [100])
#print(input_buckets)
print(caluclate_prices(300, 2610))
