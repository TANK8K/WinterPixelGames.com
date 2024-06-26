#!/bin/bash

# Loop through each language directory
for lang_dir in */; do
  lang=${lang_dir%/}
  
  # Find the .po file in the language directory
  po_file=$(find "$lang" -name 'base-*.po')
  
  if [[ -n $po_file ]]; then
    # Extract the filename without the path
    filename=$(basename "$po_file")
    
    # Replace base- with base_
    new_filename=${filename//base-/base_}
    
    # Create LC_MESSAGES directory
    mkdir -p "$lang/LC_MESSAGES"
    
    # Move and rename .po file to LC_MESSAGES directory
    mv "$po_file" "$lang/LC_MESSAGES/$new_filename"
    
    # Convert .po file to .mo file with the same name
    msgfmt -o "$lang/LC_MESSAGES/${new_filename%.po}.mo" "$lang/LC_MESSAGES/$new_filename"
  fi
done

