# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
# import mysql.connector
from app import db
import datetime
import uuid
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
from sqlalchemy.orm import scoped_session, sessionmaker

web3 = Web3(KeepAliveRPCProvider(host='idea2f2p4.eastasia.cloudapp.azure.com', port='8545'))
contract_address = '0x718ed7ff43f863af2ec7c4ca51baaab1f60f19aa'
master_address = web3.eth.coinbase
master_passphrase = '1QAZ2wsx3edc'
contract_abi = [{"constant":True,"inputs":[{"name":"","type":"uint256"}],"name":"deals","outputs":[{"name":"buyer","type":"address"},{"name":"seller","type":"address"},{"name":"buyer_sent","type":"bool"},{"name":"seller_sent","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"timestamp","type":"uint256"},{"name":"addr","type":"address"},{"name":"score","type":"int256"}],"name":"set_user_score","outputs":[],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"dealID","type":"uint256"},{"name":"timestamp","type":"string"},{"name":"score","type":"int256"},{"name":"message","type":"string"}],"name":"send_feedback","outputs":[],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"timestamp","type":"string"},{"name":"itemName","type":"string"},{"name":"buyer","type":"address"},{"name":"seller","type":"address"}],"name":"create_deal","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"master","outputs":[{"name":"","type":"address"}],"payable":False,"type":"function"},{"inputs":[],"payable":False,"type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"name":"_dealID","type":"uint256"},{"indexed":False,"name":"_timestamp","type":"string"},{"indexed":False,"name":"_itemName","type":"string"},{"indexed":True,"name":"_buyer","type":"address"},{"indexed":True,"name":"_seller","type":"address"}],"name":"deal_created","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_dealID","type":"uint256"},{"indexed":False,"name":"_timestamp","type":"string"},{"indexed":True,"name":"sender","type":"address"},{"indexed":True,"name":"receiver","type":"address"},{"indexed":False,"name":"_sender_is_seller","type":"bool"},{"indexed":False,"name":"_score","type":"int256"},{"indexed":False,"name":"_message","type":"string"}],"name":"feedback_sent","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"addr","type":"address"},{"indexed":True,"name":"timestamp","type":"uint256"},{"indexed":False,"name":"old_score","type":"int256"},{"indexed":False,"name":"new_score","type":"int256"}],"name":"user_score_changed","type":"event"}]
sessionfactory = sessionmaker(bind=db.engine)
sessionfactory2 = sessionmaker(bind=db.engine)
deal_db_session = scoped_session(sessionfactory)
feedback_db_session = scoped_session(sessionfactory2)

