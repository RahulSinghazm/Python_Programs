run=int(input("Enter run:"))
strike=int(input("Enter srtike run rate:"))
point=0
if run<50:
   run=run/2
   print("total +2 point:")
   print(run)
elif  (run>=50) and (run<100):
    run=run/2+5
    print("half century +5 point:")
elif run>=100:
    run=run/2+10
    print("century point +10")
if (strike>=80) and (strike<100):
    strike=2
    print("strike rate +2")
elif strike>=100:
   strike=4
   print("strike rate 4")
   print("total point run & strike:")
   print(strike+run)
else:
    print("closed")
