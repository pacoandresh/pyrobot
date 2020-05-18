#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________


import time
from  threading import Thread
from PYRobot.utils.utils import get_ip_port
from PYRobot.libs.comunications import Mqtt_Sub,Broadcast_Sub
import json


class Suscriptions(object):
    def __init__(self,name,mqtt_uri,broadcast,mqtt_handler,broad_handler,qos=0):
        self.host,self.mqtt_port=get_ip_port(mqtt_uri)
        self.qos=0
        self.broadcast_port=broadcast
        self.robot,self.comp=name.split("/")
        self.suscribers={}
        self.first=[]
        self.mqtt_enable=False
        self.broadcast_enable=False
        self.mqtt_handler=mqtt_handler
        self.broad_handler=broad_handler
        
        
    def Start(self):
        if len(self.suscribers)>0:
            print("suscriptions started")
            self.mqtt = Mqtt_Sub(self.host,self.mqtt_port,self.mqtt_handler,self.qos)
            self.mqtt.connect(self.suscribers)
            self.broadcast=Broadcast_Sub(self.host,self.broadcast_port,on_handler=self.broad_handler,qos=self.qos)

    def add_suscribers(self,**suscriptions):
        for s,l in suscriptions.items():
            self.add_suscriber(l,s)

    def add_suscriber(self,suscriber,link):
        self.suscribers[suscriber]=link
        self.first.append(suscriber)
        
    def del_first(self,suscriber):
        if suscriber in self.first:
            self.first.remove(suscriber)

    def get_first(self):
        return self.first
    
    def get_suscribers(self):
        return self.suscribers


    
