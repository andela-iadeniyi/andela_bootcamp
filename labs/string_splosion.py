class StringSplosion(object):
  word = "word"
  
  def __init__(self, word):
    self.word = word
    super(StringSplosion, self).__init__()

  def manipulate(self):
    result = ''
    for i in range(len(self.word)+1):
      result += self.word[:i]
    return result
