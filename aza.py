import time

start = time.time()

now = time.localtime(time.time())

print(" hello world ")

print(time.asctime(now))

print(time.strftime("%Y-%m-%d %H:%M", now))
end = time.time()
print(end - start)