from compfunc import *


## task 1
plt.cla()
vel = 100
g = 9.81
angle = 30
h = 0
dt = 0.01
x, y = proj_motion(vel, angle, g, h, dt)
plt.plot(x,y)
plt.xlim(0)
plt.ylim(0)
values = "Vel = " + str(vel) +"\nAngle = " + str(angle) + "\nH = " + str(h) + "\nG = " + str(g) + "\ndt = " + str(dt)
plt.annotate(values,xy = (400,40))
plt.title("Simple drag-free model")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph1.png")


## task 2
plt.cla()
vel = 100
g = 9.91
angle = 30
h = 0
x, y, R, t = analytic_proj_motion(vel,g,h,angle)
apx, apy = apogee(vel,g,h,angle)
plt.plot(apx,apy, 'y*', markersize=16, label='apogee')
plt.plot(x,y,label = "flight")
plt.legend()
plt.xlim(0)
plt.ylim(0)
values = "Vel = " + str(vel) +"\nAngle = " + str(angle) + "\nH = " + str(h) + "\nG = " + str(g)
plt.annotate(values,xy = (400,40))
plt.title("Analytic drag-free model")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph2.png") 


## task 3
plt.cla()
X = 1000
Y = 300
start_height = 100
g = 9.81
vel = 150
lux, luy, lbx,lby,hbx,hby = low_high_ball(g,X,Y,start_height,vel)
pos = list(lux).index(X)
maxy = max(list(hby))
plt.plot(lux[:pos],luy[:pos],label = "low_u")
plt.plot(lbx[:pos],lby[:pos],color = "black",label = "low_ball" )
plt.plot(hbx[:pos],hby[:pos],label = "high_ball")
plt.xlim(0,X*1.25)
plt.ylim(0,maxy*1.25)
plt.legend()
values = "X = " + str(X) +"\nY = " + str(Y) + "\nVel = " + str(vel) + "\nH = " + str(start_height) + "\nG = " + str(g)
plt.annotate(values,xy = (600,600))
plt.annotate("Target",xy = (X,Y))
plt.title("High/low ball trajectories through a fixed point")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph3.png")









## task 4
plt.cla()
vel = 10
angle = 60
start_height = 2
g = 9.81
x_org, y_org, x_opt, y_opt, a_max = optimum_angle(vel,angle,start_height,g)
plt.plot(x_org,y_org, color = "black", label = "Original flight")
plt.plot(x_opt,y_opt, color = "blue", label = "Max R")
plt.ylim(0)
plt.xlim(0)
plt.legend()
values = "\nVel = " + str(vel) + "\nAngle of original = " + str(angle) + "\nAngle of optimum = "+ str(a_max.round(2)) + "\nH = " + str(start_height) + "\nG = " + str(g)
plt.annotate(values,xy = (3.5,2))
plt.title("Normal trajectory vs max range trajectory")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph4.png")   


## task 5
plt.cla()
X = 1000
Y = 300
start_height = 100
g = 9.81
vel = 150
angle = 50
lux, luy, lbx,lby,hbx,hby = low_high_ball(g,X,Y,start_height,vel)
x_org, y_org, x_opt, y_opt, a_max = optimum_angle(vel,angle,start_height,g)
xbc, ybc = bounding_curve(x_opt,vel,g,start_height)
pos = list(lux).index(X)
maxy = max(list(hby))
plt.plot(lux,luy,label = "low_u")
plt.plot(lbx,lby,color = "black",label = "low_ball" )
plt.plot(hbx,hby,label = "high_ball")
plt.plot(x_opt,y_opt,color = "pink",label = "max_range")
plt.plot(xbc,ybc,"--", label = "bounding",color = "red")
plt.plot(X, Y, 'y*', markersize=16, label='X,Y (1000,300)')
plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.title("Low/high ball, max range, minimum speed and bounding parabola")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph5.png")


## task 6
plt.cla()
vel = 10
angle = 60
h = 2
g = 9.81
x_org, y_org, x_opt, y_opt, a_max = optimum_angle(vel,angle,h,g)
plt.plot(x_org,y_org, color = "black", label = "Original flight")
plt.plot(x_opt,y_opt, color = "blue", label = "Max R")
plt.ylim(0)
plt.xlim(0)
plt.legend()
x = analytic_curve_length(vel,g,angle,h)
values = "Vel = " + str(vel) +"\nAngle = " + str(angle) + "\nH = " + str(h) + "\nG = " + str(g)
plt.annotate(values,xy = (1,1))
string = "Projectile travelled " + str(x.round(3)) + "m\nOptimum angle is " + str(a_max.round(2)) + " degrees"
plt.annotate(string,xy = (2.5,2.5))  
plt.title("Graph with length of parabolic arc")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph6.png")


