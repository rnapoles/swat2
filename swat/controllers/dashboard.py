import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from swat.lib.base import BaseController, render
from routes import url_for

from swat.lib.helpers import ControllerConfiguration, DashboardConfiguration, \
BreadcrumbTrail, SwatMessages

log = logging.getLogger(__name__)

class DashboardController(BaseController):
    
    def __init__(self):
        type = request.environ['pylons.routes_dict']['action']

        c.controller_config = ControllerConfiguration()
        c.dashboard_config = DashboardConfiguration(type)

        c.breadcrumb = BreadcrumbTrail(c.controller_config)
        c.breadcrumb.build()
        
        if not session.has_key("messages"):
            session['messages'] = SwatMessages()

    def index(self):
        """ The default Dashboard. The entry point for SWAT """
        return render('/default/derived/dashboard.mako')
        
    def advanced(self):
        """ The advanced layout for the Dashboard is exactly the same as the
        'normal' dashboard. The only difference is the items that are loaded
        and the Breadcrumb Trail
        
        """
        return render('/default/derived/dashboard.mako')
            
    def goto(self):
        redirect_to(controller = 'dashboard', action = 'index')
