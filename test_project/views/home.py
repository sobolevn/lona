import os

from lona.view import LonaView


class HomeView(LonaView):
    def handle_request(self, request):
        body = ''

        if os.environ.get('DJANGO', '0') == '1':
            body += """
                <h2>Django Views</h2>
                <ul>
                    <li><a href="/admin/">Django Admin</a></li>
                    <li><a href="/django/login-required/">Login Required</a></li>
                    <li><a href="/django/template-based-form/">Template Based Form</a></li>
                    <li><a href="/django/node-based-form/">Node Based Form</a></li>
                    <li><a href="/django/data-binding-form/">Data Binding Form</a></li>
                </ul>
            """  # NOQA

        body += """
            <h2>View Types</h2>
            <ul>
                <li><a href="/view-types/interactive-view/">Interactive View</a></li>
                <li><a href="/view-types/non-interactive-view/">Non-Interactive View</a></li>
                <li><a href="/view-types/http-pass-through/">HTTP Pass Through View</a></li>
                <li><a href="/view-types/daemonized-view/">Daemonized View</a></li>
                <li><a href="/view-types/form-view/">Form View</a></li>
                <li><a href="/view-types/async-view/">Async View</a></li>
            </ul>

            <h2>Response Types</h2>
            <ul>
                <li><a href="/response-types/template-response/">Template Response</a></li>
                <li><a href="/response-types/file-response/">File Response</a></li>
                <li><a href="/response-types/json-response/">JSON Response</a></li>
                <li><a href="/response-types/redirect/">Redirect</a></li>
                <li><a href="/response-types/http-redirect/">HTTP Redirect</a></li>
            </ul>

            <h2>Permissions</h2>
            <ul>
                <li><a href="/permissions/access-denied-in-PermissionMiddleware/">Access denied in Middleware.handle_request()</a></li>
                <li><a href="/permissions/access-denied-in-PermissionMiddleware/non-interactive/">Access denied in Middleware.handle_request() (non interactive)</a></li>
                <li><a href="/permissions/access-denied-in-handle-request/">Access denied in handle_request()</a></li>
                <li><a href="/permissions/access-denied-in-handle-request/non-interactive/">Access denied in handle_request() (non interactive)</a></li>
            </ul>

            <h2>Error Types</h2>
            <ul>
                <li><a href="/error-types/404/">Interactive 404</a></li>
                <li><a href="/error-types/404/" data-lona-ignore="True">Non Interactive 404</a></li>
                <li><a href="/error-types/interactive-500/">Interactive 500</a></li>
                <li><a href="/error-types/non-interactive-500/" data-lona-ignore="True">Non Interactive 500</a></li>
                <li><a href="/error-types/non-interactive-feature-error/">Non Interactive Feature Error</a></li>
            </ul>

            <h2>Crashes</h2>
            <ul>
                <li><a data-lona-ignore="True" href="/crashes/handle-connection/">Middleware.handle_connection()</a></li>
                <li><a href="/crashes/handle-request/">Middleware.handle_middleware()</a></li>
                <li><a href="/crashes/response-dict/">Response Dict</a></li>
                <li><a href="/crashes/input-events/">Input Events</a></li>
                <li><a href="/crashes/handle-404/">404 Handler</a></li>
                <li><a href="/crashes/handle-500/">500 Handler</a></li>
                <li><a href="/crashes/frontend-widget/">Frontend Widget</a></li>
            </ul>

            <h2>Routing</h2>
            <ul>
                <li><a href="/routing/url-args/foo/bar/baz/">URL Arguments</a></li>
            </ul>

            <h2>Events</h2>
            <ul>
                <li><a href="/events/click-events/">Click Events</a></li>
                <li><a href="/events/change-events/">Change Events</a></li>
                <li><a href="/events/data-binding/">Data Binding</a></li>
                <li><a href="/events/non-node-events/">Non-Node Events</a></li>
                <li><a href="/events/widget-event-handler/">Widget Event Handler</a></li>
                <li><a href="/events/class-based-view/">Class Based View</a></li>
                <li><a href="/events/event-bubbling/">Event Bubbling</a></li>
            </ul>

            <h2>Locking</h2>
            <ul>
                <li><a href="/locking/html-tree/">HTML Tree</a></li>
                <li><a href="/locking/server-state/">Server State</a></li>
            </ul>

            <h2>Window Actions</h2>
            <ul>
                <li><a href="/window-actions/set-title/">Set Title</a></li>
            </ul>

            <h2>Frontend</h2>
            <ul>
                <li><a href="/frontend/widget-data/">Widget Data</a></li>
                <li><a href="/frontend/custom-event/">Custom Event</a></li>
                <li><a href="/frontend/custom-messages/">Custom Messages</a></li>
            </ul>

            <h2>Multi User</h2>
            <ul>
                <li><a href="/multi-user/multi-user-chat/">Multi User Chat</a></li>
            </ul>

            <h2>Contrib</h2>
            <ul>
                <li><a href="/contrib/chart-js/">Chart.js</a></li>
            </ul>
        """  # NOQA

        return body
