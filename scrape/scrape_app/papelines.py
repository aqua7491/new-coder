from sqlalchemy.orm import sessionmaker
from models import Deals, db_connect, create_deals_table

class LivingSocialPipeline(object):
	"""Livingsocial pipeline for storing scraped items in the database"""

	def __init__(self):
		engine = db_connect()
		create_deals_table(engine)
		self.Sesson =  sessionmaker.(bind=True)

	def process_item(self, item, spider):
		"""Save deals in the database.
		This method is called for every item pipeline component.
		"""
		session = self.Sesson()
		deal = Deals(**item)

		try:
			session.add(deal)
			session.commit()
		except session.rollback()
			raise
		finally:
			session.close()

		return item