class User(db.Model):
	# personalInfo
	ssn = db.Column(db.String(64), primary_key=True)
	password = db.Column(db.String(500))
	name = db.Column(db.String(500), unique=True)
	email = db.Column(db.String(120))
	# blockchain
	credit_score = db.Column(db.Float)
	eth_address = db.Column(db.String(50))
	eth_password = db.Column(db.String(500))
	# esun
	education_level = db.Column(db.String(1))
	occupation = db.Column(db.String(1))
	age = db.Column(db.String(1))
	annual_income = db.Column(db.String(7))
	employment_year = db.Column(db.String(1))
	resident_status = db.Column(db.String(5))
	credit_card_status = db.Column(db.String(1))
	limit_amount = db.Column(db.String(6))
	pre_owned_status = db.Column(db.String(1))
	revolving_count = db.Column(db.String(1))
	revolving_amount = db.Column(db.String(7))
	debt_status = db.Column(db.String(1))
	mortgage = db.Column(db.String(1))
	debt_amount = db.Column(db.String(7))
	balance_amount = db.Column(db.String(7))
	debt = db.Column(db.String(1))
	delinquent = db.Column(db.String(1))
	ever_in_use = db.Column(db.String(1))
	#  model
	about_me = db.Column(db.Text)
	emo = db.Column(db.Float)
	peo = db.Column(db.Float)
	sn = db.Column(db.Float)
	risk = db.Column(db.Float)
	idt = db.Column(db.Float)

	emo_freq_sad = db.Column(db.Float)
	emo_freq_haha = db.Column(db.Float)
	emo_freq_wow = db.Column(db.Float)
	emo_freq_angry = db.Column(db.Float)
	emo_freq_love = db.Column(db.Float)

	good_comment = db.Column(db.Integer)
	comment = db.Column(db.Integer)
	total_comment = db.Column(db.Integer)


	def __init__(
		self, ssn, password, name, email, credit_score,
		eth_address, eth_password,
		education_level, occupation, age, annual_income, employment_year, resident_status, credit_card_status, limit_amount,
		pre_owned_status, revolving_count, revolving_amount, debt_status, mortgage, debt_amount, balance_amount, debt, delinquent, ever_in_use,
		about_me, emo, peo, sn, risk, idt, emo_freq_sad, emo_freq_haha, emo_freq_wow, emo_freq_angry, emo_freq_love, good_comment, comment, total_comment
	):
		self.ssn = ssn
		self.password = password
		self.name = name
		self.email = email
		self.credit_score = credit_score
		self.eth_address = eth_address
		self.eth_password = eth_password
		self.education_level = education_level
		self.occupation = occupation
		self.age = age
		self.annual_income = annual_income
		self.employment_year = employment_year
		self.resident_status = resident_status
		self.credit_card_status = credit_card_status
		self.limit_amount = limit_amount
		self.pre_owned_status = pre_owned_status
		self.revolving_count = revolving_count
		self.revolving_amount = revolving_amount
		self.debt_status = debt_status
		self.mortgage = mortgage
		self.debt_amount = debt_amount
		self.balance_amount = balance_amount
		self.debt = debt
		self.delinquent = delinquent
		self.ever_in_use = ever_in_use

		self.about_me = about_me
		self.emo = emo
		self.peo = peo
		self.sn = sn
		self.risk = risk
		self.idt = idt

		self.emo_freq_sad = emo_freq_sad
		self.emo_freq_haha = emo_freq_haha
		self.emo_freq_wow = emo_freq_wow
		self.emo_freq_angry = emo_freq_angry
		self.emo_freq_love = emo_freq_love

		self.good_comment = good_comment
		self.comment = comment
		self.total_comment = total_comment


	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.ssn)

	def __repr__(self):
		return '<User %r>' % (self.name)

	@staticmethod
	def register(
		ssn, password, name, email,
		education_level, occupation, age, annual_income, employment_year, resident_status, credit_card_status, limit_amount,
		pre_owned_status, revolving_count, revolving_amount, debt_status, mortgage, debt_amount, balance_amount, debt, delinquent, ever_in_use,
	):
		user = User.query.get(ssn)
		if not user:
			eth_password = str(uuid.uuid1())
			eth_address = web3.personal.newAccount(eth_password)

			new_user = User(
				ssn, password, name, email, eth_address, eth_password,
				education_level, occupation, age, annual_income, employment_year, resident_status, credit_card_status, limit_amount,
				pre_owned_status, revolving_count, revolving_amount, debt_status, mortgage, debt_amount, balance_amount, debt, delinquent, ever_in_use
			)
			db.session.add(new_user)
			db.session.commit()
			#send ether to the account for gas fee
			web3.personal.unlockAccount(master_address, master_passphrase)
			tx_hash = web3.eth.sendTransaction({'to': eth_address, 'from': master_address, 'value': 10000000000000000000000})
			if not tx_hash:
				return False
			return True
		else:
			# This account already been signup.
			return False

	@staticmethod
	def login(ssn, password):
		user = User.query.get(ssn)
		if user:
			return True
		else:
			return False

	@staticmethod
	def get_user_info(ssn, other_name=None):
		if other_name is None:
			return row2dict(User.query.get(ssn))
		else:
			user = User.query.filter_by(name=other_name).first()
			if user:
				return row2dict(user)
			else:
				return None


