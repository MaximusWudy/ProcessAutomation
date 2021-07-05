ItemsInCart = 0
# 2 items will be added to cart

# 1st way: Use 'rise Exception' keywords
if ItemsInCart != 2:
    # raise Exception("Products Cart count not matching")
    pass

# 2nd way: use assert(), condition must be True
# assert(ItemsInCart == 2) # will return AssertionError

# Try.. Catch...: when exception raised in try clause, send control to catch block
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("Some how i reached this block because there is failure in try block")

# if you want to know Python original error msg
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

# finally: only works with try...except
# no matter fail or not, execute anyway
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning up resources")