import numpy as np
import matplotlib.pyplot as plt
import math

# x position
x = 0                      
x_h = 0
# y position
y = 0
y_h = 0

# velocity 0                                  
v0 = 50 

# angle
angle = 35

# egree to radian             
angle_rad = (angle/360) * (2 * np.pi)   

# gravity
g = -9.806

# time                               
t = 0
t_h = 0

# delta time
dt = 0.01                               

# Konstanta Hambatan
D = 0.0013

# Massa Benda
M = 0.15  

# array
x_arr = [x]
y_arr = [y]
t_arr = [t]

# array 1
x_arr1 = [x_h]
y_arr1 = [y_h]
t_arr1 = [t_h]

# vx and vy
vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

# vx_h and vy_h
vx_h = v0 * np.cos(angle_rad)
vy_h = v0 * np.sin(angle_rad)

# v
v = math.sqrt((vx_h*vx_h) + (vy_h*vy_h))

# ax
ax =  -1*(D/M)*v*vx
 
# ay
ay =  g-(D/M)*v*vy

# main tanpa hambatan
while y >= 0:
    vy += g*dt
    y += vy*dt
    x += vx*dt
    t += dt
    if y < 0:
        break

    x_arr.append(x)
    y_arr.append(y)
    t_arr.append(t)

# main dengan hambatan
while y_h >= 0:
    vy_h += ay*dt
    y_h += vy_h*dt
    vx_h += ax*dt
    x_h += vx_h*dt
    t_h += dt
    if y_h < 0:
        break
    # store
    x_arr1.append(x_h)
    y_arr1.append(y_h)
    t_arr1.append(t_h)

# Numeric tanpa hambatan
# Total Time
t_tot_num = t_arr[-1]

# Range
range_num = x_arr[-1]

# Max Height
h_max_num = np.max(y_arr)


#Numerik Dengan Hambatan Udara
# Total Time
t_tot_num1 = t_arr1[-1]

# Range
range_num1 = x_arr1[-1]

# Max Height
h_max_num1 = np.max(y_arr1)


# Analytic
x_ex_arr = [0]
y_ex_arr = [0]
for t in t_arr:
    x_ex = v0 * np.cos(angle_rad) * t
    y_ex = (0.5 * g * t**2) + (v0 * np.sin(angle_rad) * t)
    x_ex_arr = [x_ex]
    y_ex_arr = [y_ex]
    print(x_ex_arr)
    print(y_ex_arr)

# Total Time
t_tot_ex = (2 * v0 * np.sin(angle_rad)) / -g

# Range
range_ex = v0 * np.cos(angle_rad) * t_tot_ex

# Max Height
h_max_ex = (v0**2 * np.sin(angle_rad)**2) / (-2 * g)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# Output
print("Nilai Numerik")
print("Waktu Total : %.2f" % (t_tot_num))
print("Jarak Jatuhnya Benda (m): %.2f" % (range_num))
print("Tinggi Maksimum (m): %.2f" % (h_max_num))
print(" ")

#Analitik
print("Analitik")
print("Waktu Total : %.2f" % (t_tot_ex))
print("Jarak Jatuhnya Benda (m): %.2f" % (range_ex))
print("Tinggi Maksimum (m): %.2f" % (h_max_ex))
print(" ")

#Numerik
print("Nilai Numerik Dengan Hambatan")
print("Waktu Total : %.2f" % (t_tot_num1))
print("Jarak Jatuhnya Benda (m): %.2f" % (range_num1))
print("Tinggi Maksimum (m): %.2f" % (h_max_num1))

# Check Len
c_len = 0

if(len(y_arr)>len(y_arr1)) :
    c_len = len(y_arr)
else : 
    c_len = len(y_arr1)

# Plot for Animation
plt.rcParams.update({'figure.max_open_warning': 0})
for i in range(c_len) :
    
    #Tanpa Udara
    if(i < len(y_arr)) :
        plt.scatter(x_arr[i], y_arr[i], marker='o', c='b')
        plt.text(32, 30, '{:.2f} s'.format(t_arr[i]),c='b')
        plt.plot(x_arr, y_arr, c='b', label='Udara Diabaikan')
    else :
        plt.scatter(x_arr[len(y_arr-1)], y_arr[len(y_arr-1)], marker='o', c='b')
        plt.text(32, 30, '{:.2f} s'.format(t_arr[len(y_arr-1)]),c='b')
        plt.plot(x_arr, y_arr, c='b', label='Udara Diabaikan')

    # Dengan Udara
    if(i < len(y_arr1)) :
        plt.scatter(x_arr1[i], y_arr1[i], marker='o', c='r')
        plt.text(32, 20, '{:.2f} s'.format(t_arr1[i]), c='r')
        plt.plot(x_arr1, y_arr1, c='r', label='Udara Tidak Diabaikan')
    else :
        plt.scatter(x_arr1[len(y_arr1)-1], y_arr1[len(y_arr1)-1], marker='o', c='r')
        plt.text(32, 20, '{:.2f} s'.format(t_arr1[len(y_arr1)-1]), c='r')
        plt.plot(x_arr1, y_arr1, c='r', label='Udara Tidak Diabaikan')
    
    plt.axhline(c='black')
    plt.axvline(c='black')
    plt.legend()
    plt.draw()
    plt.pause(0.01)
    ax.clear()

plt.show()