# names are references
biz = 100
baz = biz

biz = 200 
print(f"\nbiz = {biz}")
print(f"baz = {baz}")


# the "waffa" object will have two references pointing to one object
biz = "waffa"
baz = biz

# inside, this will decrements the number reference counters so only 
# baz points to "waffa"
biz = "glitz" 

print(f"\nbiz = {biz}")
print(f"baz = {baz}")