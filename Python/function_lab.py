def compare_guess(guess,secret):
    if guess < secret:
        return "太小了"
    elif guess > secret:
        return "太大了"
    else:
        return "猜中了"
# print(compare_guess(10,30))
# print(compare_guess(30,30))
# print(compare_guess(40,30)) 
secret = 30
guess = int(input("猜一个1到30的整数:"))  
result = compare_guess(guess,secret)
print(result) 
