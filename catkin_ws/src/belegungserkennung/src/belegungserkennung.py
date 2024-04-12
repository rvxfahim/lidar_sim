
#! /usr/bin/env python3

from gazebo_msgs.srv import GetModelState
import rospy
import ros_numpy
from sensor_msgs.msg import PointCloud2
import numpy
import math
import geometry_msgs.msg
import tf 
import time
from tf2_sensor_msgs.tf2_sensor_msgs import do_transform_cloud
import sys, signal
from geometry_msgs.msg import Twist
from std_msgs.msg import String

#Klassen:

class GModel:

    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name
        self.Zustände = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.Zustände = numpy.array(self.Zustände)
        self.Belegungszustand = [0,0]



    def get_model_state(self):

        model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp_coordinates = model_coordinates(self._name, self._relative_entity_name)
        self.x = resp_coordinates.pose.position.x
        self.y = resp_coordinates.pose.position.y
        x = resp_coordinates.pose.orientation.x
        y = resp_coordinates.pose.orientation.y
        z = resp_coordinates.pose.orientation.z
        w = resp_coordinates.pose.orientation.w
        euler = euler_from_quaternion(x,y,z,w)
        self.r = euler[2]
    

    def differenzvektor(self,GModel):
        Vektor = [GModel.x-self.x, GModel.y-self.y]
        return Vektor
    

    def calculateZustand(self):

        #Berechnet den eigenen Belegungszustand.

        outdated = 60

        if time.time()-self.Zustände[1][0]>=outdated:
            self.Zustände[2][0]=1  
        if time.time()-self.Zustände[1][1]>=outdated:
            self.Zustände[2][1]=1
        if time.time()-self.Zustände[1][2]>=outdated:
            self.Zustände[2][2]=1
        if time.time()-self.Zustände[1][3]>=outdated:
            self.Zustände[2][3]=1
        if time.time()-self.Zustände[1][4]>=outdated:
            self.Zustände[2][4]=1

        if sum(self.Zustände[2]) == 5: 
            self.Belegungszustand[1] = 1

        else:
            self.Belegungszustand[1]=0
        
        self.Zustände[2][0]=0
        self.Zustände[2][1]=0
        self.Zustände[2][2]=0
        self.Zustände[2][3]=0
        self.Zustände[2][4]=0


        if sum(self.Zustände[0]) == 0: 
            self.Belegungszustand[0] = 0
        elif sum(self.Zustände[0]) == 1:
            self.Belegungszustand[0] = 1 
        elif sum(self.Zustände[0]) == 2:
            self.Belegungszustand[0] = 2 
        elif sum(self.Zustände[0]) == 3:
            self.Belegungszustand[0] = 3 
        elif sum(self.Zustände[0]) == 4:
            self.Belegungszustand[0] = 4
        elif sum(self.Zustände[0]) == 5:
            self.Belegungszustand[0] = 5   

        return self.Belegungszustand

    def displayZustand(self):

        #gibt den eigenen Belegungszustand im Terminal aus
        if self.Belegungszustand[1] == 1:
            print(str(self._name)+" ist (Unbekannt)")
        elif self.Belegungszustand[0] == 0:
            print(str(self._name)+" ist (Frei)")
        elif self.Belegungszustand[0] == 1:
             print(str(self._name)+" ist (sehr wahscheinlich Frei)")
        elif self.Belegungszustand[0] == 2:
             print(str(self._name)+" ist (wahscheinlich Frei)")
        elif self.Belegungszustand[0] == 3:
             print(str(self._name)+" ist (wahrscheinlich Belegt)")
        elif self.Belegungszustand[0] == 4:
             print(str(self._name)+" ist (sehr wahscheinlich Belegt)")
        elif self.Belegungszustand[0] == 5:
             print(str(self._name)+" ist (Belegt)")
        return
    
    def updateZustände(self,Zustand):

        #Updated die Zustandsliste wenn ein neuer Scan gemacht wird

        self.Zustände[0,4] =  self.Zustände[0,3]
        self.Zustände[0,3] =  self.Zustände[0,2]
        self.Zustände[0,2] =  self.Zustände[0,1]
        self.Zustände[0,1] =  self.Zustände[0,0]
        self.Zustände[0,0] =  Zustand

        self.Zustände[1,4] =  self.Zustände[1,3]
        self.Zustände[1,3] =  self.Zustände[1,2]
        self.Zustände[1,2] =  self.Zustände[1,1]
        self.Zustände[1,1] =  self.Zustände[1,0]
        self.Zustände[1,0] =  time.time()

        return 
    

