def compare_guess(guess,secret):
    if guess < secret:
        return "太小了"
    elif guess >secret:
        return "太大了"
    else:
        return "猜中了"

guesses = [10,30,40,25]
secret = 30

for guess in guesses:
    result =compare_guess(guess,secret)
    print(guess,result)