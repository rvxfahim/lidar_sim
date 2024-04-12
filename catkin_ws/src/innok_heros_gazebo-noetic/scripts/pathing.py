#! /usr/bin/env python3

#Autor: Lajos Kühn

import rospy
from geometry_msgs.msg import Twist


if __name__== '__main__':

    #Ros-Node wird gestartet

    rospy.init_node("pathing")
    rospy.loginfo("Node started")

    #Publisher wird initialisiert und Topic cmd_vel festgelegt

    pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

    #Rate wird auf 10 Hz festgelegt

    rate = rospy.Rate(100)


    #Messages für links- und rechtsdrehung sowie geradeaus fahren anlegen

    msgl = Twist()
    msgl.angular.z = 1.0

    msgr = Twist()
    msgr.angular.z = -1.0

    msgg = Twist()
    msgg.linear.x = 1.0

    #Kurze loopfunktionen für die kontinuierlichen Bewegungen

    def turnright(amount):
       x=0
       for x in range (0,amount):
          pub.publish(msgr)

          rate.sleep()
          x+1
    def turnleft(amount):
       x=0
       for x in range (0,amount):
          pub.publish(msgl)

          rate.sleep()
          x+1
    def move(amount):
       x=0
       for x in range (0,amount):
          pub.publish(msgg)

          rate.sleep()
          x+1
    def pause(amount):
       x=0
       for x in range (0,amount):
          rate.sleep()
          x+1

    
    #Main Loop. Anpassbar für die jeweilige Anwendung. 1 "amount" = 1/100 Sekunde Bewegung/Drehung
    
    #Beispielpfad für einen grob Acht-Förmigen Weg durch die Simulationsumgebung "Labor für intelligente Mobilität"

    
    while not rospy.is_shutdown():
      
        move(300)
        turnleft(315)
        move(1000)
        turnleft(315)
        move(600)
        turnleft(315)
        move(1400)
        turnleft(315)
        move(600)
        pause(3000)
        
         
        

