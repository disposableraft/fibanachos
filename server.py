import redis
from flask import Flask
import lib

app = Flask(__name__)

rc = redis.Redis(host='redis.default.svc.cluster.local', port=6379, decode_responses=True)
f = lib.Fibonacci(rc)
pr = lib.Prime(rc)

@app.route('/<number>')
def index(number):
    number = int(number)
    out = ["🍄" if pr.is_prime(n) else "🌲" for n in range(1, f.fib(number) + 1)]
    return ' '.join(out) + "\n"

if __name__ == "__main__":
    app.run(debug=True)