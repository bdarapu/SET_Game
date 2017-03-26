import sys
import copy

#Categorizing symbols of same type -- symbol will be stored as 'A'or 'S' or 'L' such that by knowing shading(0 or 1 or 2) 
#i can refernce that symbol is '#' by symbol_dict['A'][shading] --> symbols stored in symbol_dict in order of shading 
symbol_dict={'A':['A','a','@'],'H':['H','h','#'] , 'S':['S','s','$']}
A_symbol=['A','a','@']
S_symbol=['S','s','$']
H_symbol=['H','h','#']

#Categorising shadings of same type : lower-case-->1 , upper-case -->2 , symbol-case -->3
shading_dict={'a':1,'s':1,'h':1,'A':0,'H':0,'S':0,'#':2,'@':2,'$':2}


#attributes of a card
attributes=['color','symbol','shading','number']

max_count=0

class cards:
	def __init__(self,color,symbol,shading,number):
		self.color=color
		self.symbol=symbol
		self.shading=shading
		self.number=number

	def __eq__(self,other):
		return self.__dict__==other.__dict__

#parse a line from stdin to class
def parseLineToClass(line):
	line_list=line.split(' ')
	color=line_list[0]
	number=len(line_list[1])
	shading=shading_dict[line_list[1][0]]
	symbol=''
	
	if(line_list[1][0] in A_symbol):
		symbol='A'
	
	if(line_list[1][0] in S_symbol):
		symbol='S'
		
	if(line_list[1][0] in H_symbol):
		symbol='H'
		
	card=cards(color,symbol,shading,number)
	return card


#display list of cards given a list of cards
def display(input_cards):
	set_card=[]
	for card in input_cards:
		color=card.color
		shading=card.shading
		number=card.number
		symbol=card.symbol
		shade=''
		for i in range(number):
			shade+=symbol_dict[symbol][shading]
		display_card=color+" "+shade
		set_card.append(display_card)
	print (set_card)

#check for attributes - return true if all 3 are equal or all 3 are different else false
def valid_attribute(card1,card2,card3,attribute):
	
	if(attribute=='color'):
		if(not((card1.color==card2.color and card1.color==card3.color) or
		 (card1.color!=card2.color and card2.color!=card3.color and card1.color!=card3.color))):
			return False
		# else:
		# 	return False
	if(attribute=='symbol'):
		if(not((card1.symbol==card2.symbol and card1.symbol==card3.symbol) or
		 (card1.symbol!=card2.symbol and card2.symbol!=card3.symbol and card1.symbol!=card3.symbol))):
			return False
		# else:
		# 	return False
	if(attribute=='shading'):
		if(not((card1.shading==card2.shading and card1.shading==card3.shading) or 
			(card1.shading!=card2.shading and card2.shading!=card3.shading and card1.shading!=card3.shading))):
			return False
		# else:
		# 	return False
	if(attribute=='number'):
		if(not((card1.number==card2.number and card1.number==card3.number) or 
			(card1.number!=card2.number and card2.number!=card3.number and card1.number!=card3.number))):
			return False
		# else:
		# 	return False
	return True



#returns the list of triples of valid sets
def valid_set(input_cards):
	valid_triples=[]
	size=len(input_cards)
	for i in range(size):
		card1=input_cards[i]
		for j in range(i+1,size):
			card2=input_cards[j]
			for k in range(j+1,size):
				card3=input_cards[k]
				if(valid_attribute(card1,card2,card3,'color') and valid_attribute(card1,card2,card3,'symbol')
				 and valid_attribute(card1,card2,card3,'shading') and valid_attribute(card1,card2,card3,'number')):
					triple_set=[card1,card2,card3]
					valid_triples.append(triple_set)
	return valid_triples

#check if two triples are disjoint or not
def check_disjoint(triple1,triple2):
	for card1 in triple1:
		for card2 in triple2:
			if(card1==card2): return False
	return True



#get disjoint triples for a given triple - find triples disjoint with "triple" and return it as a list
def get_disjoint_triples(valid_triples,triple):
	size=len(valid_triples)
	disjoint_sets=[triple]
	for triple1 in valid_triples:
		count=0
		for triple2 in disjoint_sets:
			if(check_disjoint(triple1,triple2)):
				count+=1
		if(count==len(disjoint_sets)):
			disjoint_sets.append(triple1)
				
	return disjoint_sets
		


#display output in the given format
def display_output(valid_triples):
	for triple in valid_triples:
		for card in triple:
			color=card.color
			shading=card.shading
			number=card.number
			symbol=card.symbol
			shade=''
			for i in range(number):
				shade+=symbol_dict[symbol][shading]
			display_card=color+" "+shade
			print(display_card)
		print("\n")

