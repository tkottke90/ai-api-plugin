import ai_api_plugin.constants
import pluggy
from dataclasses import dataclass

hookspec = pluggy.HookspecMarker(ai_api_plugin.constants.PROJECT_NAME)

@dataclass(kw_only=True)
class AiApiBasePlugin:

  @hookspec
  def initialize():
    """
    Initialize the plugin
    """

  @hookspec
  def render():
    """
    Render a partial html document to be returned to the browser
    """