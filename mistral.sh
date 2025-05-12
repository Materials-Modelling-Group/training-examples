module load applications/gpu/python/conda-25.1.1-python-3.9.21
conda activate python-3.9.21
pip install mistral-inference

export MISTRAL_MODEL=$HOME/localscratch/dat
mkdir -p $MISTRAL_MODEL
export B_DIR="$MISTRAL_MODEL/12B_Nemo"
mkdir -p $B_DIR
wget https://models.mistralcdn.com/mistral-nemo-2407/mistral-nemo-instruct-2407.tar
tar -xf mistral-nemo-instruct-2407.tar -C $B_DIR
# prompt it:
# $ mistral-chat $B_DIR --instruct --max_tokens 1024 --temperature 0.35
#  Write me a function that computes fibonacci in Rust
