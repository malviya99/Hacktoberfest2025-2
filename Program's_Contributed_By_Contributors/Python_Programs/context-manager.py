import time
from functools import wraps

# ========== CUSTOM CONTEXT MANAGER ==========
class Timer:
    """
    Context manager that measures execution time
    Use it with 'with' statement - super clean!
    Automatically handles setup and cleanup
    """
    def __init__(self, name="Code block"):
        self.name = name
    
    def __enter__(self):
        """Called when entering 'with' block"""
        self.start = time.time()
        print(f"⏱️  Starting: {self.name}")
        return self  # This is what 'as' captures
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block (even if error!)"""
        self.elapsed = time.time() - self.start
        print(f"✅ Finished: {self.name} in {self.elapsed:.4f}s\n")
        return False  # Don't suppress exceptions


# ========== DECORATORS WITH ARGUMENTS ==========
def repeat(times):
    """
    Decorator that runs a function multiple times
    Shows off closure magic - the inner functions remember 'times'!
    """
    def decorator(func):
        @wraps(func)  # Preserves original function's name and docstring
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"  🔁 Run {i+1}/{times}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


def cache_result(func):
    """
    Memoization decorator - caches function results
    Super useful for expensive computations!
    """
    cache = {}  # Closure variable - persists between calls
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"  💾 Cache hit for {args}")
            return cache[args]
        print(f"  🔧 Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


# ========== WALRUS OPERATOR (:=) ==========
def process_data(numbers):
    """
    Shows off the walrus operator - assign AND use in same expression!
    Available since Python 3.8 - makes code more concise
    """
    # Old way would need two lines
    if (n := len(numbers)) > 5:  # Assigns AND checks in one line!
        print(f"Processing large list: {n} items")
        return sum(numbers) / n
    return 0


# ========== F-STRING DEBUGGING (Python 3.8+) ==========
def debug_info(x, y):
    """F-string debugging - the = makes it print var name + value!"""
    result = x * y
    print(f"{x=}, {y=}, {result=}")  # Super handy for debugging!
    return result


# ========== DEMO TIME! ==========
if __name__ == "__main__":
    print("🐍 Python Modern Features Showcase\n")
    
    # Context Manager Demo
    print("1️⃣  CONTEXT MANAGER:")
    with Timer("Sum calculation"):
        total = sum(range(1000000))
    
    # Decorator Demo
    print("2️⃣  DECORATOR WITH ARGUMENTS:")
    @repeat(3)
    def greet(name):
        return f"Hello, {name}!"
    
    greet("Python")
    
    # Memoization Demo
    print("\n3️⃣  CACHING DECORATOR:")
    @cache_result
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(f"Fib(5) = {fibonacci(5)}")
    print(f"Fib(5) again = {fibonacci(5)}")  # Uses cache!
    
    # Walrus Operator Demo
    print("\n4️⃣  WALRUS OPERATOR (:=):")
    process_data([1, 2, 3, 4, 5, 6, 7])
    
    # F-string Debug Demo
    print("\n5️⃣  F-STRING DEBUGGING:")
    debug_info(12, 34)
    
    print("\n🎉 All features demonstrated!")
