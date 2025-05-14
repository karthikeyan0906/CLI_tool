import requests
import sys

def query_word(word):
      url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word)
      response = requests.get(url)

      if response.status_code == 200:
          data = response.json()

          if not data:
              print("no definitions found for : {}".format(word))
              return

          # ftching the data
          #print( data[0] ) 
          definition = data[0]
          

          # Extracting the word's pronunciation
          if 'phonetic' in definition:
              pronunciation = definition['phonetic']
          else:
              pronunciation = "No pronunciation available"

          # Extracting the part of speech (noun, verb, etc.) and the definition
          if 'meanings' in definition:
              meanings = definition['meanings'][0]
              part_of_speech = meanings['partOfSpeech']
              word_definition = meanings['definitions'][0]['definition']
          else:
              part_of_speech = "Unknown"
              word_definition = "No definition available"

          # Formatting the output
          print("{} ({}) : {}".format(word, part_of_speech, word_definition))
          print("Pronunciation: {}".format(pronunciation))
      else:
          print("Error: Unable to fetch data. Status code: {}".format(response.status_code))

  # Main function
def main():
      if len(sys.argv) != 2:
          print("Usage: python dictionary.py <word>")
          sys.exit(1)

      word = sys.argv[1]
      query_word(word)

if __name__ == "__main__":
        main()

