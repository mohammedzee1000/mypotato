#!/bin/bash

for bx in `vagrant box list | cut -d ' ' -f1`; do

	#echo $bx
	vagrant box remove $bx;
	vagrant box add $bx;

done
