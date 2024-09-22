import ai_api_plugin.constants
import ai_api_plugin.hookspec
import pluggy

PluginManager = pluggy.PluginManager(ai_api_plugin.constants.PROJECT_NAME)
PluginManager.add_hookspecs(ai_api_plugin.hookspec.AiApiBasePlugin)