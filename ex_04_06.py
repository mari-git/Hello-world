def computepay(h,r):
    if h > 40 :
        pay = 40 * r + (h-40) * 1.5 * r
    else :
        pay = h * r
    return pay

hrs = input('Enter Hours:')
rate = input('Enter Rate:')
try :
    h = float(hrs)
    r = float(rate)
except:
    print ('Error, pls enter numeric data')
    quit()

p = computepay(h,r)
print('Pay', p)
