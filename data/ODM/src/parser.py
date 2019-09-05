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
        tokens_checked = 0

        for token in range(0, len(token_stream))
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            
            if token == 0 and token_type == "OBJ_DEFINER":
                last_declaration = "tree"
            
            elif token == 1 and token_type == "ROOT_IDENTIFIER":
                if last_declaration == "tree":
                    tree = [token_value, {}]
                else:
                    print("ERROR: Can't merge a tree without tree declaration")
                    raise("UndeclaredError")

            elif token == 2 and token_type != "ROOT_OPENING":
                raise("RootError")

            tokens_checked += 1