## task 7.1
plt.cla()
vel = 10
g = 9.81
start_height = 0
angle = 30
x_val30,y_val30,R,T30 = neg_proj_motion(vel,g,start_height,30)
x_val45,y_val45,R,T45 = neg_proj_motion(vel,g,start_height,45)
x_val60,y_val60,R,T60 = neg_proj_motion(vel,g,start_height,60)
x_val70_5,y_val70_5,R,T70_5 = neg_proj_motion(vel,g,start_height,70.5)
x_val78,y_val78,R,T78 = neg_proj_motion(vel,g,start_height,78)
x_val85,y_val85,R,T85 = neg_proj_motion(vel,g,start_height,85)
values = "Vel = " + str(vel) +"\nH = " + str(start_height) + "\nG = " + str(g) +"\nAngle = Legend"
plt.annotate(values,xy = (15,4))
plt.plot(x_val30,y_val30,label = "30")
plt.plot(x_val45,y_val45,label = "45")
plt.plot(x_val60,y_val60,label = "60")
plt.plot(x_val70_5,y_val70_5,label = "70.5")
plt.plot(x_val78,y_val78,label = "78")
plt.plot(x_val85,y_val85,label = "85")
plt.legend()
plt.ylim(-5)
plt.xlim(0)
plt.title("Projectiles not stopping at h=0")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph7_1.png")


## task 7.2
plt.cla()
vel = 10
g = 10
start_height = 0
angle = 85
time = 2.5
t_val85, r_val85,maxco85,minco85 = time_r(vel,g,start_height,85,time)
t_val78, r_val78,maxco78,minco78 = time_r(vel,g,start_height,78,time)
t_val705, r_val705,maxco705,minco705 = time_r(vel,g,start_height,70.5,time)
t_val60, r_val60,maxco60,minco60 = time_r(vel,g,start_height,60,time)
t_val45, r_val45,maxco45,minco45 = time_r(vel,g,start_height,45,time)
t_val30, r_val30,maxco30,minco30 = time_r(vel,g,start_height,30,time)

plt.plot(maxco85[0], maxco85[1], 'x', markersize=16)
plt.plot(minco85[0], minco85[1], 'x', markersize=16)
plt.plot(maxco78[0], maxco78[1], 'x', markersize=16)
plt.plot(minco78[0], minco78[1], 'x', markersize=16)
plt.plot(t_val85,r_val85,label = "85")
plt.plot(t_val78,r_val78,label = "78")
plt.plot(t_val705,r_val705,label = "70.5")
plt.plot(t_val60,r_val60,label = "60")
plt.plot(t_val45,r_val45,label = "45")
plt.plot(t_val30,r_val30,label = "30")
plt.xlim(0,2.5)
plt.ylim(0,30)
plt.legend()
plt.title("Range against time with max/min for angle>70.5")
plt.xlabel("t/s")
plt.ylabel("range r/m")
plt.savefig("graph7_2.png")



## task 8 
plt.cla()
vel = 5
C = 0.7
angle = 45
h = 10
g = 9.81
N = 15
x, y = bounce_ball_analytic(vel,C,angle,h,g,N)
plt.plot(x,y)
plt.xlim(0)
plt.ylim(0)
values = "\nVel = " + str(vel) + "\nAngle = " + str(angle) + "\nC = " + str(C) + "\nH = " + str(h) + "\nG = " + str(g)
plt.annotate(values,xy = (17.5,7))
plt.title("Bouncy ball with coeffecient of restitution C")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph8.png")

## task 9.1
plt.cla()
vel = 100
angle = 45
h = 10
g = find_g(9.81,6371000,h)
dc = 0.1
A = 1
ad = air_density(h)
m = 1
x_val,y_val = ar_proj_motion(angle,vel,h,g,dc,ad,A,m)
plt.plot(x_val,y_val,label = "ar")
plt.legend()
plt.xlim(0)
plt.ylim(0)
values = "\nVel = " + str(vel) + "\nAngle = " + str(angle) + "\nH = " + str(h) + "\nG and air density are recalculated each step"
plt.annotate(values,xy = (10,10))
plt.title("Model incorporating drag, change in g and air density with altitude")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph9_1.png")


## task 9.2
plt.cla()
vel = 50
angle = 45
h = 10
g = find_g(9.81,6371000,h)
dc = 0.1
A = 1
ad = air_density(h)
m = 1
xar,yar = ar_proj_motion(angle,vel,h,g,dc,ad,A,m)
x,y,r,t = analytic_proj_motion(vel,9.81,h,angle)
plt.plot(xar,yar,label = "ar")
plt.plot(x,y, label = "no ar")
plt.legend()
plt.xlim(0)
plt.ylim(0)
values = "\nVel = " + str(vel) + "\nAngle = " + str(angle) + "\nH = " + str(h) + "\nG and air density are recalculated \neach step"
plt.annotate(values,xy = (75,30))
plt.title("Drag-free vs drag incorporating model")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("graph9_2.png")


