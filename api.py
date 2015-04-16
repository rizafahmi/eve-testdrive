from eve import Eve
from flask.ext.admin import Admin
from flask.ext.admin import BaseView, expose

import settings

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


app = Eve(__name__)
admin = Admin(app)
admin.add_view(MyView(name='Hello'))

if __name__ == '__main__':
    app.run(debug=True)
