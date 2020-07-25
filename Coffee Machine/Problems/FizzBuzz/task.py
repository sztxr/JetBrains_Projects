for num in range(1, 101):
    fizz = num % 3 == 0
    buzz = num % 5 == 0
    print('FizzBuzz' if fizz and buzz
          else 'Fizz' if fizz
          else 'Buzz' if buzz
          else num)
