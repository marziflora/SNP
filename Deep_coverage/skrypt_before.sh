z=$(wc -l $1 | awk '{print $1}')

for ((i=2; i<=z; i++)); do
        chr=$(sed -n "$i""p" $1 | awk '{print $1}') 
        end=$(sed -n "$i""p" $1 | awk '{print $2}')
	begin=$((end-500))
        name=$chr+$begin+$end+$1
        if (( $chr == 30 )); then
        chr=$"X"
        fi 
        samtools depth -r Chr$chr:$begin-$end $2 >> before+$name
done

