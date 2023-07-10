[![EmreKybs](https://img.shields.io/badge/MadeBy-EmreKybs-yellow)
# Inctlnx
Linux Incident Response Tool
The purpose of this application is to enhance the efficiency of incident response procedures by gathering information from Linux operating systems.

<img src="https://github.com/emrekybs/inctlnx/blob/main/Cyber-Security-1.gif">
# Commands
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

# 𝗜𝗡𝗦𝗧𝗔𝗟𝗟𝗔𝗧𝗜𝗢𝗡 𝗜𝗡𝗦𝗧𝗥𝗨𝗖𝗧𝗜𝗢𝗡𝗦

    $ git clone https://github.com/emrekybs/inctlnx.git
    $ sudo pip3 install paramiko
    $ sudo pip3 install colorama
    
    $ python3 inctlnx
<img src="https://github.com/emrekybs/inctlnx/blob/main/inc.png">
<img src="https://github.com/emrekybs/inctlnx/blob/main/report.png">
