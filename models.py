from mongokit import Document
import datetime
from app import conn
class Entry(Document):
	structure = {
		'content': [unicode],
		'date': [datetime.datetime],
		'rows': [int],
		'visible': bool,
		'public': bool,
	}
	required_fields = ['content', 'date', 'rows']
	use_dot_notation = True
	
	def __repr__(self):
		return '<Entry {0}>'.format(self.content)


conn.register([Entry])
