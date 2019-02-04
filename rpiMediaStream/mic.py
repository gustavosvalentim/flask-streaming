import pyaudio


class rpiMicrophone:

    def __init__(self):
        self.CHANNELS = 1
        self.FORMAT = pyaudio.paInt32
        self.RATE = 44100
        self.CHUNK = 512
        self.pyAudio = pyaudio.PyAudio()
        self.stream = self.pyAudio.open(
            format = self.FORMAT,
            channels = self.CHANNELS,
            rate = self.RATE,
            input = True,
            frames_per_buffer = self.CHUNK
        )

    
    def getFrame(self):
        data = self.stream.read(self.CHUNK)

        return data


    def streamAudio(self):
        datasize = 2000*10**6
        o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
        o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
        o += bytes("WAVE",'ascii')                                              # (4byte) File type
        o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
        o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
        o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
        o += (1).to_bytes(2,'little')                                    # (2byte)
        o += (self.RATE).to_bytes(4,'little')                                  # (4byte)
        o += (self.RATE * 1 * 32 // 8).to_bytes(4,'little')  # (4byte)
        o += (1 * 32 // 8).to_bytes(2,'little')               # (2byte)
        o += (32).to_bytes(2,'little')                               # (2byte)
        o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
        o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
        return o + self.getFrame()