class para_test:
   def __init__(self,a,b):
      self.a = a
      self.b=b

   def set_a(self,a):
      self.a = a 
   def print_para(self):
      print self.a,self.b
def fun(test):
   test.set_a(5);

para=para_test(1,3)
para.print_para()
fun(para)
para.print_para()
   
