
#! /bin/python3

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
import pymap3d as pm
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PoseWithCovarianceStamped 

#Klassen:

class GModel:

    def __init__(self, name):
        self._name = name
        self.gps = NavSatFix()
        self.Zustände = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.Zustände = numpy.array(self.Zustände)
        self.Belegungszustand = [0,0]



    def get_model_state(self):

        #Angepasst auf GPS Topic

        self.gps = rospy.wait_for_message("gps/fix",NavSatFix,timeout=5)
        self.pose = rospy.wait_for_message("utm_local",PoseWithCovarianceStamped,timeout=5)
        x = self.pose.pose.pose.orientation.x
        y = self.pose.pose.pose.orientation.y
        z = self.pose.pose.pose.orientation.z
        w = self.pose.pose.pose.orientation.w
        self.yaw = euler_from_quaternion(x,y,z,w)[2]
        


        # Extra Code um die Position des Roboters um 40 cm nach hinten zu setzen. Weil TF der Antenne unklar
        #vf = [1,0]
        #fixl = [((0.4)/length(vf))*vf[0],((0.4)/length(vf))*vf[1]]
        #fixa = [fixl[0]*math.cos(self.yaw+math.pi)-fixl[1]*math.sin(self.yaw+math.pi),fixl[0]*math.sin(self.yaw+math.pi)+fixl[1]*math.cos(self.yaw+math.pi)]
        #fixp = pm.enu2geodetic(fixa[0],fixa[1],0,self.gps.latitude,self.gps.longitude,0)

        #elf.gps.latitude = fixp[0]
        #self.gps.longitude = fixp[1]
    

    def differenzvektor(self,GModel):
        #Angepasst an Lat/Long Koordinaten
        Vektor = pm.geodetic2enu(GModel.gps.latitude, GModel.gps.longitude, 0, self.gps.latitude, self.gps.longitude, 0)
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

def pause(amount):
       x=0
       for x in range (0,amount):
          rate.sleep()
          x+1

#Vektorfunktionen

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def vec (v1,v2):
    #Weg von V1 nach V2
    r =[0,0]
    r[0] = v2[0]-v1[0]
    r[1] = v2[1]-v1[1]
    return r



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
        # Höhe des definierten Parkplatzes in Metern
    MaxZ = 4

    #Höhe des Lidar Sensors über dem Boden in Metern
    LidarPos = 0.85

    #Maximal zulässige Höhe und Tiefe der zu Zählenden Punkte in Metern

    H = MaxZ-LidarPos
    L = 0.2
    

    for i in range (0,Zeilen): 

        a1 = array[i][0]
        a2 = array[i][1]

        #Erklärung für if Abfrage siehe Screenshot

        if (0 < dotproduct(vec(PS[0],[a1,a2]),vec(PS[0],PS[1])) < dotproduct(vec(PS[0],PS[1]),vec(PS[0],PS[1])) and 0 < dotproduct(vec(PS[0],[a1,a2]),vec(PS[0],PS[3])) < dotproduct(vec(PS[0],PS[3]),vec(PS[0],PS[3])) and array[i][2] > L and array[i][2] < H ):

            count1=count1+1


    return count1 



def createparkingspace(Parkplatz):

    #Funktin definiert die Fläche eines Parkplatzes in Relation zur Position des Roboters

    global InnokHeros
    global Parkplätze

    # Gemessene   Parkplatzmaße = [4.85,2.3]

    Parkplatzmaße = [4.7,2.2]


    #Yaw Winkel der Parkplätze in Referenz zu Koordinatensystem bestimmen
    PXtoPYEnu = pm.geodetic2enu(Parkplätze["5"].gps.latitude, Parkplätze["5"].gps.longitude, 0, Parkplätze["9"].gps.latitude, Parkplätze["9"].gps.longitude, 0)
    Referenzvektor = [1,0]
    Parkplatzvektor = [PXtoPYEnu[0],PXtoPYEnu[1]]
    Pyaw = -angle(Referenzvektor,Parkplatzvektor)
    #print(Pyaw)

    #um Yaw Winkel rotierte Parkplatzeckvektoren bestimmen (Vektoren die vom Mittelpunkt in die jeweiligen Ecken zeigen)

    ProtHH = [Parkplatzmaße[1]/2*math.cos(Pyaw)-Parkplatzmaße[0]/2*math.sin(Pyaw),Parkplatzmaße[1]/2*math.sin(Pyaw)+Parkplatzmaße[0]/2*math.cos(Pyaw)]
    ProtHL = [Parkplatzmaße[1]/2*math.cos(Pyaw)+Parkplatzmaße[0]/2*math.sin(Pyaw),Parkplatzmaße[1]/2*math.sin(Pyaw)-Parkplatzmaße[0]/2*math.cos(Pyaw)]
    ProtLL = [-Parkplatzmaße[1]/2*math.cos(Pyaw)+Parkplatzmaße[0]/2*math.sin(Pyaw),-Parkplatzmaße[1]/2*math.sin(Pyaw)-Parkplatzmaße[0]/2*math.cos(Pyaw)]
    ProtLH = [-Parkplatzmaße[1]/2*math.cos(Pyaw)-Parkplatzmaße[0]/2*math.sin(Pyaw),-Parkplatzmaße[1]/2*math.sin(Pyaw)+Parkplatzmaße[0]/2*math.cos(Pyaw)]

    DV = InnokHeros.differenzvektor(Parkplatz)

    #Punkt Oben Rechts rotiert
    PH = [DV[0]+ProtHH[0],DV[1]+ProtHH[1]]

    #Punkt Oben Links rotiert
    PHL = [DV[0]+ProtHL[0],DV[1]+ProtHL[1]]

    #Punkt Unten Rechts rotiert
    PL = [DV[0]+ProtLL[0],DV[1]+ProtLL[1]]

    #Punkt Unten Links rotiert
    PLH = [DV[0]+ProtLH[0],DV[1]+ProtLH[1]]

    PSpace = [[PH[0],PH[1]],[PHL[0],PHL[1]],[PL[0],PL[1]],[PLH[0],PLH[1]]]

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


    D = {'1': D1,'2': D2,'3': D3,'4': D4,'5': D5,'6': D6,'7': D7,'8': D8,'9': D9,'10': D10}
    Dsort = sorted(D.items(),key = lambda x:x[1])

    I = [0,0,0]

    I[0] = Dsort[0][0]
    I[1] = Dsort[1][0]
    I[2] = Dsort[2][0]

    return I