#Funktionen: 

#Für automatische Bewegung des Roboters 
    
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



def countPoints(array,PS):

    #Funkton zählt die Punkte die innerhalb eines Parkplatzes vom Lidar Sensor gemessen werden
    
    Zeilen = len(array)
    count1 = 0

    for i in range (0,Zeilen): 

        if array[i,0] >= PS[1,0] and array[i,0] <=PS[0,0]and array[i,1] >= PS[1,1] and array[i,1] <=PS[0,1] and array[i,2] >= PS[1,2] and array[i,2] <=PS[0,2]:
            count1=count1+1

    return count1 



def createparkingspace(Parkplatz):

    #Funktin definiert die Fläche eines Parkplatzes in Relation zur Position des Roboters

    global InnokHeros

    #Maße eines deutschen Parkplatzes sind 5m x 2,3m 
    Parkplatzmaße = [5,2.3]

    # Höhe des definierten Parkplatzes in Metern
    MaxZ = 4

    #Höhe des Lidar Sensors über dem Boden in Metern
    LidarPos = 0.85

    DV = InnokHeros.differenzvektor(Parkplatz)
    PH = [DV[0]+(Parkplatzmaße[0]/2),DV[1]+(Parkplatzmaße[1]/2)]
    PL = [DV[0]-(Parkplatzmaße[0]/2),DV[1]-(Parkplatzmaße[1]/2)]
    PSpace = [[PH[0],PH[1],MaxZ-LidarPos],[PL[0],PL[1],-LidarPos]]
    PSpace = numpy.array(PSpace)
    return PSpace

def checknearest():

    #Funktion um die 3 nächsten Parkplätze herauszufinden

    global Parkplätze
    global InnokHeros

    V1 = InnokHeros.differenzvektor(Parkplätze["1"])
    V2 = InnokHeros.differenzvektor(Parkplätze["2"])
    V3 = InnokHeros.differenzvektor(Parkplätze["3"])
    V4 = InnokHeros.differenzvektor(Parkplätze["4"])
    V5 = InnokHeros.differenzvektor(Parkplätze["5"])
    V6 = InnokHeros.differenzvektor(Parkplätze["6"])
    V7 = InnokHeros.differenzvektor(Parkplätze["7"])
    V8 = InnokHeros.differenzvektor(Parkplätze["8"])
    V9 = InnokHeros.differenzvektor(Parkplätze["9"])
    V10 = InnokHeros.differenzvektor(Parkplätze["10"])
    V11 = InnokHeros.differenzvektor(Parkplätze["11"])
    V12 = InnokHeros.differenzvektor(Parkplätze["12"])
    V13 = InnokHeros.differenzvektor(Parkplätze["13"])
    V14 = InnokHeros.differenzvektor(Parkplätze["14"])
    V15 = InnokHeros.differenzvektor(Parkplätze["15"])
    V16 = InnokHeros.differenzvektor(Parkplätze["16"])

    D1 = math.sqrt(sum(i*i for i in V1))
    D2 = math.sqrt(sum(i*i for i in V2))
    D3 = math.sqrt(sum(i*i for i in V3))
    D4 = math.sqrt(sum(i*i for i in V4))
    D5 = math.sqrt(sum(i*i for i in V5))
    D6 = math.sqrt(sum(i*i for i in V6))
    D7 = math.sqrt(sum(i*i for i in V7))
    D8 = math.sqrt(sum(i*i for i in V8))
    D9 = math.sqrt(sum(i*i for i in V9))
    D10 = math.sqrt(sum(i*i for i in V10))
    D11 = math.sqrt(sum(i*i for i in V11))
    D12 = math.sqrt(sum(i*i for i in V12))
    D13 = math.sqrt(sum(i*i for i in V13))
    D14 = math.sqrt(sum(i*i for i in V14))
    D15 = math.sqrt(sum(i*i for i in V15))
    D16 = math.sqrt(sum(i*i for i in V16))

    D = {'1': D1,'2': D2,'3': D3,'4': D4,'5': D5,'6': D6,'7': D7,'8': D8,'9': D9,'10': D10,'11': D11,'12': D12,'13': D13,'14': D14,'15': D15,'16': D16,}
    Dsort = sorted(D.items(),key = lambda x:x[1])

    I = [0,0,0]

    I[0] = Dsort[0][0]
    I[1] = Dsort[1][0]
    I[2] = Dsort[2][0]

    return I

    #return Parkplätze[str(I1)],Parkplätze[str(I2)],Parkplätze[str(I3)]


