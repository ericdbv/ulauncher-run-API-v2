from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
import subprocess

class RunExtension(Extension):

    def __init__(self):
        super(RunExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_argument()
        items = [
                ExtensionResultItem(
                    icon="images/icon.png",
                    name="Run a shell command",
                    description="" if not data else 'Run "%s" in shell' % data,
                    on_enter=ExtensionCustomAction(data),
                    ),
                ]

        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data() or ""
        subprocess.Popen(data, shell=True)

        return RenderResultListAction([])

if __name__ == '__main__':
    RunExtension().run()

