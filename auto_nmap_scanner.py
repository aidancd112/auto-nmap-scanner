from os import system
system("clear")
print("If you do not have nmap installed, please install it before use of this application (if you are using linux, you can type install into the press enter to continue, it will install for you :)")
buffer_input = input("press enter")
if buffer_input == "install":
	system("sudo apt install nmap")
else:
	check_for_ips_or_scan_input = input("would you like to scan an ip or would you like to check for ips? (check/scan): ")
	if check_for_ips_or_scan_input == "scan":
		private_public_input = input("would you like to scan a public ip or private ip (pu/pr): ")
		if private_public_input == "pr":
			ip_input = input("please enter the last section of the private ip adress: ")
			system("clear")
			system("sudo nmap -v -sS -O 192.168.1."+ip_input)
		if private_public_input == "pu":
			ip_input = input("what ip would you like to scan?: ")
			system("clear")
			system("sudo nmap -v -sS -O "+ip_input)
	if check_for_ips_or_scan_input == "check":
		system("clear")
		system("nmap -v -sn 192.168.1.1/24 192.168.1.254/24")