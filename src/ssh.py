import paramiko

class SSHControl:
    def __init__(self, ip, user, pwd):
        self._ssh_ip = ip
        self._ssh_user = user
        self._ssh_pwd = pwd

        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def __enter__(self):
        self._ssh.connect(self._ssh_ip, username=self._ssh_user, password=self._ssh_pwd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._ssh.close()

    def connection_possible(self) -> bool:
        """
        Trying to establish a connection to the SSH server.

        .. warning:: Calling this method does not lead to an open connection. It should not be
                     called using the ``with``-statement!

        :return: ``True`` when connection is possible, ``False`` otherwise
        """
        try:
            self._ssh.connect(self._ssh_ip, username='', password='')
            self._ssh.close()
            return True
        except paramiko.ssh_exception.AuthenticationException:
            return True
        except Exception:
            return False

    def get_file(self, remote_path, local_path):
        """ Download file. """
        ftp_client = self._ssh.open_sftp()
        try:
            ftp_client.get(remote_path, local_path)
        finally:
            ftp_client.close()

    def put_file(self, local_path, remote_path):
        """ Upload file. """
        ftp_client = self._ssh.open_sftp()
        try:
            ftp_client.put(local_path, remote_path)
        finally:
            ftp_client.close()

    def send_cmd(self, cmd):
        """ Sends a shell cmd via SSH and reads the answer """
        # execute command
        _, stdout, stderr = self._ssh.exec_command(cmd)
        # read and return answers
        return stdout.readlines(), stderr.readlines()