def istBelegt(PSpace):

    #Funktion überprüft ob ein einzelner Parkplatz belegt ist oder nicht
    
    pcl2 = rospy.wait_for_message("/lidar_sensor/scan",PointCloud2,timeout=2)

    rotarray = transform_pointcloud(pcl2)

    xyz_array = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(rotarray)
    xyz_array = numpy.array(xyz_array)

    
    Points = countPoints(xyz_array,PSpace)
    print("Punkte gemessen: " +str(Points))

    #treshhold Wählen. Anzahl an Punkten die im ParkingSpace empfangen werden müssen bevor der Parkplatz als belegt gillt.
    
    treshhold = 20
    

    if Points >= treshhold:
        return 1
    elif  Points < treshhold:
        return 0



def transform_pointcloud(pointcloud):

    #Funktion um die Pointcloud über den yaw wert des Roboters zu rotieren.

    trans = geometry_msgs.msg.TransformStamped()
    trans.header.stamp = pointcloud.header.stamp
    trans.header.frame_id = pointcloud.header.frame_id
    trans.header.seq = pointcloud.header.seq
    trans.child_frame_id = "rotation"
    trans.transform.translation.x = 0
    trans.transform.translation.y = 0
    trans.transform.translation.z = 0
    quat = tf.transformations.quaternion_from_euler(0,0,InnokHeros.r)
    trans.transform.rotation.x = quat[0]
    trans.transform.rotation.y = quat[1]
    trans.transform.rotation.z = quat[2]
    trans.transform.rotation.w = quat[3]

    newpointcloud = do_transform_cloud(pointcloud, trans)
    return newpointcloud


def checkparking():

    #Die Funktion ermittelt die nächsten 3 Parkplätze und überprüft ob diese Frei oder Belegt sind

    print("Starting Parking Space Scan... ")

    global Parkplätze
    global InnokHeros

    InnokHeros.get_model_state()
    Parkplätze["1"].get_model_state()
    Parkplätze["2"].get_model_state()
    Parkplätze["3"].get_model_state()
    Parkplätze["4"].get_model_state()
    Parkplätze["5"].get_model_state()
    Parkplätze["6"].get_model_state()
    Parkplätze["7"].get_model_state()
    Parkplätze["8"].get_model_state()
    Parkplätze["9"].get_model_state()
    Parkplätze["10"].get_model_state()
    Parkplätze["11"].get_model_state()
    Parkplätze["12"].get_model_state()
    Parkplätze["13"].get_model_state()
    Parkplätze["14"].get_model_state()
    Parkplätze["15"].get_model_state()
    Parkplätze["16"].get_model_state()

    PSpaces = {'1':createparkingspace(Parkplätze["1"]),'2':createparkingspace(Parkplätze["2"]),'3':createparkingspace(Parkplätze["3"]),'4':createparkingspace(Parkplätze["4"]),'5':createparkingspace(Parkplätze["5"]),'6':createparkingspace(Parkplätze["6"]),'7':createparkingspace(Parkplätze["7"]),'8':createparkingspace(Parkplätze["8"]),'9':createparkingspace(Parkplätze["9"]),'10':createparkingspace(Parkplätze["10"]),'11':createparkingspace(Parkplätze["11"]),'12':createparkingspace(Parkplätze["12"]),'13':createparkingspace(Parkplätze["13"]),'14':createparkingspace(Parkplätze["14"]),'15':createparkingspace(Parkplätze["15"]),'16':createparkingspace(Parkplätze["16"])}

    NP  = checknearest()

    print("3 Nearest Parking Spaces are Numbers "+str(NP))

    Parkplätze[NP[0]].updateZustände(istBelegt(PSpaces[NP[0]]))
    Parkplätze[NP[1]].updateZustände(istBelegt(PSpaces[NP[1]]))
    Parkplätze[NP[2]].updateZustände(istBelegt(PSpaces[NP[2]]))

    Parkplätze["1"].calculateZustand()
    Parkplätze["2"].calculateZustand()
    Parkplätze["3"].calculateZustand()
    Parkplätze["4"].calculateZustand()
    Parkplätze["5"].calculateZustand()
    Parkplätze["6"].calculateZustand()
    Parkplätze["7"].calculateZustand()
    Parkplätze["8"].calculateZustand()
    Parkplätze["9"].calculateZustand()
    Parkplätze["10"].calculateZustand()
    Parkplätze["11"].calculateZustand()
    Parkplätze["12"].calculateZustand()
    Parkplätze["13"].calculateZustand()
    Parkplätze["14"].calculateZustand()
    Parkplätze["15"].calculateZustand()
    Parkplätze["16"].calculateZustand()

    Parkplätze["1"].displayZustand()
    Parkplätze["2"].displayZustand()
    Parkplätze["3"].displayZustand()
    Parkplätze["4"].displayZustand()
    Parkplätze["5"].displayZustand()
    Parkplätze["6"].displayZustand()
    Parkplätze["7"].displayZustand()
    Parkplätze["8"].displayZustand()
    Parkplätze["9"].displayZustand()
    Parkplätze["10"].displayZustand()
    Parkplätze["11"].displayZustand()
    Parkplätze["12"].displayZustand()
    Parkplätze["13"].displayZustand()
    Parkplätze["14"].displayZustand()
    Parkplätze["15"].displayZustand()
    Parkplätze["16"].displayZustand()
   
    return 

