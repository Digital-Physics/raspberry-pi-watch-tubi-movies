![tubi on raspberry pi](./raspberry_pi_tubi.GIF)

This is some script to watch movies on tubi and youtube. It is helpful if you SSH into your Raspberry Pi (with wifi capabilities).

Once in the raspberry pi terminal, navigate to where you have saved this file and run it with "python main.py". 

Update the the movie URL in the file as desidre on your Raspberry Pi using "nano main.py"

Audio Note: Static was encountered on our Bluetooth speaker that was connected to the Raspberry Pi 4 model b.
To avoid it, open the config file with "sudo nano /boot/config.txt" and add this line to the config.txt file:
"audio_pwm_mode=2"

Code Note: This code is somewhat dependent on the current tubi and youtube UI, so you may need to update it if things change.



