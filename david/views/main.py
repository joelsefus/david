from trumpet.views.base import prepare_layout
from trumpet.views.base import BaseViewer

def prepare_main_layout(request):
    layout = request.layout_manager.layout
    prepare_layout(layout)
    layout.left_menu.set_header('Main Menu')
    url = request.route_url('view_wiki')
    layout.left_menu.append_new_entry('wiki', url)
    url = request.route_url('rssviewer', context='listfeeds', feed=None)
    layout.left_menu.append_new_entry('rss', url)
    layout.title = 'David'
    layout.header = 'David'
    layout.subheader = ''
    

    

class MainViewer(BaseViewer):
    def __init__(self, request):
        BaseViewer.__init__(self, request)
        prepare_main_layout(self.request)
        