def send():

    #Die Funktion veröffentlich den Belegungszustand der Parkplätze auf einem Ros Topic

    message = str(Parkplätze["1"].Belegungszustand)+str(Parkplätze["2"].Belegungszustand)+str(Parkplätze["3"].Belegungszustand)+str(Parkplätze["4"].Belegungszustand)+str(Parkplätze["5"].Belegungszustand)+str(Parkplätze["6"].Belegungszustand)+str(Parkplätze["7"].Belegungszustand)+str(Parkplätze["8"].Belegungszustand)+str(Parkplätze["9"].Belegungszustand)+str(Parkplätze["10"].Belegungszustand)+str(Parkplätze["11"].Belegungszustand)+str(Parkplätze["12"].Belegungszustand)+str(Parkplätze["13"].Belegungszustand)+str(Parkplätze["14"].Belegungszustand)+str(Parkplätze["15"].Belegungszustand)+str(Parkplätze["16"].Belegungszustand)

    pub2.publish(message)


    return


def signal_handler(signal, frame):
    #Funktion mit der man das Programm per STRG + C "gracefully" beenden kann. 
    print("\nprogram exiting gracefully")
    sys.exit(0)



#Variablen: 

msgl = Twist()
msgl.angular.z = 1.0
msgr = Twist()
msgr.angular.z = -1.0
msgg = Twist()
msgg.linear.x = 1.0

InnokHeros = GModel('innok_heros','link')
Parkplatz1 = GModel('Parkplatz 5x2.3','link')
Parkplatz2 = GModel('Parkplatz 5x2.3_0','link')
Parkplatz3 = GModel('Parkplatz 5x2.3_1','link')
Parkplatz4 = GModel('Parkplatz 5x2.3_2','link')
Parkplatz5 = GModel('Parkplatz 5x2.3_3','link')
Parkplatz6 = GModel('Parkplatz 5x2.3_3_clone','link')
Parkplatz7 = GModel('Parkplatz 5x2.3_3_clone_0','link')
Parkplatz8 = GModel('Parkplatz 5x2.3_3_clone_1','link')
Parkplatz9 = GModel('Parkplatz 5x2.3_3_clone_2','link')
Parkplatz10 = GModel('Parkplatz 5x2.3_3_clone_3','link')
Parkplatz11 = GModel('Parkplatz 5x2.3_3_clone_4','link')
Parkplatz12 = GModel('Parkplatz 5x2.3_3_clone_5','link')
Parkplatz13 = GModel('Parkplatz 5x2.3_3_clone_6','link')
Parkplatz14 = GModel('Parkplatz 5x2.3_3_clone_7','link')
Parkplatz15 = GModel('Parkplatz 5x2.3_3_clone_8','link')
Parkplatz16 = GModel('Parkplatz 5x2.3_3_clone_9','link')


Parkplätze = {'1':Parkplatz1,'2':Parkplatz2,'3':Parkplatz3,'4':Parkplatz4,'5':Parkplatz5,'6':Parkplatz6,'7':Parkplatz7,'8':Parkplatz8,'9':Parkplatz9,'10':Parkplatz10,'11':Parkplatz11,'12':Parkplatz12,'13':Parkplatz13,'14':Parkplatz14,'15':Parkplatz15,'16':Parkplatz16}


if __name__ == '__main__':

    rospy.init_node("main")

    rate = rospy.Rate(100)

    signal.signal(signal.SIGINT, signal_handler)

    pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

    pub2 = rospy.Publisher("/Belegung", String, queue_size=10)

    while(True):

        checkparking()
        send()
        pause(50)














 




    

    
    

    
    


    






    