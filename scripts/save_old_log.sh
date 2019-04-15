#!/bin/bash
today=`date '+%Y_%m_%d__%H_%M_%S'`;
filename="$today.csv"
cp enviro.csv ./old_logs/$filename
