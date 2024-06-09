import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider
#from matplotlib import animation
#from matplotlib.animation import FuncAnimation
#from ipywidgets import interact, widgets

def proj_motion(vel,angle,grav_strength,start_height,time_interval):
    angle = np.radians(angle)
    y_coords = []
    x_coords = []
    x_vel = vel*np.cos(angle)
    y_vel = vel*np.sin(angle)
    x_pos = 0
    y_pos = start_height
    landed = False
    while landed == False:
        y_pos += y_vel*(time_interval)
        y_vel += -1*(grav_strength)*(time_interval)

        x_pos += x_vel*(time_interval)

        if y_pos <=0:
            landed = True

        y_coords.append(y_pos)
        x_coords.append(x_pos)
    return x_coords, y_coords


def apogee(vel,g,start_height,angle):
    angle = np.radians(angle)
    x_apogee = ((vel**2)/g)*np.sin(angle)*np.cos(angle)
    y_apogee = ((vel*vel)/(2*g))*np.sin(angle)*np.sin(angle)+start_height
    return x_apogee,y_apogee


def analytic_proj_motion(vel,g,start_height,angle):
    angle = np.radians(angle)
    st_part_R = (vel**2)/g
    sqrt_part_R = ((np.sin(angle))**2)+((2*g*start_height)/(vel**2))
    sc_part_R = np.sin(angle)*np.cos(angle)
    R = st_part_R*(sc_part_R + np.cos(angle)*np.sqrt(sqrt_part_R))
    x_val = np.arange(start = 0,stop = R, step = 0.1)     ### may need to change step based on size of R
    x_val = list(x_val)
    y_val = []
    for i in range(len(x_val)):
        x = x_val[i]
        y_first = start_height + (x*np.tan(angle))
        z = g/(2*(vel**2))
        y_second = z*(1+(np.tan(angle)**2))*(x**2)
        y = y_first - y_second
        y_val.append(y)
    flight_time = R/(vel*np.cos(angle))
    return x_val, y_val, R, flight_time


def low_high_ball(g,X,Y,start_height,vel): 
    luY = Y-start_height
    low_u = np.sqrt(g) * np.sqrt(luY+np.sqrt((X**2)+(luY**2)))
    low_u_anglep1 = luY + np.sqrt((X**2)+(luY**2))
    low_u_angle = np.degrees(np.arctan(low_u_anglep1/X))
    low_u_x, low_u_y, low_u_R, low_u_time = analytic_proj_motion(low_u,g,start_height,low_u_angle)
    a = (g/(2*(vel**2)))*(X**2)
    b = (-1)*X
    c = Y - start_height + ((g*(X**2))/(2*(vel**2)))
    disc = (b**2)-(4*a*c)
    postheta = np.degrees(np.arctan((-b+np.sqrt(disc))/(2*a)))
    negtheta = np.degrees(np.arctan((-b-np.sqrt(disc))/(2*a)))
    low_ball_x, low_ball_y, low_ball_R, low_ball_time = analytic_proj_motion(vel,g,start_height,negtheta)
    high_ball_x, high_ball_y, high_ball_R, high_ball_time = analytic_proj_motion(vel,g,start_height,postheta)
    return low_u_x, low_u_y, low_ball_x, low_ball_y, high_ball_x, high_ball_y



def curve_length_approx(x_val,y_val):
    clen = 0
    for i in range(len(x_val)-1):
        xlen = abs(x_val[i+1]-x_val[i])
        ylen = abs(y_val[i+1]-y_val[i])
        clen += np.sqrt((xlen**2)+(ylen**2))
    return clen

def optimum_angle(vel,angle,start_height,g):
    x_org, y_org, R_org, t_org = analytic_proj_motion(vel,g,start_height,angle)
    amaxp1 = 2+((2*g*start_height)/(vel**2))
    amax = np.arcsin(1/(np.sqrt(amaxp1)))
    amax = np.degrees(amax)
    x_opt, y_opt, R_opt, t_opt = analytic_proj_motion(vel,g,start_height,amax)
    return x_org, y_org, x_opt, y_opt,amax


def analytic_curve_length(vel,g,angle,h):
    angle = np.radians(angle)
    Rp1 = (vel**2)/(g)
    Rp2 = np.sin(angle)*np.cos(angle)
    Rp3 = (np.sin(angle)**2)+((2*g*h)/(vel**2))
    X = Rp1*(Rp2 + (np.cos(angle)*np.sqrt(Rp3)))
    clenp1 = (vel**2)/(g*(1+(np.tan(angle)**2)))
    uplim = np.tan(angle)
    lowlim = (np.tan(angle)) - ((g*X)/(vel**2))*(1+(np.tan(angle)**2))
    uplimval = (0.5*np.log(abs(np.sqrt(1+(uplim**2))+uplim))) + (0.5*uplim*np.sqrt(1+uplim**2))
    lowlimval = (0.5*np.log(np.sqrt(1+(lowlim**2))+lowlim)) + (0.5*lowlim*np.sqrt(1+(lowlim**2)))
    clenp2 = uplimval-lowlimval
    s = clenp1*clenp2
    return s


def bounding_curve(x_val,vel,g,start_height):
    y_val = []
    vel2 = vel**2
    for x in x_val:
        yp1 = (vel2)/(2*g)
        yp2 = (g/(2*vel2))*(x**2)
        y = start_height + yp1 - yp2
        y_val.append(y)
    return x_val,y_val

