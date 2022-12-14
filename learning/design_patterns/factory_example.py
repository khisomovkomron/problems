import pathlib
from abc import ABC, abstractmethod


""""
AbstractClass1(ABC)
Class1(AbstractClass1)

AbstractClass2(ABC)
Class2(AbstractClass2)

AbstractFactory(ABC)
FactoryClass1(AbstractFactory)
FactoryClass2(AbstractFactory)
FactoryClass2(AbstractFactory)

create any function that selects factories from dictionary
"""

class VideoExporter(ABC):
    
    @abstractmethod
    def prepare_export(self, video_data):
       """Prepare video data for exporting"""
       
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video to a folder"""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")
        
    
class AudioExporter(ABC):
    
    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepare audio data for exporting"""

    @abstractmethod
    def do_export(self, folder:pathlib.Path):
        """Exports the audio to a folder"""
        

class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")

## ABSTRACT FACTORY CLASS
class ExportFactory(ABC):
    
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """ Returns a new video exporter belonging to this factory"""
        
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter belonging to this factory"""
        
# FACTORY CLASS1
class FastExporter(ExportFactory):
    """Factory aimed at providing a high speed, lower quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


# FACTORY CLASS2
class HighQualityExporter(ExportFactory):
    """Factory aimed at providing a slower speed, high quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


# FACTORY CLASS3
class MasterQualityExporter(ExportFactory):
    """Factory aimed at providing a low speed, master quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()
    

def read_factory() -> ExportFactory:
    
    factories = {
        'low': FastExporter(),
        'high': HighQualityExporter(),
        'master': MasterQualityExporter(),
    }
    
    while True:
        export_quality = input('Enter desired output quality (low, high, master): ')
        if export_quality in factories:
            return factories[export_quality]
        print(f'Unknown output quality option: {export_quality}')
        

def main(fac: ExportFactory) -> None:
    
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()
    
    video_exporter.prepare_export('placeholder_for_video_data')
    audio_exporter.prepare_export('placeholder_for_audio_data')
    
    folder = pathlib.Path('C:\\khiso')
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)
    

if __name__ == '__main__':
    
    factory = read_factory()
    
    main(factory)
