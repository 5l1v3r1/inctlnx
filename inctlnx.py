from time import sleep
from colorama import Fore, init
import paramiko

init(autoreset=True)

class Incresp():
    def __init__(self):
        self.__str__()
        self.RESPONSE = ""
        self.Run()

    def __str__(self):
        print(Fore.LIGHTGREEN_EX + """
        
        █░░ █ █▄░█ █░█ ▀▄▀   █ █▄░█ █▀▀ █ █▀▄ █▀▀ █▄░█ ▀█▀   █▀█ █▀▀ █▀ █▀█ █▀█ █▄░█ █▀ █▀▀
        █▄▄ █ █░▀█ █▄█ █░█   █ █░▀█ █▄▄ █ █▄▀ ██▄ █░▀█ ░█░   █▀▄ ██▄ ▄█ █▀▀ █▄█ █░▀█ ▄█ ██▄

              𝔸𝕦𝕥𝕙𝕠𝕣: 𝑬𝒎𝒓𝒆 𝑲𝒐𝒚𝒃𝒂𝒔𝒊
              𝒉𝒕𝒕𝒑𝒔://𝒈𝒊𝒕𝒉𝒖𝒃.𝒄𝒐𝒎/𝒆𝒎𝒓𝒆𝒌𝒚𝒃𝒔

       														 """)

    def Run(self):
        sleep(2)
        with open('credential.txt') as f:
            lines = f.readlines()
            for line in lines:
                IP_address, user, passw = line.strip().split("|")
                print(IP_address, "-", user, "-", passw)
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(IP_address, username=user, password=passw)

                commands = [
                    "cat /etc/passwd",
                    "cat /etc/shadow",
                    "cat /etc/group",
                    "cat /etc/sudoers",
                    "lastlog",
                    "cat /var/log/auth.log",
                    "uptime",
                    "cat /proc/meminfo",
                    "ps aux",
                    "cat /etc/resolv.conf",
                    "cat /etc/hosts",
                    "iptables -L -v -n",
                    "service --status-all",
                    "find / -type f -size +512k -exec ls -lh {}/;",
                    "find / -mtime -1 -ls",
                    "ip a",
                    "netstat -nap",
                    "arp -a",
                    "echo $PATH"
                ]

                try:
                    for command in commands:
                        stdin, stdout, stderr = ssh.exec_command(command)
                        output = stdout.read().decode()

                        self.RESPONSE += f"{command}:\n{output}"
                        print(Fore.LIGHTRED_EX + f"{command}:\n")
                        print(output)
                        print("\n\n\n")
                except Exception as e:
                    print(e)
                finally:
                    with open("report.txt", "w") as file:
                        file.write(self.RESPONSE)

                ssh.close()
                print("Result saved in report.txt\n")


incresp = Incresp()
