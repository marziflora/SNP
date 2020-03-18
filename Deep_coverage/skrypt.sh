z=$(wc -l $1 | awk '{print $1}')

for ((i=2; i<=z; i++)); do
        chr=$(sed -n "$i""p" $1 | awk '{print $1}') 
        begin=$(sed -n "$i""p" $1 | awk '{print $2}')
        end=$(sed -n "$i""p" $1 | awk '{print $3}')
        name=$chr+$begin+$end+$1
        if (( $chr == 30 )); then
	chr=$"X"
        fi 
        samtools depth -r Chr$chr:$begin-$end $2 >> result+$name
done