def neg_proj_motion(vel,g,start_height,angle):
    angle = np.radians(angle)
    st_part_R = (vel**2)/g
    sqrt_part_R = ((np.sin(angle))**2)+((2*g*start_height)/(vel**2))
    sc_part_R = np.sin(angle)*np.cos(angle)
    R = st_part_R*(sc_part_R + np.cos(angle)*np.sqrt(sqrt_part_R))
    Z = R*2
    x_val = np.arange(start = 0,stop = Z, step = 0.1)
    x_val = list(x_val)
    y_val = []
    ftime = []
    for i in range(len(x_val)):
        x = x_val[i]
        y_first = start_height + (x*np.tan(angle))
        z = g/(2*(vel**2))
        y_second = z*(1+(np.tan(angle)**2))*(x**2)
        y = y_first - y_second
        y_val.append(y)
    flight_time = R/(vel*np.cos(angle))
    return x_val, y_val, R, flight_time

def time_r(vel,g,start_height,angle,time):
    angle = np.radians(angle)
    t_val =np.arange(start = 0,stop = time, step = 0.0001)
    r_val = []
    for t in t_val:
        r1 = (vel**2)*(t**2)
        r2 = (g)*(t**3)*(vel)*(np.sin(angle))
        r3 = (0.25)*(g**2)*(t**4)
        r = np.sqrt(r1-r2+r3)
        r_val.append(r)
    if np.degrees(angle)>70.5:
        t1 = ((3*vel)/(2*g))*np.sin(angle)
        t2 = ((9*(vel**2))/(4*(g**2)))*(np.sin(angle)**2)
        t3 = t2 - ((2*(vel**2))/(g**2))
        tmax = t1 + np.sqrt(t3)
        tmin = t1 - np.sqrt(t3)

        r1 = (vel**2)*(tmax**2)
        r2 = (g)*(tmax**3)*(vel)*(np.sin(angle))
        r3 = (0.25)*(g**2)*(tmax**4)
        tmaxr = np.sqrt(r1-r2+r3)
        tmaxco = [tmax,tmaxr]

        r1 = (vel**2)*(tmin**2)
        r2 = (g)*(tmin**3)*(vel)*(np.sin(angle))
        r3 = (0.25)*(g**2)*(tmin**4)
        tminr = np.sqrt(r1-r2+r3)
        tminco = [tmin,tminr]
    else:
        tmaxco = [-1000,-1000]
        tminco = [-1000,-1000]
    return t_val,r_val,tmaxco,tminco

def bounce_ball_analytic(vel,C,angle,h,g,N):
    angle = np.radians(angle)
    x_vel = np.cos(angle)*vel
    x_val = []
    y_val = []
    rang = 0
    try:
        for i in range(N):
            angle = np.degrees(angle)
            x, y, R, t = analytic_proj_motion(vel,g,h,angle)
            h = 0
            angle = np.radians(angle)
            x = [x+rang for x in x]
            y_distch = y[-2]-y[-1]
            dt = t/len(y)
            y_vel = y_distch/(dt)
            new_y_vel = y_vel*C
            newangle = np.arctan(new_y_vel/x_vel)
            angle = newangle
            new_vel = np.sqrt((new_y_vel**2)+(x_vel**2))
            vel = new_vel
            x_val+=x
            y_val+=y
            rang += R
    except:
        pass
    return x_val,y_val

def air_density(alt):  ## alt in metres
    if alt>25000:
        T = -131.21 + (0.00299*alt)
        p = 2.488 * (((T+273.1)/216.6)**(-11.388))
    elif alt>11000:
        T = -56.46
        p = 22.65 * np.e**(1.73-(0.000157*alt))
    else:
        T = 15.04 - (0.00649*alt)
        p = 101.29 * (((T+273.1)/288.08)**5.256)
    kgperm = p/(0.2869*(T+273.1))
    return kgperm

def find_g(g,R,h):  # earth rad = 6371000m or give height and rad in same units
    return (g*(1-((2*h)/R)))

def find_k(dc,ad,A,m):
    k = (0.5*dc*ad*A)/(m)
    return k

def ar_proj_motion(angle,vel,h,g,dc,ad,A,m):
    x_coord = []
    y_coord = []
    x_pos = 0
    y_pos = h
    dt = 0.01
    angle = np.radians(angle)
    x_vel = np.sin(angle)*vel
    y_vel = np.cos(angle)*vel
    landed = False
    while landed == False:
        k = find_k(dc,ad,A,m)
        x_coord.append(x_pos)
        y_coord.append(y_pos)
        a_xp1 = x_vel/vel
        a_xp2 = k*(vel**2)
        a_x = -(a_xp1*a_xp2)
        a_yp1 = -(g)
        a_yp2 = y_vel/vel
        a_yp3 = a_xp2
        a_y = a_yp1-(a_yp2*a_yp3)
        x_pos += x_vel*dt + (0.5*a_x*(dt**2))
        y_pos += y_vel*dt + (0.5*a_y*(dt**2))
        x_vel += a_x*dt
        y_vel += a_y*dt
        vel = np.sqrt((x_vel**2)+(y_vel**2))
        ad = air_density(y_pos)
        g = find_g(9.81,6371000,y_pos)
        #print(x_vel,y_vel,vel)
        if y_pos<0:
            landed = True
        
    return x_coord, y_coord