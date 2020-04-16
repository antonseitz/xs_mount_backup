#!/bin/python
import os
execfile( "helper.py")

mountdir="/xenbackup"
banner("Mount Point " + mountdir)
go=ask("Should we make mount point for " + mountdir +" ?")
if go=="":
	if os.system("mkdir " + mountdir ) > 0:
		exit(1)


if os.system("df | grep " + mountdir) ==0:

	go=ask("Should we unmount  " + mountdir +" ?")
	if go=="":
		if os.system("umount  " + mountdir ) > 0:
			print("error unmounting" + mountdir)
			exit(1)


nfs=ask("USB HDD (u) or NFS (n) [default]  ? ")
if (nfs==""  or nfs=="n"):
	nfs_server=ask_text("enter IP oder FQDN of NFS Server: ")
	if(nfs_server==""):
		print("Error: no server given!")
		exit(1)
	
	print("Output from rcpinfo: \n")
	er=os.system("rpcinfo -p " + nfs_server +" | grep nfs")
	
	print("Output from showmount: \n")
	er+=os.system("showmount -e " + nfs_server )
			
	if er>0: 
		print("Error while connecting!")
		exit(1)
	
	
	nfs_share=ask_text("enter path of NFS Share: ")
	
	banner("Try mounting NFS...")
	print("mount -t nfs " + nfs_server + ":" + nfs_share  + mountdir )
	if 0 < os.system("mount -t nfs " + nfs_server + ":" + nfs_share + " " + mountdir ):
		print("Error while mounting")
		exit(1)
	else:
		if 0<os.system("umount " + mountdir):
			print("Error unmounting")
			exit(1)
		if ask("Should we insert mount in fstab ?")=="":
			fstab=open("/etc/fstab","a")
			fstab.write("## ENTRY for " + mountdir + "  -Partition\n")
		
			fstab.write( nfs_server + ":" + nfs_share +" " +mountdir + " nfs defaults,noauto 0 2\n" )
			fstab.close()
			print(mountdir + " is now in fstab ")
		mount=ask("Should we mount " + mountdir + " ?")
		if mount=="":
			if 0<os.system("mount " + mountdir):
				print("mounting " + mountdir + " failed!")
				exit(1)
			
if (nfs=="u"):
	print("\nList of USB-HDDS: \n")
	os.system("ls -l /dev/disk/by-path/ | grep usb")
	print("\nList of UUIDS: \n")
	os.system("ls -l /dev/disk/by-uuid/ | grep sd")
	
	usbhdd=ask_text("enter path or UUID (better) of USB partition [/dev/sdx1| xxxxx-xxxx-xxx-xxx ]: ")
	if not usbhdd.startswith("/"):
		usbhdd="UUID="+usbhdd
	print(usbhdd)
	banner("Try mounting USB HDD...")
	print("mount -t ext4 " + usbhdd + " " + mountdir )
	if 0 < os.system("mount -t ext4 " + usbhdd + " " + mountdir ):
		print("\nError while mounting")
		exit(1)
	else:
		print( usbhdd + " was successfully mounted!\n")
		if ""==ask("Should we unmount it ?"):
		
			if 0<os.system("umount " + mountdir):
				print("\nError unmounting")
				exit(1)
		if ask("Should we insert mount in fstab ?")=="":
			fstab=open("/etc/fstab","a")
			fstab.write("## ENTRY for " + mountdir + "  -Partition\n")
		
			fstab.write( usbhdd + " " + mountdir + " ext4 defaults,noauto 0 2\n" )
			fstab.close()
			print(mountdir + " is now in fstab ")
		mount=ask("Should we mount " + mountdir + " ?")
		if mount=="":
			if 0<os.system("mount " + mountdir):
				print("mounting " + mountdir + " failed!")
				exit(1)
	

 
print("/etc/fstab Output : \n")
os.system("cat /etc/fstab")
print("\nfinished!")