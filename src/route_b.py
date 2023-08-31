# from paramiko import SSHClient

# client = SSHClient()

# try:
#     client.connect('172.290.10.4', username='pi', password='raspberry')
# except:
#     print("Error")
# finally:
#     client.close()

import ssh
    
print('Hi')

ssh_client = ssh.SSHControl("172.20.10.4", "pi", "raspberry")
with ssh_client:
    print(ssh_client.send_cmd('cd /home/pi/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi'))
    print(ssh_client.send_cmd('ls'))
    # print(ssh_client.send_cmd('sudo python LightXX2.py'))

print('Bye')