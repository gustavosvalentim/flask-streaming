if [ -f /etc/redhat-release ]; then
  sudo dnf install -y portaudio-devel python3-pip python3-pyaudio
fi

if [ -f /etc/lsb-release ]; then
  sudo apt-get install -y portaudio-devel python3-pip python3-pyaudio
fi

pip install -r requirements.txt
