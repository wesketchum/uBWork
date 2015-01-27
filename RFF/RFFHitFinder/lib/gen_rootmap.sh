#!/bin/bash

temp=make_rootmap.$$.temp

rootlibmap() {
 ROOTMAP=$1
 SOFILE=$2
 LINKDEF=$3
 shift 3
 DEPS=$*
 if [[ -e $SOFILE && -e $LINKDEF ]]; then
     rlibmap -f -o $ROOTMAP -l $SOFILE -d $DEPS -c $LINKDEF 2>> $temp
     rm -f $temp
 fi
}

######################################################
# RFFHitFinder
rootlibmap libRFF_RFFHitFinder.rootmap libRFF_RFFHitFinder.so $LARLITE_USERDEVDIR/RFF/RFFHitFinder/LinkDef.h 