class Deal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    buyer_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
    seller_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
    # buyer_to_seller_feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))
    # seller_to_buyer_feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))
    # buyer_to_seller_feedback = db.relationship("Feedback", uselist=False, back_populates="deal")
    # seller_to_buyer_feedback = db.relationship("Feedback", uselist=False, back_populates="deal")

    def __init__(self, id, item_name, timestamp, buyer_id, seller_id):
        self.id = id
        self.item_name = item_name
        self.timestamp = timestamp
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        # self.buyer_to_seller_feedback_id = None
        # self.seller_to_buyer_feedback_id = None

    def create_deal(item_name, buyer_id, seller_id):
        # Create deal in blockchain and get deal id
        # Get buyer and seller address first
        buyer_addr = User.query.get(buyer_id).eth_address
        seller_addr = User.query.get(seller_id).eth_address

        #Unlock and call contract function
        web3.personal.unlockAccount(master_address, master_passphrase)
        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        tx_hash = blockchain_contract.transact({'from': master_address}).create_deal(
            timestamp, item_name.encode('utf8'), buyer_addr, seller_addr)
        return tx_hash

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deal_id = db.Column(db.Integer, db.ForeignKey('deal.id'))
    deal = db.relationship("Deal", cascade='all, delete-orphan', single_parent = True)
    score = db.Column(db.Integer)
    message = db.Column(db.Text)
    from_is_seller = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    from_user_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
    # from_who = db.relationship('User', foreign_keys=[from_user_id])
    to_user_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
    # to_who = db.relationship('User', foreign_keys=[to_user_id])

    def __init__(self, deal_id, score, message, from_who_id, to_who_id, from_is_seller, created_date=None):
        self.deal_id = deal_id
        self.score = score
        self.message = message
        self.from_is_seller = from_is_seller
        if created_date is None:
            created_date = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        # self.from_who = from_who
        self.from_user_id = from_who_id
        # self.to_who = to_who
        self.to_user_id = to_who_id

    @staticmethod
    def create_feedback(deal_id, score, message, from_user_id, to_user_id):
        from_user = User.query.get(from_user_id)
        to_user_id = User.query.get(to_user_id).eth_address
        web3.personal.unlockAccount(from_user.eth_address, from_user.eth_password)
        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        tx_hash = blockchain_contract.transact({'from': from_user.eth_address}).send_feedback(
            deal_id, timestamp, score, message.encode('utf8'))
        # print(tx_hash)
        return tx_hash

    @staticmethod
    def get_all_received_feedback(ssn, other_name = None):
        from_buyers = Feedback.get_received_feedback_from_buyer(ssn, other_name)
        from_sellers = Feedback.get_received_feedback_from_seller(ssn, other_name)
        mixed = from_buyers + from_sellers
        return sorted(mixed, key=lambda x: x[4], reverse = True)

    @staticmethod
    def get_received_feedback_from_buyer(ssn, other_name = None):
        if not other_name:
            feedbacks = db.session.query(Feedback.score.label('score'), Deal.item_name.label('item_name'), User.name.label('user_name'), Feedback.message.label('message'), Feedback.created_date.label('timestamp'))\
            .join(User, User.ssn==Feedback.from_user_id) \
            .join(Deal, Deal.id == Feedback.deal_id) \
            .filter((Feedback.to_user_id == ssn) & (Feedback.from_is_seller == False)) \
            .order_by(Feedback.created_date.desc()).limit(20).all()
            return feedbacks
        else:
            other = User.query.filter_by(name=other_name).first()
            if other is None:
                return None
            other_ssn = other.ssn
            feedbacks = db.session.query(Feedback.score.label('score'), Deal.item_name.label('item_name'), User.name.label('user_name'), Feedback.message.label('message'), Feedback.created_date.label('timestamp'))\
            .join(User, User.ssn==Feedback.from_user_id) \
            .join(Deal, Deal.id == Feedback.deal_id) \
            .filter((Feedback.to_user_id == other_ssn) & (Feedback.from_is_seller == False)) \
            .order_by(Feedback.created_date.desc()).limit(20).all()
            return feedbacks

    @staticmethod
    def get_received_feedback_from_seller(ssn, other_name = None):
        if not other_name:
            feedbacks = db.session.query(Feedback.score.label('score'), Deal.item_name.label('item_name'), User.name.label('user_name'), Feedback.message.label('message'), Feedback.created_date.label('timestamp'))\
            .join(User, User.ssn==Feedback.from_user_id) \
            .join(Deal, Deal.id == Feedback.deal_id) \
            .filter((Feedback.to_user_id == ssn) & (Feedback.from_is_seller == True)) \
            .order_by(Feedback.created_date.desc()).limit(20).all()
            return feedbacks
        else:
            other = User.query.filter_by(name=other_name).first()
            if other is None:
                return None
            other_ssn = other.ssn
            feedbacks = db.session.query(Feedback.score.label('score'), Deal.item_name.label('item_name'), User.name.label('user_name'), Feedback.message.label('message'), Feedback.created_date.label('timestamp'))\
            .join(User, User.ssn==Feedback.from_user_id) \
            .join(Deal, Deal.id == Feedback.deal_id) \
            .filter((Feedback.to_user_id == other_ssn) & (Feedback.from_is_seller == True)) \
            .order_by(Feedback.created_date.desc()).limit(20).all()
            return feedbacks

    @staticmethod
    def get_all_sent_feedback(ssn, other_name = None):
        if not other_name:
            feedbacks = db.session.query(Feedback.score.label('score'), Deal.item_name.label('item_name'), User.name.label('user_name'), Feedback.message.label('message'), Feedback.created_date.label('timestamp'))\
            .join(User, User.ssn==Feedback.to_user_id) \
            .join(Deal, Deal.id == Feedback.deal_id) \
            .filter(Feedback.from_user_id == ssn) \
            .order_by(Feedback.created_date.desc()).limit(20).all()
            return feedbacks
        else:
            other = User.query.filter_by(name=other_name).first()
            if other is None:
                return None
            other_ssn = other.ssn
            feedbacks = db.session.query(Feedback.score.label('score'), Deal.item_name.label('item_name'), User.name.label('user_name'), Feedback.message.label('message'), Feedback.created_date.label('timestamp'))\
            .join(User, User.ssn==Feedback.to_user_id) \
            .join(Deal, Deal.id == Feedback.deal_id) \
            .filter(Feedback.from_user_id == other_ssn) \
            .order_by(Feedback.created_date.desc()).limit(20).all()
            return feedbacks


    def __repr__(self):
        return '<Feedback %r>' % (self.message)

