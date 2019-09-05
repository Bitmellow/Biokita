class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
    def parse(self):
        while self.index < len(self.tokens):
            token_type = self.tokens[self.index][0]
            token_value = self.tokens[self.index][1]
            
            if token_value == "tree" and token_type == "OBJ_DEFINER":
                before_end = 0
                for i in self.tokens[self.index:len(self.tokens)]:
                    if i[1] == "}" and i[0] == "ROOT_CLOSING":
                        before_end += 1
                        break
                    else:
                        before_end += 1
                self.parse_tree_declaration(self.tokens[self.index:before_end])


            self.index += 1
    
    def parse_tree_declaration(self, token_stream):
        for i in token_stream:
            token_type = i[0]
            token_value = i[1]
            