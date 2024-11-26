sudo apt-get install python-matplotlib python-numpy python-pil python-scipy
#pip install torch
pip install opencv-python-headless
pip install ultralytics==8.3.36
pip install scikit-image
pip install streamlit
python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0