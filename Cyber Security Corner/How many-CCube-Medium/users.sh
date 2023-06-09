#! /bin/bash
echo -n Total count of USER IDs are:

cat users.txt |cut -d' ' -f5| grep -E '553|828|723|698'|wc -l

