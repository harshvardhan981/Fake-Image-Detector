rm -rf tensorflow_env
python3.10 -m venv tensorflow_env
source tensorflow_env/bin/activate

pip install tensorflow matplotlib
 pip install --upgrade pip      
pip install scipy
pip install numpy matplotlib pillow

pip uninstall tensorflow
pip install tensorflow-macos tensorflow-metal