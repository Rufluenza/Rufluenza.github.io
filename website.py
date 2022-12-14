import streamlit as st
import os

dev = {}
devs = {}
def get_usb():
    i = 0
    if os.path.exists('/dev/disk/by-label'):
        for dev in os.listdir('/dev/disk/by-label'):
            if dev != "ESP" and dev != "EFI":
                i += 1
                l = '/dev/disk/by-label/'+dev
                devs[i] = l

    return devs


st.header("Xmount eject")
st.subheader("Eject your USB devices")
def main():
    for i in range(len(get_usb())):
        l = str(i)
        st.write(get_usb()[i+1].split('/')[-1])
        st.container()
        l = st.button('Eject ' + 'Nr. '+l+' ' + get_usb()[i+1].split('/')[-1])
        if l:
            st.write('ejecting'+ ' ' + get_usb()[i+1])
            os.system('udisksctl unmount --block-device '+get_usb()[i+1])
            if os.system('udisksctl power-off --block-device '+get_usb()[i+1]) == 0:
                st.write('Ejected'+ ' ' + get_usb()[i+1].split('/')[-1])
                st.write('Reload the page to see the changes.  ')
                # refresh the page from the server side

    
if __name__ == "__main__":
    main()
