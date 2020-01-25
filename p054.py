from copy import deepcopy

rank_order = {"High Card":1, "One Pair":2, "Two Pairs":3,"Three of a Kind":4, "Straight":5, "Flush":6,
			  "Full House":7, "Four of a Kind":8, "Straight Flush":9, "Royal Flush":10}
card_valuation = {'2': 1, "3": 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
card_order= {'A':0,'2': 1, "3": 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}

def compareHands(hand1, hand2):
	rank1=hand1.get_rank()
	rank2=hand2.get_rank()

	if rank1==None and rank2==None:
		for i in range(len(hand1.bestCards)):
			if hand1.bestCards[i] > hand2.bestCards[i]:
				return "Player 1"
			elif hand1.bestCards[i] < hand2.bestCards[i]:
				return "Player 2"
	elif rank1==None:
		return "Player 2"
	elif rank2==None:
		return "Player 1"

	if rank_order[rank1[0]]==rank_order[rank2[0]]:
		if rank1[1]==rank2[1]:
			try:
				for i in range(len(hand1.bestCards)):
					if hand1.bestCards[i] > hand2.bestCards[i]:
						return "Player 1"
					elif hand1.bestCards[i] < hand2.bestCards[i]:
						return "Player 2"
			except:
				raise IOError
		elif rank1[1]>rank2[1]:
			return "Player 1"
		else:
			return "Player 2"
	elif rank_order[rank1[0]]>rank_order[rank2[0]]:
		return "Player 1"
	else:
		return "Player 2"

class Hand(object):
	def __init__(self, cards):
		assert len(cards) == 5 and type(cards) == list
		self.cards = cards
		self.bestCards = self.get_highest_value()

	def get_highest_value(self):
		values = []
		for card in self.cards:
			values.append(card_valuation[card[0]])
		values.sort(reverse=True)
		return values

	def get_rank(self):

		classifications=[]

		cardnums = []
		suits=[]
		for card in self.cards:
			cardnums.append(card[0])
			suits.append(card[1])

		hand = cardnums
		cardnums = list(set(cardnums))
		suits = list(set(suits))
		cardnums.sort()
		for cardnum in cardnums:
			count = 0
			for card in hand:
				if cardnum == card:
					count += 1
			if count==3:
				classifications.append(("Three of a Kind", card_valuation[cardnum]))
			elif count==4:
				classifications.append(("Four of a Kind", card_valuation[cardnum]))
			elif count==2:
				classifications.append(("One Pair", card_valuation[cardnum]))

		flatclassifications=[item for sublist in classifications for item in sublist]
		if "Three of a Kind" in flatclassifications and "One Pair" in flatclassifications:
			for item in classifications:
				if item[0]=="Three of a Kind":
					classifications.append(("Full House", item[1]))
					break

		counter=0
		for item in flatclassifications:
			if item=="One Pair":
				counter+=1
		if counter==2:
			classifications.append(("Two Pairs", 0))

		flush=False
		if len(suits)==1:
			flush=True
			classifications.append(("Flush", 0))

		newcardnums=[]
		for item in cardnums:
			newcardnums.append(card_order[item])
		newcardnums.sort()
		if len(newcardnums)==5:
			consecutive=True
			prev=newcardnums[0]-1
			for item in newcardnums:
				if item!=prev+1:
					consecutive=False
					break
				prev=item
			if consecutive and flush:
				classifications.append(("Straight Flush", 0))
			elif consecutive:
				classifications.append(("Straight", 0))

			if 'T' in cardnums and "K" in cardnums and "J" in cardnums and "Q" in cardnums and "K" in cardnums and 'A' in cardnums and flush:
				classifications.append(("Royal Flush", 0))

		bestRank=None
		bestValue=0
		for item in classifications:
			if rank_order[item[0]]>bestValue:
				bestRank=item
				bestValue=rank_order[item[0]]
		return bestRank

string="7S KS 6C 2S 4D AC QS 5H TS JD"

hand1=string[:14]
hand2=string[15:]

hand1=Hand(hand1.split())
hand2=Hand(hand2.split())

print(hand1.get_rank(), hand1.bestCards)
print(hand2.get_rank(), hand2.bestCards)

print(compareHands(hand1, hand2))


file=open("p054_poker.txt", "r")
plies=[]
player1=0
player2=0
for line in file:
	line=line.replace('\n', "")
	hand1=line[:14]
	hand2=line[15:]
	cards1=hand1.split()
	cards2=hand2.split()
	winner=compareHands(Hand(cards1), Hand(cards2))
	print(hand1, ", ", hand2, ", ", winner)
	if winner=="Player 2":
		player2+=1
	else:
		player1+=1

print(player1)
