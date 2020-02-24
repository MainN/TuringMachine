counter=0
f = open("finitestate.txt")
transitions={}
for string in f:
    state,elem,new_state=string.split(" ")
    transitions[(state,elem)]=new_state[:len(new_state)-1]
print(transitions)
state=input("enter initial state \n")
end_state=input("enter ending state \n")
input_string=input("enter string")
for x in input_string:
    print(state,x)
    state=transitions[(state,x)]
if state==end_state:
    print("True")
else:
    print("False")