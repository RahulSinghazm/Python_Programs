wicket=int(input("Enter wicket:"))
economy_rate=float(input("Enter economy_rate per over:"))
catch=int(input("Enter no. of catch:"))
stumping=int(input("Enter no. of stumping:"))
run_out=int(input("Enter no.of run out:"))
points=0
if wicket:
   points=wicket*10
   print("total +10 wicket  point:")
   print(wicket)
if wicket==3:
   points=points+5
   print("total +5 extra for 3 wicket point:")
   print(points)
if wicket>=5:
   points=points+10
   print("total +10 extra for 5 or more wicket point:")
   print(points)
if (economy_rate>=3.5) and (economy_rate<=4.5):
   points=points+4
   print("total +4 extra for run rate per over point:")
   print(points)
if (economy_rate>=2) and (economy_rate<=3.5):
   points=points+7
   print("total +7 extra for run rate per over point:")
   print(points)
if economy_rate<2:
   points=points+10
   print("total +10 extra for run rate per over point:")
   print(points)
if catch:
   points=points+catch*10
   print("total +10 catch wicket  point:")
   print(points)
if stumping:
   points=points+stumping*10
   print("total +10 stumping wicket  point:")
   print(points)
if run_out:
   points=points+run_out*10
   print("total +10 run out wicket  point:")
   print(points)
else:
    print("closed")
