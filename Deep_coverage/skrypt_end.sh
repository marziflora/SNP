z=$(wc -l $1 | awk '{print $1}')

for ((i=2; i<=z; i++)); do
        chr=$(sed -n "$i""p" $1 | awk '{print $1}') 
	begin=$(sed -n "$i""p" $1 | awk '{print $3}')
	end=$((begin+500))	
        if (( $chr == 30 )); then
        chr=$"X"
        fi 
	name=$chr+$begin+$end+$1
        samtools depth -r Chr$chr:$begin-$end $2 >> after+$name
done

