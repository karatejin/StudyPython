## Fizz Buzz

## 3으로 나누어 떨어질때 Fizz

## 5로 나누어 떨어질때 Buzz

## 둘다 포함되면 FizzBuzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 !=0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 !=0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    else:
        print(number)

## 더 좋은 방법

for number in range(1,101):
    if number % 3 == 0 and number % 5 ==0: ## 여기를 먼저 시행한다음 elif 을 시행하기 때문에 코드를 짧게 할수 있다.
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
