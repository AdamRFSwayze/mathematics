import string
import random

# corpus taken from article about Nikola Tesla
corpus = "Nikola Tesla is finally beginning to attract real attention and encourage serious debate more than 70 years after his death. Was he for real? A crackpot? Part of an early experiment in corporate government control? We know that he was undoubtedly persecuted by the energy power brokers of his day namely Thomas Edison, whom we are taught in school to revere as a genius. He was also attacked by J.P. Morgan and other captains of industry. Upon Tesla's death on January 7th, 1943, the U.S. government moved into his lab and apartment confiscating all of his scientific research, some of which has been released by the FBI through the Freedom of Information Act. I've embedded the first 250 pages below and have added a link to the .pdf of the final pages, 290 in total. Besides his persecution by corporate government interests which is practically a certification of authenticity, there is at least one solid indication of Nikola Tesla's integrity he tore up a contract with Westinghouse that was worth billions in order to save the company from paying him his huge royalty payments. But, let's take a look at what Nikola Tesla a man who died broke and alone has actually given to the world. For better or worse, with credit or without, he changed the face of the planet in ways that perhaps no man ever has. This is where it all began, and what ultimately caused such a stir at the 1893 World's Expo in Chicago. A war was leveled ever after between the vision of Edison and the vision of Tesla for how electricity would be produced and distributed. The division can be summarized as one of cost and safety: The DC current that Edison backed by General Electric had been working on was costly over long distances, and produced dangerous sparking from the required converter called a commutator. Regardless, Edison and his backers utilized the general dangers of electric current to instill fear in Tesla's alternative: Alternating Current. As proof, Edison sometimes electrocuted animals at demonstrations. Consequently, Edison gave the world the electric chair, while simultaneously maligning Tesla's attempt to offer safety at a lower cost. Tesla responded by demonstrating that AC was perfectly safe by famously shooting current through his own body to produce light. This Edison Tesla GE Westinghouse feud in 1893 was the culmination of over a decade of shady business deals, stolen ideas, and patent suppression that Edison and his moneyed interests wielded over Tesla's inventions. Yet, despite it all, it is Tesla's system that provides power generation and distribution to North America in our modern era. Of course he didn't invent light itself, but he did invent how light can be harnessed and distributed. Tesla developed and used fluorescent bulbs in his lab some 40 years before industry invented them. At the World's Fair, Tesla took glass tubes and bent them into famous scientists' names, in effect creating the first neon signs. However, it is his Tesla Coil that might be the most impressive, and controversial. The Tesla Coil is certainly something that big industry would have liked to suppress: the concept that the Earth itself is a magnet that can generate electricity electromagnetism utilizing frequencies as a transmitter. All that is needed on the other end is the receiver much like a radio. These two are inextricably linked, as they were the last straw for the power elite what good is energy if it can't be metered and controlled? Free? Never. J.P. Morgan backed Tesla with $150,000 to build a tower that would use the natural frequencies of our universe to transmit data, including a wide range of information communicated through images, voice messages, and text. This represented the world's first wireless communications, but it also meant that aside from the cost of the tower itself, the universe was filled with free energy that could be utilized to form a world wide web connecting all people in all places, as well as allow people to harness the free energy around them. Essentially, the 0's and 1's of the universe are embedded in the fabric of existence for each of us to access as needed. Nikola Tesla was dedicated to empowering the individual to receive and transmit this data virtually free of charge. But we know the ending to that story until now? Tesla had perhaps thousands of other ideas and inventions that remain unreleased. A look at his hundreds of patents shows a glimpse of the scope he intended to offer. If you feel that the additional technical and scientific research of Nikola Tesla should be revealed for public scrutiny and discussion, instead of suppressed by big industry and even our supposed institutions of higher education, join the world's call to tell power brokers everywhere that we are ready to Occupy Energy and learn about what our universe really has to offer. The release of Nikola Tesla's technical and scientific research specifically his research into harnessing electricity from the ionosphere at a facility called Wardenclyffe is a necessary step toward true freedom of information. Please add your voice by sharing this information with as many people as possible."

def initialize(corpus, chain):
    # randomly choose starting state
    initial = random.randint(0, len(corpus)-1)
    last_word = ''
    # if chain is empty (starting from the beginning)
    if chain == '':
        if initial+1 > len(corpus)-1:
            chain += corpus[initial] + ' ' + corpus[0] + ' '
            last_word = corpus[0]
        else:
            chain += corpus[initial] + ' ' + corpus[initial+1] + ' '
            last_word = corpus[initial+1]
    else:
        chain += corpus[initial]
    return chain, last_word

def markov_chain(corpus, ngram=2):
    # start markov chain
    last_word = corpus[random.randint(0, len(corpus)-1)]
    chain = last_word + ' '
    for i in range(0, 17):
        # put ngram in bucket (have to put it
        # in loop due to generator object)
        bucket = zip(*[corpus[i:] for i in range(ngram)])
        # generate list of next words given last word
        choices = []
        for index, gram in enumerate(bucket):
            if gram[0] == last_word:
                choices.append(gram)
        # if choices are empty, randomly pick another word
        if len(choices) == 0:
            last_word = corpus[random.randint(0, len(corpus)-1)]
        else:
            random_choice = random.choice(choices)
            chain += ' '.join(random_choice[-(ngram-1):]) + ' '
            last_word = random_choice[-1]
    return chain

# clean text
corpus = corpus.lower()
exclude = set(string.punctuation)
corpus = ''.join(str(ch) for ch in corpus if ch not in exclude)
corpus = corpus.split(' ')

# generate markov chain
chain = markov_chain(corpus, ngram=2).strip()
print('"' + chain + '"')