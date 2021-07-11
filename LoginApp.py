import bravia_tv
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from fold_to_ascii import fold

import json

from bravia_tv import BraviaRC

from os import path

import time

class WindowManager(ScreenManager):
    pass

class IpWindow(Screen):
    ip = ObjectProperty("None")
    file = json.load(open("./config.json", "r"))
    ip_saved=file["ip"]

    def connection(self):
        if not path.exists("config.json"):
            file = open("config.json", 'w')
            json.dump({"ip": "192.168.1.", 
                        "pin": 0})
            file.close()

        file = json.load(open("./config.json", "r"))
        pin_saved=int(file["pin"])

        ip=self.ip.text
        braviarc = BraviaRC(ip)
        if ip != "192.168.1.":
            braviarc.connect(pin_saved, "openremote", "Open Bravia Remote")
            if braviarc.is_connected():
                self.parent.current="home"
                a_file = open("config.json", "w")
                json.dump({"ip": ip, "pin": pin_saved}, a_file, indent=4)
                a_file.close()
                time.sleep(0.01)
            else:
                a_file = open("config.json", "w")
                json.dump({"ip": ip, "pin": pin_saved}, a_file, indent=4)
                a_file.close()
                time.sleep(0.01)
                self.parent.current="pin"


class PinWindow(Screen):
    file = json.load(open("./config.json", "r"))
    ip_saved=file["ip"]
    pin_saved=str(file["pin"])
    pin = ObjectProperty(None)
    def connection(self):
        pin=int(self.pin.text)
        braviarc = BraviaRC(self.ip_saved)
        braviarc.connect(pin, "openremote", "Open Bravia Remote")
        if braviarc.is_connected():
            a_file = open("config.json", "w")
            json.dump({"ip": self.ip_saved, "pin": int(self.pin)}, a_file, indent=4)
            a_file.close()
            self.parent.current="home"

class HomeWindow(Screen):
    searched = ObjectProperty("None")
    file = json.load(open("./config.json", "r"))
    ip_saved=file["ip"]
    pin_saved=str(file["pin"])
    braviarc = BraviaRC(ip_saved)
    braviarc.connect(pin_saved, "openremote", "Open Bravia Remote")
    def disconnect(self):
        a_file = open("config.json", "w")
        json.dump({"ip": "", "pin": 0}, a_file, indent=4)
        a_file.close()
        self.parent.current="ip"
    def power_switch(self):
        if self.braviarc.is_connected():
            self.braviarc.turn_off()
        else:
            self.braviarc.turn_on()
    def input(self):
        self.braviarc.send_command("Input")
    def retour(self):
        self.braviarc.send_command("Return")
    def home(self):
        self.braviarc.send_command("Home")
    def up(self):
        self.braviarc.send_command("Up")
    def left(self):
        self.braviarc.send_command("Left")
    def confirm(self):
        self.braviarc.send_command("Confirm")
    def right(self):
        self.braviarc.send_command("Right")
    def netflix(self):
        self.braviarc.send_command("Netflix")
    def down(self):
        self.braviarc.send_command("Down")
    def volume_down(self):
        self.braviarc.send_command("VolumeDown")
    def volume_up(self):
        self.braviarc.send_command("VolumeUp")
    def volume_mute(self):
        self.braviarc.send_command("Mute")
    
    def channel_down(self):
        self.braviarc.send_command("ChannelDown")
    def channel_up(self):
        self.braviarc.send_command("ChannelUp")   
    def zero(self):
        self.braviarc.send_command("Num0")
    def one(self):
        self.braviarc.send_command("Num1")
    def two(self):
        self.braviarc.send_command("Num2")
    def three(self):
        self.braviarc.send_command("Num3")
    def four(self):
        self.braviarc.send_command("Num4")
    def five(self):
        self.braviarc.send_command("Num5")
    def six(self):
        self.braviarc.send_command("Num6")
    def seven(self):
        self.braviarc.send_command("Num7")
    def eight(self):
        self.braviarc.send_command("Num8")
    def nine(self):
        self.braviarc.send_command("Num9")
    def ten(self):
        self.braviarc.send_command("Num10")
    def eleven(self):
        self.braviarc.send_command("Num11")
    def twelve(self):
        self.braviarc.send_command("Num12")

    def youtube(self):
        file = json.load(open("./config.json", "r"))
        ip_saved=file["ip"]
        pin_saved=str(file["pin"])
        braviarc = BraviaRC(ip_saved)
        braviarc.connect(pin_saved, "openremote", "Open Bravia Remote")
        braviarc.load_app_list()
        braviarc.start_app('YouTube')
    def write_this_on_youtube(self):
        for i in fold(self.searched.text):
            for j in range(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '].index(i)//7):
                self.down()
            for j in range(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '].index(i)%7):
                self.right()
            self.confirm()
            for j in range(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '].index(i)//7):
                self.up()
            for j in range(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '].index(i)%7):
                self.left()

    def write_this_on_netflix(self):
        for i in fold(self.searched.text):
            for j in range(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', "nul", "nul", 'w', 'x', 'c', 'v', 'b', 'n'].index(i)//10):
                self.braviarc.send_command("Down")
            for j in range(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', "nul", "nul", 'w', 'x', 'c', 'v', 'b', 'n'].index(i)%10+1):
                self.braviarc.send_command("Right")
            self.confirm()
            for j in range(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', "nul", "nul", 'w', 'x', 'c', 'v', 'b', 'n'].index(i)//10):
                self.braviarc.send_command("Up")
                
            for j in range(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', "nul", "nul", 'w', 'x', 'c', 'v', 'b', 'n'].index(i)%10+1):
                self.braviarc.send_command("Left")
        


class MyApp(App):
    def build(self):
        return Builder.load_file("my.kv")
    
MyApp().run()