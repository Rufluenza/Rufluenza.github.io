import streamlit as st
import os
import json

# mtp = mountpoint
debug = True
devices = {}
mtp = {}

dev = {}
devs = {}
def get_usb():
    i = 0
    for dev in os.listdir('/dev/disk/by-label'):
        if dev != "ESP" and dev != "EFI":
            i += 1
            dev[i] = os.path.realpath('/dev/disk/by-label/'+dev)
            
            # devs[i] = '/Volumes/'+dev
            #devs.append((dev, '/Volumes/'+dev))
    return devs


# st.write(get_usb())

def get_name():
    if debug == True:
        for i in range(5):
            # write a fake device to the devices.json file
            num = str(i)
            devices[i] = str('usb_name'+num)
            
    return devices

def get_mtp():
    if debug == True:
        for i in range(5):
            # write a fake device to the devices.json file
            num = str(i)
            mtp[i] = str('/dev/sd'+num)
            
    return mtp
# make a box for each device in the devices list and put the device name in the box with a eject button

        


st.header("Xmount eject")
st.subheader("Eject your USB devices")
for i in range(len(get_usb())):
    # all_names = get_name()[i]
    st.write(get_usb()[i+1].split('/')[-1])
    st.container() # make a container for each device
    if st.button('Eject' + ' ' + get_usb()[i+1].split('/')[-1]):
        st.write('ejecting'+ ' ' + get_usb()[i+1])
        if os.system('diskutil eject '+get_usb()) == 0: # if the command is successful maybe delete the if statement "sudo -S umount" on linux
            st.write('Ejected'+ ' ' + get_usb()[i+1].split('/')[-1])

        








# make a web page with all the devices listed