def istBelegt(PSpace):

    #Funktion überprüft ob ein einzelner Parkplatz belegt ist oder nicht
    
    pcl2 = rospy.wait_for_message("/hesai/pandar",PointCloud2,timeout=2)

    rotarray = transform_pointcloud(pcl2)

    xyz_array = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(rotarray)
    xyz_array = numpy.array(xyz_array)

    
    Points = countPoints(xyz_array,PSpace)
    print("Punkte gemessen: " +str(Points))

    #treshhold Wählen. Anzahl an Punkten die im ParkingSpace empfangen werden müssen bevor der Parkplatz als belegt gillt.
    
    treshhold = 150

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
    quat = tf.transformations.quaternion_from_euler(0,0,InnokHeros.yaw)
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

    PSpaces = {'1':createparkingspace(Parkplätze["1"]),'2':createparkingspace(Parkplätze["2"]),'3':createparkingspace(Parkplätze["3"]),'4':createparkingspace(Parkplätze["4"]),'5':createparkingspace(Parkplätze["5"]),'6':createparkingspace(Parkplätze["6"]),'7':createparkingspace(Parkplätze["7"]),'8':createparkingspace(Parkplätze["8"]),'9':createparkingspace(Parkplätze["9"]),'10':createparkingspace(Parkplätze["10"])}

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

    return 

def send():

    #Die Funktion veröffentlich den Belegungszustand der Parkplätze auf einem Ros Topic

    message = str(Parkplätze["1"].Belegungszustand)+" "+str(Parkplätze["2"].Belegungszustand)+" "+str(Parkplätze["3"].Belegungszustand)+" "+str(Parkplätze["4"].Belegungszustand)+" "+str(Parkplätze["5"].Belegungszustand)+" "+str(Parkplätze["6"].Belegungszustand)+" "+str(Parkplätze["7"].Belegungszustand)+" "+str(Parkplätze["8"].Belegungszustand)+" "+str(Parkplätze["9"].Belegungszustand)+" "+str(Parkplätze["10"].Belegungszustand)+" "

    pub2.publish(message)


    return


def signal_handler(signal, frame):
    #Funktion mit der man das Programm per STRG + C "gracefully" beenden kann. 
    print("\nprogram exiting gracefully")
    sys.exit(0)



#Variablen: 

InnokHeros = GModel('innok_heros')
Parkplatz1 = GModel('Parkplatz1')
Parkplatz1.gps.latitude = 51.50627735
Parkplatz1.gps.longitude = 7.45638655
Parkplatz2 = GModel('Parkplatz2')
Parkplatz2.gps.latitude = 51.50625682192889
Parkplatz2.gps.longitude = 7.456382638647902
Parkplatz3 = GModel('Parkplatz3')
Parkplatz3.gps.latitude = 51.5062370694
Parkplatz3.gps.longitude = 7.45637688889
Parkplatz4 = GModel('Parkplatz4')
Parkplatz4.gps.latitude = 51.5062153444
Parkplatz4.gps.longitude = 7.45637531944
Parkplatz5 = GModel('Parkplatz5')
Parkplatz5.gps.latitude = 51.5061945528
Parkplatz5.gps.longitude = 7.456373725
Parkplatz6 = GModel('Parkplatz6')
Parkplatz6.gps.latitude = 51.5061742
Parkplatz6.gps.longitude = 7.45637013333
Parkplatz7 = GModel('Parkplatz7')
Parkplatz7.gps.latitude = 51.5061539111
Parkplatz7.gps.longitude = 7.45636640833
Parkplatz8 = GModel('Parkplatz8')
Parkplatz8.gps.latitude = 51.50613338302848
Parkplatz8.gps.longitude = 7.456362496988469
Parkplatz9 = GModel('Parkplatz9')
Parkplatz9.gps.latitude = 51.5061130722
Parkplatz9.gps.longitude = 7.4563582
Parkplatz10 = GModel('Parkplatz10')
Parkplatz10.gps.latitude = 51.50609254412832
Parkplatz10.gps.longitude = 7.4563542886619665


Parkplätze = {'1':Parkplatz1,'2':Parkplatz2,'3':Parkplatz3,'4':Parkplatz4,'5':Parkplatz5,'6':Parkplatz6,'7':Parkplatz7,'8':Parkplatz8,'9':Parkplatz9,'10':Parkplatz10}



if __name__ == '__main__':

    rospy.init_node("main")

    rate = rospy.Rate(100)

    signal.signal(signal.SIGINT, signal_handler)

    pub2 = rospy.Publisher("/Belegung", String, queue_size=10)

    while(True):
        
        checkparking()
        send()
        pause(50)


