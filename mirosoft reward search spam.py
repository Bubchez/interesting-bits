# make a microsoft edge tab and click into the search bar
import pyautogui, time, random, keyboard

list = ['able', 'above', 'according', 'across', 'action', 'actually', 'address', 'admit', 'affect', 'again', 'age', 'agent', 'agree', 'ahead', 'all', 'almost', 'along', 'also', 'always', 'among', 'analysis', 'animal', 'answer', 'anyone', 'appear', 'approach', 'argue', 'around', 'art', 'artist', 'ask', 'at', 'attention', 'audience', 'authority', 'avoid', 'baby', 'bad', 'ball', 'bar', 'be', 'beautiful', 'become', 'before', 'behavior', 'believe', 'best', 'between', 'big', 'billion', 'black', 'blue', 'body', 'born', 'box', 'break', 'brother', 'build', 'business', 'buy', 'call', 'campaign', 'cancer', 'capital', 'card', 'career', 'case', 'cause', 'center', 'century', 'certainly', 'challenge', 'change', 'charge', 'child', 'choose', 'citizen', 'civil', 'class', 'clearly', 'coach', 'collection', 'color', 'commercial', 'community', 'compare', 'concern', 'conference', 'consider', 'contain', 'control', 'could', 'couple', 'court', 'create', 'cultural', 'cup', 'customer', 'dark', 'daughter', 'dead', 'death', 'decade', 'decision', 'defense', 'Democrat', 'describe', 'despite', 'determine', 'development', 'difference', 'difficult', 'direction', 'discover', 'discussion', 'do', 'dog', 'down', 'dream', 'drop', 'during', 'early', 'easy', 'economic', 'edge', 'effect', 'eight', 'election', 'employee', 'energy', 'enough', 'entire', 'environmental', 'establish', 'evening', 'ever', 'everybody', 'everything', 'exactly', 'executive', 'expect', 'expert', 'eye', 'fact', 'fail', 'family', 'fast', 'fear', 'feel', 'few', 'fight', 'fill', 'final', 'financial', 'fine', 'finish', 'firm', 'fish', 'floor', 'focus', 'food', 'for', 'foreign', 'form', 'forward', 'free', 'from', 'full', 'future', 'garden', 'general', 'get', 'give', 'go', 'good', 'great', 'ground', 'grow', 'guess', 'guy', 'half', 'hang', 'happy', 'have', 'head', 'hear', 'heat', 'help', 'here', 'high', 'himself', 'history', 'hold', 'hope', 'hot', 'hour', 'how', 'huge', 'hundred', 'I', 'identify', 'image', 'impact', 'improve', 'include', 'increase', 'indicate', 'industry', 'inside', 'institution', 'interesting', 'interview', 'investment', 'issue', 'item', 'itself', 'join', 'keep', 'kid', 'kind', 'know', 'land', 'large', 'late', 'laugh', 'lawyer', 'lead', 'learn', 'leave', 'leg', 'less', 'letter', 'lie', 'light', 'likely', 'list', 'little', 'local', 'look', 'loss', 'love', 'machine', 'main', 'major', 'make', 'manage', 'manager', 'market', 'material', 'may', 'me', 'measure', 'medical', 'meeting', 'memory', 'message', 'middle', 'military', 'mind', 'miss', 'model', 'moment', 'month', 'morning', 'mother', 'move', 'movie', 'Mrs', 'music', 'my', 'name', 'national', 'nature', 'nearly', 'need', 'never', 'news', 'next', 'night', 'none', 'north', 'note', 'notice', "n't", 'occur', 'off', 'office', 'official', 'oh', 'ok', 'on', 'one', 'onto', 'operation', 'option', 'order', 'other', 'our', 'outside', 'own', 'page', 'painting', 'parent', 'participant', 'particularly', 'party', 'past', 'pattern', 'peace', 'per', 'performance', 'period', 'personal', 'physical', 'picture', 'place', 'plant', 'player', 'point', 'policy', 'politics', 'popular', 'position', 'possible', 'practice', 'present', 'pressure', 'prevent', 'private', 'problem', 'produce', 'production', 'professor', 'project', 'protect', 'provide', 'pull', 'push', 'quality', 'quickly', 'race', 'raise', 'rate', 'reach', 'ready', 'reality', 'really', 'receive', 'recently', 'record', 'reduce', 'region', 'relationship', 'remain', 'remove', 'represent', 'require', 'resource', 'response', 'rest', 'return', 'rich', 'rise', 'road', 'role', 'rule', 'safe', 'save', 'scene', 'science', 'score', 'season', 'second', 'security', 'seek', 'sell', 'senior', 'series', 'serve', 'set', 'several', 'sexual', 'share', 'shoot', 'shot', 'shoulder', 'side', 'significant', 'simple', 'since', 'single', 'sit', 'situation', 'size', 'skin', 'smile', 'social', 'soldier', 'somebody', 'something', 'son', 'soon', 'sound', 'south', 'space', 'special', 'speech', 'sport', 'staff', 'stand', 'star', 'state', 'station', 'step', 'stock', 'store', 'strategy', 'strong', 'student', 'stuff', 'subject', 'successful', 'suddenly', 'suggest', 'support', 'surface', 'table', 'talk', 'tax', 'teacher', 'technology', 'tell', 'tend', 'test', 'thank', 'the', 'them', 'then', 'there', 'they', 'think', 'this', 'though', 'thousand', 'three', 'throughout', 'thus', 'to', 'together', 'too', 'total', 'toward', 'trade', 'training', 'treat', 'tree', 'trip', 'true', 'try', 'TV', 'type', 'understand', 'until', 'upon', 'use', 'value', 'very', 'view', 'visit', 'vote', 'walk', 'want', 'watch', 'way', 'weapon', 'week', 'well', 'western', 'whatever', 'where', 'which', 'white', 'whole', 'whose', 'wide', 'will', 'wind', 'wish', 'within', 'woman', 'word', 'worker', 'worry', 'write', 'wrong', 'yeah', 'yes', 'you', 'your']

def search():
    time.sleep(1.5)
    for i in range(90):
        while not keyboard.is_pressed("q"):
            word = list[random.randint(0, len(list))]
            x, y = pyautogui.position()
            pyautogui.click(x, y)
            time.sleep(0.1)
            pyautogui.typewrite(word)
            list.remove(word)
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.5)


#def quiz():
#    x = 394
#    y = 956
#    time.sleep(1)
#    for i in range(2):
#        x = 394
#        for ii in range(10):
#            pyautogui.click(x, y)
#            x += 80
#            time.sleep(2)


search()