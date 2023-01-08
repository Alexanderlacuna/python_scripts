
count = 0

import scipy.stats

import time
results = []

initial_time = time.time()
with open("/home/kabui/correlation_rust/tests/data/db300.txt") as fp:
    while True:
        count +=1

        line = fp.readline()

        if not line:
            break


        line = [float(x.strip()) for x in line.split(",")]

        x_vals =  [79.39, 24.36, 47.64, 79.49, 17.81, 15.77, 15.12, 24.03, 18.09, 84.22, 84.19, 86.9, 91.23, 37.87, 17.29, 61.53]

        results.append(scipy.stats.pearsonr(x_vals,line))




print(f"Time taken is {time.time()-initial_time}")




env GN2_PROFILE=$GUIX_ENVIRONMENT TMPDIR=/tmp SERVER_PORT=5004 WEBSERVER_MODE=DEBUG LOG_LEVEL=DEBUG
GENENETWORK_FILES=$HOME/data/genotype_files ./bin/genenetwork2 $HOME/project3/genenetwork2/etc/default_settings.py

env GUIX_PACKAGE_PATH="/home/kabui/guix-bioinformatics/:/home/kabui/guix-past/modules" 
GN_PROXY_URL="http://localhost:8080"  GN3_LOCAL_URL="http://localhost:8081"
GENENETWORK_FILES=/home/kabui/data/genotype_files
 guix package -p ~/opt/python3-genenetwork2 --substitute-urls="http://guix.genenetwork.org https://berlin.guixsd.org https://ci.guix.gnu.org https://mirror.hydra.gnu.org" -i genenetwork2 --fallback --dry-run


env GUIX_PACKAGE_PATH="/home/kabui/guix-bioinformatics/:/home/kabui/guix-past/modules" GENENETWORK_FILES=/home/kabui/data/genotype_files
guix package -p ~/opt/python3-genenetwork2 --substitute-urls="http://guix.genenetwork.org https://berlin.guixsd.org https://ci.guix.gnu.org https://mirror.hydra.gnu.org" -i genenetwork2 --fallback --dry-run