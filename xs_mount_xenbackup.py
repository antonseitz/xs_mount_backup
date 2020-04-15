#!/bin/python
import os
execfile( "helper.py")

mountdir="/xenbackup"
banner("Mount Point " + mountdir)
go=ask("Should we make mount point for " + mountdir +" ?")
if go=="":
	if os.system("mkdir " + mountdir ) < 0:
		exit(1)
	
	nfs=ask("LokalHDD (l) or NFS (n) [default]  ? ")
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
		os.system("mount -t nfs " + nfs_server + ":" + nfs_share  + mountdir )
		
		# fstab=open("/etc/fstab",a)
		# fstab.write("## ENTRY for /xenbackup -Partition")
		
		# fstab.write( nfsserver + ":" + nfs_share +" /xenbackup nfs defaults,noauto 0 2" )
		# fstab.close()









# echo " /dev/disk/by-path/ : "
# echo
 # ls -la /dev/disk/by-path/
 
 # echo " /dev/disk/by-uuid :"
 # echo
 # ls -la /dev/disk/by-uuid
 
 # echo 
 # echo " blkid  :"
 # blkid
 
 # echo 
 # echo " by-id  :"
 # ls -la /dev/disk/by-id
 
 
 # echo
 
 
 # echo
 # echo
 # red
 # read -rsp $'Copy UUID from above for Pasting in /etc/fstab ...\n' -n1
 # nor
 
 
 # UUID findet man unter /dev/disk/by-uuid 
 # echo "## ENTRY for /snapshots -Partition"  >> /etc/fstab
 # echo "UUID=COPY-HERE_UUID /snapshots ext4 defaults,noauto 0 2" >> /etc/fstab
 
 # nano /etc/fstab
 