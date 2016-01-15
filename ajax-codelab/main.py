import webapp2
import time
import json

class DelayHandler(webapp2.RequestHandler):
    colors = ['blue', 'green', 'yellow', 'red']
    def get(self):
        delay_secs = int(self.request.get("delay"))
        time.sleep(delay_secs)
        new_color = DelayHandler.colors.pop(0)
        DelayHandler.colors.append(new_color)
        reply_obj = {
            "color": new_color,
            "request_type": "GET",
        }
        self.response.headers["Content-Type"] = "application/json"
        self.response.write(json.dumps(reply_obj))

    def post(self):
        delay_secs = int(self.request.get("delay"))
        time.sleep(delay_secs)
        new_color = DelayHandler.colors.pop(0)
        DelayHandler.colors.append(new_color)
        reply_obj = {
            "color": new_color,
            "request_type": "POST",
        }
        self.response.headers["Content-Type"] = "application/json"
        self.response.write(json.dumps(reply_obj))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(open("index.html").read())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/send_delayed_response', DelayHandler),

], debug=True)
