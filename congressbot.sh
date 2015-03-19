file=tmp.csv

while true; do

	h=$(uniq $file | grep `date +%y-%m-%d` | sort | \
	  tr '[[:upper:]]' '[[:lower:]]' | \
	  grep -oE '#[a-z_-]+' | \
	  sort | uniq -c | sort -nr | head -1 | sed 's/^ *[0-9]* //')

	t update "Congress' most-used hastag today was \"$h\""

	u=$(uniq $file | grep `date +%y-%m-%d` | sort | \
	  tr '[[:upper:]]' '[[:lower:]]' | \
	  grep -oE '@[a-z_-]+' | \
	  sort | uniq -c | sort -nr | head -1 | sed 's/^ *[0-9]* //')

	t update "Congress' most-mentioned Twitter user today was $u"

	w=$(uniq $file | grep `date +%y-%m-%d` | sort | \
	  tr '[[:upper:]]' '[[:lower:]]' | \
	  sed 's/@/1/' | sed 's/#/2/' | \
	  grep -oE '\b[[:alpha:]]{5,}' | \
	  grep -v 'https' | \
	  sort | uniq -c | sort -nr | head -1 | sed 's/^ *[0-9]* //')

	t update "Congress' most-used word today was $w"

	rm tmp.csv
	sleep 86400
	

done	