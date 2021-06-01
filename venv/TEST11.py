import json

obj='{"1Data":"1stvalue","2data":"2ndvalue"}'
obj1= json.loads(obj)
(k,v)=obj1.items()
print(k,v)


pob={"Data":"Value","2ndData":"2ndValue"}
pjson=json.dumps(pob)
print(pjson)

print("the ASCII value of @ is ",ord("@"))
print("the BInary value of 10 is ",bin(10).replace("0b",''))
print("I am Learning \U0001F40D")


