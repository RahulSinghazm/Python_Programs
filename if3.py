run=int(input("Enter run:"))
strike=int(input("Enter srtike run rate:"))
boundary=int(input("Enter Four:"))
boundary1=int(input("Enter Six:"))
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
   boundary=boundary
   print("boundary four +1 point:")
   print(boundary+points)
if boundary1:
   boundary1=boundary1*2
   print("boundary1 Six +2 point:")
   print(boundary1+boundary+points)
   print("total point run & strike & boundary & boundary1")
   print(boundary1+boundary+points)
else:
    print("closed")
