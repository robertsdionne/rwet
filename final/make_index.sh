echo '<html>'
echo '<body>'
echo '<p>'
for item in $(ls reading*.html); do
  first=$(grep '<p>' $item | cut -d '>' -f 2 | cut -d '<' -f 1)
  echo "<a href=\"$item\">$item: $first</a><br />"
done
echo '</p>'
echo '</body>'
echo '</html>'
