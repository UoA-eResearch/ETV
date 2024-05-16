#!/bin/bash
for f in *.mp4; do
  output_file=$f.json
  if [ ! -f $output_file ]; then
    time insanely-fast-whisper --file-name $f --transcript-path $output_file --flash True --language en
  fi
done
