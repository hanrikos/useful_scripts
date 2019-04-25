#!/bin/bash

# Description	: Download files using curl.

echo "Enter the name of your flat file: "
read input_variable
echo "You entered: $input_variable"

#create urls variable array
declare urls=( `cat "$input_variable" `)

#Download files from URL list
for m in "${urls[@]}"
	do curl -O "$m"
done