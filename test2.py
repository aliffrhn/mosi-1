import numpy as np
import matplotlib.pyplot as plt
import math

# x position
x = 0  

# velocity 0
y = 0   

# y position
v0 = 50

# angle
angle = 35

# degree to radian                          
angle_rad = (angle/360) * (2 * np.pi)

#gravity
g = -9.8

#time
t = 0   

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

# vx and vy
vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

# v
v = math.sqrt((vx*vx) + (vy*vy))

# ax
ax =  -1*(D/M)*v*vx

# ay
ay =  g-(D/M)*v*vy

# Update
while y >= 0:
    vy+= ay*dt
    y += vy*dt
    vx+= ax*dt
    x += vx*dt
    t += dt
    if y < 0:
        break
    # store
    x_arr.append(x)
    y_arr.append(y)
    t_arr.append(t)

# Numeric
# Total Time
t_tot_num = t_arr[-1]

# Range
range_num = x_arr[-1]

# Max Height
h_max_num = np.max(y_arr)

# Analytic
x_ex_arr = [0]
y_ex_arr = [0]
for t in t_arr:
    x_ex = v0 * np.cos(angle_rad) * t
    y_ex = (0.5 * g * t**2) + (v0 * np.sin(angle_rad) * t)
    x_ex_arr = [x_ex]
    y_ex_arr = [y_ex]

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
print("Waktu Total (T): %.2f" % (t_tot_num))
print("Jarak Jatuhnya Benda (m): %.2f" % (range_num))
print("Tinggi Maksimum (m): %.2f" % (h_max_num))

print("Analitik")
print("Waktu Total (s): %.2f" % (t_tot_ex))
print("Jarak Jatuhnya Benda (m): %.2f" % (range_ex))
print("Tinggi Maksimum (m): %.2f" % (h_max_ex))


# Plot for Animation
plt.rcParams.update({'figure.max_open_warning': 0})
for i in range(len(y_arr)):
    plt.scatter(x_arr[i], y_arr[i], marker='o', c='b')
    plt.text(32, 14, '{:.2f} s'.format(t_arr[i]))
    plt.plot(x_arr, y_arr, c='b', label='Numerik', color='red')
    plt.axhline(c='black')
    plt.axvline(c='black')
    plt.legend()
    plt.draw()
    plt.pause(0.01)
    ax.clear()
    


plt.show()