from src.controller.speak_controller import SpeakController
from src.controller.listen_controller import ListenController
from src.controller.module_manager import ModuleManager
from src.controller.session import Session


manager = ModuleManager()
manager.keep_listening()
