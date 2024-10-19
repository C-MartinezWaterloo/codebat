

def string_times(str, n):
  return str * n

def front_times(str, n):
  if len(str) >= 3:
    return str[0:3] * n
  else:
    return str * n

def array_count9(nums):
  num = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      num += 1
  return num

def array_front9(nums):
  var = False
  if len(nums) >= 4:
    for i in range(4):
      if nums[i] == 9:
        return True
      else:
         var = False
  else:
    for i in range(len(nums)):
      if nums[i] == 9:
        return True
      else:
        var = False

  return var

def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


def strings_match(a, b):
    num = 0

    len1 = len(a)
    len2 = len(b)
    len3 = 0

    if len1 >= len2:
        len3 = len2
    else:
        len3 = len1

    for i in range(len3 - 1):
        if a[i] == b[i] and a[i + 1] == b[i + 1]:
            num += 1

    return num


def first_half(str):
  a = len(str) // 2
  return str[0:a]


def without_end(str):
  return str[1:-1]


def combo_string(a, b):
  short = ""
  long = ""
  if len(a) > len(b):
    long = a
    short = b
  else:
    long = b
    short = a

  string = ""
  string += short
  string += long
  string += short

  return string


def left2(str):
  vari = str[0:2]
  new_vari = str + vari
  return new_vari[2:]


def near_ten(num):
    val = num % 10
    if val in {0, 1, 2, 8, 9}:  # Check if val is in the set of values
        return True
    else:
        return False

def count_code(str):
  code = 0
  for i in range(len(str)-3):
    if str[i] == "c" and str[i+1] == "o" and str[i+3] == "e":
      code += 1

  return code

def end_other(a, b):
    if a.lower() == b[-len(a):].lower():
        return True
    if b.lower() == a[-len(b):].lower():
        return True
    return False

def centered_average(nums):
  low = nums[0]
  high = nums[0]
  sum = 0
  for i in range(len(nums)):
    if nums[i] > high:
      high = nums[i]

  for i in range(len(nums)):
    if nums[i] < low:
      low = nums[i]


  for i in range(len(nums)):
    sum += nums[i]

  sum -= low
  sum -= high
  average = sum//((len(nums)-2))

  return average


import math

global current_digit
current_digit = -1

def next_digit_pi():
    global current_digit

    current_digit += 1

    var = str(math.pi).replace(".", "")[current_digit]


    return var

if __name__ == "__main__":





























