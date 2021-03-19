from subprocess import call

call(["node", "./converter/3d-tiles-validator-master/tools/bin/3d-tiles-tools.js upgrade -i ./data/in/ -o ./data/out/"])
