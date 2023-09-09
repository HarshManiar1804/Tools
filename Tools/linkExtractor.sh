#!/bin/bash

while IFS= read -r line; do
  # Use grep to find all URLs in the line
  urls=$(echo "$line" | grep -oP 'http[s]?://[^[:space:]]+')

  # Print the extracted URLs
  echo "$urls"
done

exit 0
