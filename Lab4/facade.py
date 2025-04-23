class BitrateReader:
    def read_bits(path: str) -> str:
        pass

class OggCompressionCodec:
    def __init__(self, bit_str: str):
        self.mov_file = bit_str

    def convert(self):
        pass

class MPEG4CompressionCodec:
    def __init__(self, bit_str: str):
        self.mp4_file = bit_str

    def convert(self):
        pass

class VideoConverter:
    def __init__(self):
        pass
    
    def convertVideo(self, path: str, type: str):
        bit_str = BitrateReader.read_bits(path)

        if type == 'mp4':
            codec = MPEG4CompressionCodec(bit_str)
        else:
            codec = OggCompressionCodec(bit_str)

        return codec.convert()
