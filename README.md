Lydia Crompton
Tutorial 1
15/09/2023




##EXERCISE 1
# code 1 variable for 1 exercise

def main():
#Initialise neuron membrane potential in mV
    V_membrane=float(-75)
#update neuron membrane potential
    V_membrane=V_membrane+1
    print(V_membrane)

if __name__=='__main__':
    main()



    
##EXERCISE2
# Initialize the membrane potential variable with value 1
membrane_potential = 1

# Check the type of the variable
print(type(membrane_potential))

# Compute the value of the variable by multiplying it by 0.7
membrane_potential = membrane_potential * 0.7

# Check the type of the variable after multiplication
print(type(membrane_potential))




##EXERCISE3

#Neuron1

import sys
membrane_potential=0 #Initial membrane potential
spike_value=float(sys.argv[1])
    #Update membrane potential
membrane_potential+=spike_value
    
if membrane_potential>=-65:
   print("5")
   
else :
        print("0")



#Neuron2
def main():
    V_membrane = float(-56)
    
    spike = float(input())
    V_membrane += spike
    
    print(spike)
    
if __name__=='__main__':
    main()

#in terminal 
python3 neuron1.py | python3 neuron2.py
