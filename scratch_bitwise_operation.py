import random

# okay this is how we are gonna check valid directions later

valid_nums = [1,2,4,8]

random_number = valid_nums[random.randint(0,len(valid_nums)-1)]
random_binary = bin(random_number)

valid_dir_bin = bin(0b1001)
valid_dir_int = int(0b1001)

print(f"random_number: {random_number}, random_binary: {random_binary} & {valid_dir_bin}")
print(bin(valid_dir_int & random_number))


