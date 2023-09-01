import ssh

ssh_client = ssh.SSHControl("172.20.10.4", "pi", "raspberry")
with ssh_client:
    print(ssh_client.send_cmd('sudo python /home/pi/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server/LightXX2.py'))
