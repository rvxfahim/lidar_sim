#! /usr/bin/env python3

import numpy
from sensor_msgs.msg import NavSatFix
import rospy
import geopy.distance
import pymap3d as pm
from geometry_msgs.msg import PoseWithCovarianceStamped
import math

def euler_from_quaternion(x, y, z, w):
        
        #importierter Code um quaternion Winkel in Euler Winkel umzuwandeln

        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians

#Vektorfunktionen

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


if __name__ == '__main__':

    

    # rospy.init_node("main")

    #position und roatation des Roboters von GPS Sensor

    """pos = rospy.wait_for_message("gps/fix",NavSatFix,timeout=5)
    pose = rospy.wait_for_message("utm_local",PoseWithCovarianceStamped,timeout=5)
    x = pose.pose.pose.orientation.x
    y = pose.pose.pose.orientation.y
    z = pose.pose.pose.orientation.z
    w = pose.pose.pose.orientation.w
    
    yaw = euler_from_quaternion(x,y,z,w)[2]
    print ("yaw des Roboters:")
    print (yaw)"""


    #Parkplätze: 

    PBreite = 2.3
    PBreitea = 2.2
    PLänge = 4.85

    Antennepos = 0.4 #in X Richtung des Roboters

    p = NavSatFix()
    p.latitude = 51.5060516495208
    p.longitude = 7.456405157715967


    p0 = NavSatFix()
    p0.latitude = 51.5060489074
    p0.longitude = 7.45644033068


    p1 = NavSatFix()
    p1.latitude = 51.5060463889
    p1.longitude = 7.45647319444


    p2 = NavSatFix()
    p2.latitude = 51.5060438333
    p2.longitude = 7.45650763889



    p3 = NavSatFix()
    p3.latitude = 51.5060412222
    p3.longitude = 7.45654191111


    p4a = NavSatFix()
    p4a.latitude = 51.5060385278
    p4a.longitude = 7.45657486389



    p5a = NavSatFix()
    p5a.latitude = 51.50603609640693
    p5a.longitude = 7.456606309423941






    #Neue Tests mit 10 Parkplätzen:

    t1 = NavSatFix()
    t1.latitude = 51.50627735
    t1.longitude = 7.45638655

    t2 = NavSatFix()
    t2.latitude = 51.50625682192889
    t2.longitude = 7.456382638647902

    t3 = NavSatFix()
    t3.latitude = 51.5062370694
    t3.longitude = 7.45637688889

    t4 = NavSatFix()
    t4.latitude = 51.5062153444
    t4.longitude = 7.45637531944

    t5 = NavSatFix()
    t5.latitude = 51.5061945528
    t5.longitude = 7.456373725

    t6 = NavSatFix()
    t6.latitude = 51.5061742
    t6.longitude = 7.45637013333

    t7 = NavSatFix()
    t7.latitude = 51.5061539111
    t7.longitude = 7.45636640833

    t8 = NavSatFix()
    t8.latitude = 51.50613338302848
    t8.longitude = 7.456362496988469

    t9 = NavSatFix()
    t9.latitude = 51.5061130722
    t9.longitude = 7.4563582

    t10 = NavSatFix()
    t10.latitude = 51.50609254412832
    t10.longitude = 7.4563542886619665



    #Yaw Ausrichtung der parkplätze

    tv = pm.geodetic2enu(t9.latitude, t9.longitude, 0, t5.latitude, t5.longitude, 0)
    print ("vektor P4a > P1")
    print (tv)
    v1 = [1,0]
    v2 = [tv[0],tv[1]]
    
    print ("Länge des Vektors")
    print(length(v2))
    print ("Winkel des Vektors")
    pyaw = angle(v1,v2)
    print(pyaw)
 

    pz = [((PBreite)/length(v2))*v2[0],((PBreite)/length(v2))*v2[1]]

    fixa = [pz[0]*math.cos(math.pi/2)-pz[1]*math.sin(math.pi/2),pz[0]*math.sin(math.pi/2)+pz[1]*math.cos(math.pi/2)]

    print(fixa)

    p0 = pm.enu2geodetic(pz[0],pz[1],0,t9.latitude,t9.longitude,0)
    print ("Interpolierter Punkt P0:")
    print(p0)




  