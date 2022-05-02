class Memo:
    def __init__(self, redis_client, key_prefix=""):
        self.client = redis_client
        self.key_prefix = key_prefix
    
    def set(self, k, v):
        self.client.set(f'{self.key_prefix}:{k}', v)
        return self.get(k)
    
    def get(self, k):
        return self.client.get(f'{self.key_prefix}:{k}')

class Prime(Memo):
    def __init__(self, redis_client):
        Memo.__init__(self, redis_client, 'prime')
    
    def is_prime(self, n) -> bool:
        if n <= 1:
            return False
        if self.get(n):
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        self.set(n, 1)
        return True

class Fibonacci(Memo):
    def __init__(self, redis_client):
        self.client = redis_client
        Memo.__init__(self, redis_client, 'fib')

        self.set(0, 0)
        self.set(1, 1)
    
    def get(self, n) -> int:
        v = Memo.get(self, n)
        if v is None:
            return None
        return int(v)
    
    def set(self, n, v) -> int:
        return int(Memo.set(self, n, v))

    def fib(self, n) -> int:
        if (v := self.get(n)) is not None:
            return v
        else:
            f = self.fib(n-1) + self.fib(n-2)
            return self.set(n, f)