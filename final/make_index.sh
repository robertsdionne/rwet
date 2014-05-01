echo '<html>'
echo '<body>'
echo '<p>'
for item in $(ls reading*.html); do
  echo "<a href=\"$item\">$item</a><br />"
done
echo '</p>'
echo '</body>'
echo '</html>'
