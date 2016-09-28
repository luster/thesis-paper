#!/bin/bash

# FILES=("./main.py" "./models/model.py"  "./models/generator.py" "./models/discriminator.py" "./util/ops.py" "./dataset_loading/dataset.py" "./dataset_loading/input_chain.py")
FILES=("../thesis/thesis/comparisons/autoencoder.py")

for f in "${FILES[@]}";  do
    echo "${f%.*}".py
    echo "${f%.*}".ps    
    a2ps -R  --columns=1 --font-size=12 --left-title="" --header="" --left-footer=""  --right-footer="" $f -o "${f%.*}".ps
    ps2pdf "${f%.*}".ps
done


