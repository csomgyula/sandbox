from numpy import exp

def f(v, w, b):
   return 1/( 1 + exp(-(v*w + b)) )
   
def dfw(v, w, b):
   return v * f(v,w,b) * (1 - f(v,w,b))
   
def dfb(v, w, b):
   return f(v,w,b) * (1 - f(v,w,b))
   
def loop(v,w,b):
   for i in range(100):
       fv = f(v,w,b)
       
       error = fv - 0.5
       if error * error < 0.000001:
           return

       dfwv = dfw(v,w,b)
       dfbv = dfb(v,w,b)
       
       if dfwv < 0.1:
           dfwv = 0.1         
       if dfbv < 0.1:
           dfbv = 0.1          
       
       adjust_w = 2 * error * dfwv
       adjust_b = 2 * error * dfbv
       print(f"v*: {v*w+b}, w: {w}, b: {b},error: {error}, adjust_w: {adjust_w}, adjust_b: {adjust_b}")
       
       w -= adjust_w
       b -= adjust_b
       
loop(100,1,0)