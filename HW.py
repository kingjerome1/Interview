a = int(input('請輸入德瑞克分數: '))
b = int(input('請輸入尚恩分數: '))
c = int(input('請輸入傑夫分數: '))
d = int(input('請輸入馬基分數: '))

def round_up(num, divisor):
    return num - (num%divisor) + divisor

def add_score(x):
    if (x + 3) > round_up(x, 5) :
        result = round_up(x, 5)
        if result < 40:
            return x
        return result
    else:
        result = x 
        return result

print('以下為加分後的總成績')
print('德瑞克新分數: ' + add_score(a))
print('尚恩新分數: ' + add_score(b))
print('傑夫新分數: ' + add_score(c))
print('馬基新分數: ' + add_score(d))
