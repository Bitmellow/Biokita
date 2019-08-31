import re

class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code
    def tokenize(self):
        source_text = self.source_code.split()
        source_index = 0
        tokens = []

        for text in source_text:
            if text == "tree":
                tokens.append(["OBJ_DEFINER", text])
            elif re.match("[0-9]", text):
                if text.endswith(","):
                    text = text.replace(",", "")
                    tokens.append(["INTEGER", text])
                    tokens.append(["CONTINOUS_STATEMENT", ","])
                else:
                    tokens.append(["INTEGER", text])

            elif text.startswith("'") or text.startswith('"'):
                if text.startswith("'"):
                    startunit = "'"
                elif text.startswith('"'):
                    startunit = '"'
                string = []
                bendedString = ""
                index2 = 0
                for text2 in source_text:
                    if index2 >= source_index:
                        if text2.endswith(startunit) == False:
                            string.append(text2)
                        elif text2.endswith(startunit):
                            string.append(text2)
                            break
                    index2 += 1                            
                for word in string:
                    if (word.endswith("'") or word.endswith('"')):
                        if (word.endswith("',") or word.endswith('",')):
                            word = word.replace(",", "")
                            bendedString += word
                        else:
                            bendedString += word
                    else:
                        bendedString += word + " "

                if re.search(",", bendedString):
                    bendedString = bendedString.split(",")[0]
                    tokens.append(["STRING", bendedString])
                    tokens.append(["CONTINOUS_STATEMENT", ","])
                else:
                    tokens.append(["STRING", bendedString])
            elif re.match("[A-Z]", text):
                if text.endswith("{"):
                    text = text.replace("{", "")
                    tokens.append(["ROOT_IDENTIFIER", text])
                    tokens.append(["ROOT_OPENING", "{"])
            elif re.match("[a-z]", text):
                if text.endswith(":"):
                    text = text.replace(":", "")
                    tokens.append(["VAR_IDENTIFIER", text])
                    tokens.append(["OPERATOR", ":"])
                else:
                    tokens.append(["VAR_IDENTIFIER", text])
            
            elif text in "+-=/*":
                tokens.append(["OPERATOR", text])
            
            elif text == "{":
                tokens.append(["ROOT_OPENING", text])
            
            elif text == "}":
                tokens.append(["ROOT_CLOSING", text])
            
            source_index += 1
        return tokens