class Blockchain:

    @staticmethod
    def get_newest_20_blocks():
        blocks = []
        for block_number in reversed(range(web3.eth.blockNumber-20, web3.eth.blockNumber)):
            blocks.append(web3.eth.getBlock(block_number))
        return blocks

    @staticmethod
    def get_newest_20_deals():
        deal_filter = blockchain_contract.on("deal_created", {'fromBlock': web3.eth.blockNumber-10000, 'address': contract_address})
        logs = deal_filter.get(only_changes=False)
        for log in logs[:20]:
            log['args']['_itemName'] = log['args']['_itemName'].encode('latin1').decode('utf8')

        return logs[:20]

    @staticmethod
    def get_newest_20_feedbacks():
        feedback_filter = blockchain_contract.on("feedback_sent", {'fromBlock': web3.eth.blockNumber-10000, 'address': contract_address})
        logs = feedback_filter.get(only_changes=False)
        for log in logs[:20]:
            log['args']['_message'] = log['args']['_message'].encode('latin1').decode('utf8')

        return logs[:20]



# Will be called everytime a deal is successfully created on blockchain
def deal_created_callback(event):
    deal_id = event['args']['_dealID']
    item_name = event['args']['_itemName'].encode('latin1').decode('utf8')
    buyer_addr = event['args']['_buyer']
    seller_addr = event['args']['_seller']
    timestamp = event['args']['_timestamp']
    buyer_id = User.query.filter_by(eth_address=buyer_addr).first().ssn
    seller_id = User.query.filter_by(eth_address=seller_addr).first().ssn
    new_deal = Deal(deal_id, item_name, timestamp, buyer_id, seller_id)
    deal_db_session.add(new_deal)
    deal_db_session.commit()
    # with open('test.txt', 'w') as file:
    #     file.write(new_deal.item_name)
    #     file.close()
    #     print('haha')
    # print(deal_id, item_id, buyer_addr, seller_addr, timestamp)
    # cnx = mysql.connector.connect(user='jim@esunmysql', password='1QAZ2wsx3edc',
    #                           host='esunmysql.mysql.database.azure.com',
    #                           database='esun')
    # cursor = cnx.cursor()
    # add_deal = ("INSERT INTO deal "
    #             "(id, timestamp, buyer_id, seller_id) "
    #             "VALUES (%s, %s, %s, %s)")
    # find_user_id = ("SELECT ssn FROM user WHERE eth_address = %s")
    # cursor.execute(find_user_id, (buyer_addr))
    # buyer_id = cursor[0]
    # cursor.execute(find_user_id, (seller_addr))
    # seller_id = cursor[0]
    # cursor.execute(add_deal, (deal_id, item_id, timestamp, buyer_id, seller_id))
    # cnx.commit()
    # cursor.close()
    # cnx.close()

def feedback_sent_callback(event):
    deal_id = event['args']['_dealID']
    timestamp = event['args']['_timestamp']
    sender_addr = event['args']['sender']
    receiver_addr = event['args']['receiver']
    sender_is_seller = event['args']['_sender_is_seller']
    score = event['args']['_score']
    message = event['args']['_message'].encode('latin1').decode('utf8')
    sender_id = User.query.filter_by(eth_address=sender_addr).first().ssn
    receiver_id = User.query.filter_by(eth_address=receiver_addr).first().ssn
    deal = Deal.query.get(deal_id)
    check_feedback = Feedback.query.filter_by(deal_id = deal_id, from_user_id = sender_addr).first()
    if check_feedback is not None:
        return
    from_is_seller = False
    if deal.seller_id == sender_id:
        from_is_seller = True

    feedback = Feedback(deal_id, score, message, sender_id, receiver_id, from_is_seller, timestamp)
    feedback_db_session.add(feedback)
    # if from_is_seller:
    #     deal.seller_to_buyer_feedback_id = feedback.id
    #     # deal.seller_to_buyer_feedback = feedback
    #     print(deal.seller_to_buyer_feedback)
    # else:
    #     deal.buyer_to_seller_feedback_id = feedback.id
    #     # deal.buyer_to_seller_feedback = feedback
    #     print(deal.buyer_to_seller_feedback)
    feedback_db_session.commit()

 

def row2dict(row):
	d = {}
	for column in row.__table__.columns:
		d[column.name] = str(getattr(row, column.name))
	return d

# The main blockchain smart contract
blockchain_contract = web3.eth.contract(address = contract_address, abi = contract_abi)

#listeners of blockchain
deal_created_listener = blockchain_contract.on("deal_created", None, deal_created_callback)
feedback_sent_listener = blockchain_contract.on("feedback_sent", None, feedback_sent_callback)