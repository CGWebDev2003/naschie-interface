import ssh

ssh_client = ssh.SSHControl("172.20.10.4", "pi", "raspberry")

with ssh_client:
    print(ssh_client.put_file(LOCAL_PATH, REMOTE_PATH))
