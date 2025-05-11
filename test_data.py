# filepath: /workspaces/EaseParkHK/test_data.py
from app import db, app
from app.models import User

app_context = app.app_context()
app_context.push()
db.drop_all()
db.create_all()

u1 = User(username='john', email='john@example.com')
u2 = User(username='susan', email='susan@example.com')
u1.set_password("P@ssw0rd")
u2.set_password("P@ssw0rd")
db.session.add(u1)
db.session.add(u2)
db.session.commit()