#check if all the triples in the input are disjoint
def checkAlltriplesDisjoint(valid_triples):
	for i in range(len(valid_triples)):
		count=0 # counts the number of triples that are disjoint with elemant at index i
		for j in range(i+1,len(valid_triples)):
			if(check_disjoint(valid_triples[i],valid_triples[j])): count+=1
		if(count!=len(valid_triples)-(i+1)): 
			return False
	return True

#a recursive backtracking function to calculate maximum disjoint sets
#removing one element at a time and check for disjoint triples via backtracking
# def maximum_disjoint_sets(valid_triples,start,max_count):
# 	global result
# 	if(start>=len(valid_triples)): return
# 	# print("outside test")
# 	#check if all elements in the set are disjoint
# 	if(checkAlltriplesDisjoint(valid_triples)):
# 		# print("test")
# 		if(len(valid_triples)>max_count):
# 			max_count=len(valid_triples)
# 			result=copy.deepcopy(valid_triples)
# 		return

# 	for i in range(len(valid_triples)):
# 		# sub_valid_triples=copy.deepcopy(valid_triples)
# 		removed_triple=valid_triples.pop(i)
# 		maximum_disjoint_sets(valid_triples,i+1,max_count) 
# 		valid_triples.insert(i,removed_triple) 28 input taking too long - convert represenation to numeric rep. and try
#for

def maximum_disjoint_sets(valid_triples,triples_picked,cards_picked,start,count):
	
	global result,max_count
	# ,sets,size
	
	if(start>=len(valid_triples)): return

	if(count>=max_count):
		max_count=count
		result=copy.deepcopy(triples_picked)

	maximum_disjoint_sets(valid_triples,copy.deepcopy(triples_picked),copy.deepcopy(cards_picked),start+1,count)

	curr_triple=valid_triples[start]
	# print("curr_triple at start: ",start)
	# display_output([curr_triple])
	if((curr_triple[0] not in cards_picked) and (curr_triple[1] not in cards_picked) and (curr_triple[2] not in cards_picked)):
		triples_picked.append(curr_triple)
		cards_picked.append(curr_triple[0])
		cards_picked.append(curr_triple[1])
		cards_picked.append(curr_triple[2])
		# print("cards picked count: ")
		count+=1

		
		if(count>=max_count):
			# print("test..")
			# display_output(triples_picked)
			max_count=count
			result=copy.deepcopy(triples_picked)

		# if(max_count>6): print("mising these recursions: ")

		maximum_disjoint_sets(valid_triples,copy.deepcopy(triples_picked),copy.deepcopy(cards_picked),start+1,count)

	return







if __name__=='__main__':
	# infile=sys.stdin
	# input_size=int(next(infile))
	input_cards=[]

	#reading input from file
	with open('input.txt', 'r') as infile:
		input_size=int(infile.readline()[:-1])
		while input_size:
			line=infile.readline()[:-1]
			print(line)
			card=parseLineToClass(line)
			input_cards.append(card)
			input_size-=1

	#reading input from stdin
	# while input_size:
	# 	line=next(infile)[:-1]
	# 	card=parseLineToClass(line)
	# 	input_cards.append(card)
	# 	input_size-=1

	if(len(input_cards)<3): 
		print("Number of cards should be more than 3")
		sys.exit(0)
	display(input_cards)

	print("size of input: ",len(input_cards))
	
	valid_triples=valid_set(input_cards)
	print("Possible sets:   ",len(valid_triples))
	display_output(valid_triples)

	# global triples_picked,cards_picked
	# triples_picked=[]
	# cards_picked=[]
	# global sets,size
	# sets=valid_triples
	# size=len(valid_triples)
	global max_count
	maximum_disjoint_sets(valid_triples,[],[],0,0)

	if(len(valid_triples)>0):
		print("Number of Disjoint sets: ",len(result))
		display_output(result)
	else :
		print("Number of Disjoint sets: ",0)
	
	# dict_disjoint_set={} # dictionary for disjoint set with each triple in valid_triples
	# for i,triple in enumerate(valid_triples):
	# 	dict_disjoint_set[i]=get_disjoint_triples(valid_triples,triple)

	# print("length of dictionary: ",len(dict_disjoint_set))

	# #finding the key where the length of list is maximum
	# max_len=len(dict_disjoint_set[0])
	# index=0
	# for i in range(len(dict_disjoint_set)):
	# 	if(len(dict_disjoint_set[i])>max_len):
	# 		max_len=len(dict_disjoint_set[i])
	# 		index=i
	

	# print("Size of maximum disjoint set: ",max_len)
	# display_output(dict_disjoint_set[index])



	





