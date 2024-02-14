![tubi on raspberry pi](./raspberry_pi_tubi.GIF)

This was some script to watch movies on tubi after SSH into the Raspberry Pi.

Once in the raspberry pi, from the terminal launch this file with "python main.py". 
Make sure you have "cd" to the right directory and have any packages installed that are needed.

Audio Note: Static was encountered on our Bluetooth speaker that was connected to the Raspberry Pi 4 model b.
To avoid that, open the config file with "sudo nano /boot/config.txt" and add this line to the config.txt file:
"audio_pwm_mode=2"

Code Note: This code is somewhat dependent on the current UI layout of the tubi site, so you may need to update it.



