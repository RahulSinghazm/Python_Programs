run=int(input("Enter run:"))
strike=int(input("Enter srtike run rate:"))
boundary=int(input("Enter Four:"))
boundary1=int(input("Enter Six:"))
wicket=int(input("Enter wicket:"))
economy_rate=float(input("Enter economy_rate per over:"))
catch=int(input("Enter no. of catch:"))
stumping=int(input("Enter no. of stumping:"))
run_out=int(input("Enter no.of run out:"))
points=0
if run<50:
   points=run/2
   print("total +2 point:")
   print(points)
if  (run>=50) and (run<100):
    points=run/2
    points=points+5
    print("half century +5 point:")
    print(points)
if run>=100:
    points=run/2
    points=points+10
    print("century point +10")
    print(points)
if (strike>80) and (strike<=100):
    points=points+2
    print("strike rate +2")
    print(points)
if strike>100:
   points=points+4
   print("strike rate 4")
   print(points)
if boundary:
   points=boundary
   print("boundary four +1 point:")
   print(points)
if boundary1:
   points=boundary1*2
   print("boundary1 Six +2 point:")
   print(points)
if wicket:
   points=wicket*10
   print("total +10 wicket  point:")
   print(points)
if wicket:
   points=wicket*10
   print("total +10 wicket  point:")
   print(wicket+points)
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
