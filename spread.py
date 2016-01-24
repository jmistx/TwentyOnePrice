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
    // n > 0
    // k > 0
    // len(buckets> == k
    // len(conditions) == k
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
        
input_buckets = [0]
spread_with_limit(1, 1, input_buckets, [100])
print(input_buckets)