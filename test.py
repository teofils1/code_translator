class Sample:
    i=0
    def hello(self, o):
        print(o)
        print("Hello")
    def function(self, a,b):
        d=a+b
        table=[False,True]
        if d==0:
            arrr=[1,5,7,8]
            for i in arrr:
                for j in arrr:
                    if j<i:
                        z=i+j
                        print(z)
                        print(table)
object=Sample()
object.hello("ala")
object.function(1,2)
