names=$(cat congress_screen_names.txt) 

while true; do
    for line in $names; do
	  t timeline -n 1 --csv $line | grep '^[0-9]' >> tmp.csv
	  sleep 6
  done
done